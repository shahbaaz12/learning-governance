"""Enforce a small fictional suspension and recovery policy."""

from models.demo import respond


def check_recovery(incident, release, recovery, evidence, reviewers):
    reasons = []
    incident_id = incident["incident_id"]
    if recovery.get("incident_id") != incident_id or recovery.get("release_id") != release["release_id"]:
        reasons.append("recovery does not identify this incident and release")

    investigation = evidence["investigations"].get(recovery.get("investigation_ref"), {})
    if investigation.get("incident_id") != incident_id or investigation.get("contained") is not True:
        reasons.append("matching containment investigation missing")

    retest = evidence["retests"].get(recovery.get("retest_ref"), {})
    if retest.get("incident_id") != incident_id or retest.get("release_id") != release["release_id"] or retest.get("passed") is not True:
        reasons.append("matching passed retest missing")

    approval = recovery.get("approval") or {}
    reviewer = reviewers.get(approval.get("reviewer_id"), {})
    if reviewer.get("active") is not True or "incident_owner" not in reviewer.get("roles", []):
        reasons.append("authorized recovery reviewer missing")
    if approval.get("decision") != "approved" or approval.get("incident_id") != incident_id or approval.get("release_id") != release["release_id"]:
        reasons.append("explicit recovery approval for this incident and release missing")
    return reasons


def application_state(incidents, release, recoveries, evidence, reviewers, policy):
    reasons = []
    for incident in incidents:
        if incident["system_id"] != release["system_id"]:
            continue
        if incident["confirmation"] != "confirmed" or incident["category"] not in policy["suspend_categories"]:
            continue
        recovery = recoveries.get(incident["incident_id"], {})
        gaps = check_recovery(incident, release, recovery, evidence, reviewers)
        reasons.extend(f"{incident['incident_id']}: {gap}" for gap in gaps)
    return {
        "status": "suspended" if reasons else "active",
        "response_owner": policy["response_owner"],
        "reasons": reasons or ["no outstanding suspension under this example policy"],
    }


def guarded_reply(question, state, calls):
    if state["status"] != "active":
        return {"decision": "blocked", "response": None, "reasons": state["reasons"], "model_api_calls": 0}
    return {"decision": "allow", "response": respond(question, calls), "reasons": state["reasons"], "model_api_calls": 0}
