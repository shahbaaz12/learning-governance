"""Compose the learned checks before a local demonstration responder."""

from copy import deepcopy
import json

from models.demo import respond
from tools.approvals import check_approval
from tools.data_policy import check_documents
from tools.evidence import check_evidence
from tools.inventory import check_system
from tools.manifest import build_manifest, check_bindings


def check_risks(risks, evidence, reviewers, release):
    reasons = []
    if not risks:
        reasons.append("risk register missing")
    for risk in risks:
        reviewer = reviewers.get(risk.get("reviewer_id"), {})
        if not risk.get("owner", "").strip() or risk.get("evidence_id") not in evidence:
            reasons.append(f"{risk['risk_id']}: owner or control evidence missing")
        if risk.get("system_id") != release["system_id"] or risk.get("release_id") != release["release_id"]:
            reasons.append(f"{risk['risk_id']}: risk review belongs to another application or release")
        if reviewer.get("active") is not True or "risk_reviewer" not in reviewer.get("roles", []):
            reasons.append(f"{risk['risk_id']}: authorized risk reviewer missing")
        if risk.get("decision") != "accepted":
            reasons.append(f"{risk['risk_id']}: explicit fictional risk acceptance missing")
    return reasons


def prepare_case(base, scenario):
    case = deepcopy(base)
    case["case_id"] = scenario["case_id"]
    case["report"] = deepcopy(base["reports"].get(scenario["report_id"]))
    case["release"]["artifacts"]["prompt"] = scenario["prompt_file"]
    case["incidents"] = deepcopy(scenario["incidents"])
    return case


def review_case(case, project_dir, as_of):
    release = case["release"]
    policy = json.loads((project_dir / release["artifacts"]["policy"]).read_text(encoding="utf-8"))
    manifest = build_manifest(project_dir, release)
    checks = []

    profile = check_system(case["profile"], as_of)
    profile_ok = profile["status"] == "complete" and case["profile"]["system_id"] == release["system_id"]
    checks.append({"stage": "inventory", "passed": profile_ok, "reasons": [profile["reason"] if profile_ok else "profile incomplete, review due, or application mismatch"]})

    risk_gaps = check_risks(case["risks"], case["risk_evidence"], case["reviewers"], release)
    checks.append({"stage": "risk_review", "passed": not risk_gaps, "reasons": risk_gaps or ["fictional risk review recorded; residual concerns remain documented"]})

    data_results = check_documents(case["documents"], case["context"], policy, as_of)
    data_gaps = [f"{item['data_id']}: {reason}" for item in data_results if item["decision"] != "allow" for reason in item["reasons"]]
    if not data_results:
        data_gaps.append("no approved context documents selected")
    checks.append({"stage": "data_use", "passed": not data_gaps, "reasons": data_gaps or ["selected document metadata passed"]})

    evidence = check_evidence(release, case["report"], policy["release_requirements"])
    checks.append({"stage": "evaluation", "passed": evidence["decision"] == "ready_for_human_review", "reasons": evidence["reasons"]})

    bindings = check_bindings(manifest, {"evaluation": case["report"], "approval": case["approval"]})
    checks.append({"stage": "artifact_binding", "passed": bindings["decision"] == "bindings_match", "reasons": bindings["reasons"]})

    approval = check_approval(release, case["approval"], case["reviewers"])
    checks.append({"stage": "release_approval", "passed": approval["decision"] == "approved", "reasons": approval["reasons"]})

    incidents = [item for item in case["incidents"] if item["system_id"] == release["system_id"] and item["confirmation"] == "confirmed" and item["category"] in policy["suspend_categories"]]
    checks.append({"stage": "incident_status", "passed": not incidents, "reasons": ["confirmed incident requires the separate recovery workflow"] if incidents else ["no confirmed in-scope suspension"]})

    gaps = [f"{item['stage']}: {reason}" for item in checks if not item["passed"] for reason in item["reasons"]]
    return {
        "case_id": case["case_id"],
        "release_id": release["release_id"],
        "manifest": manifest,
        "decision": "blocked" if gaps else "allow",
        "reasons": gaps or ["all checks passed under the fictional example policy"],
        "checks": checks,
        "input_references": {
            "system_id": case["profile"]["system_id"],
            "application_owner": case["profile"]["owner"],
            "request_purpose": case["context"]["purpose"],
            "risk_ids": [risk["risk_id"] for risk in case["risks"]],
            "document_ids": [document["data_id"] for document in case["documents"]],
            "report_id": (case["report"] or {}).get("report_id"),
            "fixture_reviewer_id": (case["approval"] or {}).get("reviewer_id"),
            "response_owner": policy["response_owner"],
        },
        "outstanding_work": gaps,
        "learner_decision": "pending; sample decisions are fictional",
    }


def run_cases(base, scenarios, project_dir, as_of):
    results = []
    calls = []
    for scenario in scenarios:
        case = prepare_case(base, scenario)
        result = review_case(case, project_dir, as_of)
        before = len(calls)
        result["response"] = respond(case["question"], calls) if result["decision"] == "allow" else None
        result["local_responder_calls"] = len(calls) - before
        result["model_api_calls"] = 0
        results.append(result)
    return results, calls


def show_results(results):
    for result in results:
        print(result["case_id"], result["decision"], "| local calls:", result["local_responder_calls"])
        print("  ", "; ".join(result["reasons"]))
