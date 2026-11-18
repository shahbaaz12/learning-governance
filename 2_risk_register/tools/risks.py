"""Find documentation gaps in fictional draft risks; never accept risks."""


def assess_risk(risk, evidence):
    gaps = []
    if not risk.get("owner", "").strip():
        gaps.append("owner missing")
    if risk.get("evidence_id") not in evidence:
        gaps.append("control evidence reference missing or unknown")
    reasons = gaps + ["human review pending"]
    if risk.get("unresolved_concern"):
        reasons.append(risk["unresolved_concern"])
    return {
        "risk_id": risk["risk_id"],
        "status": "needs_information" if gaps else "needs_human_review",
        "reasons": reasons,
    }


def assess_register(risks, evidence):
    return [assess_risk(risk, evidence) for risk in risks]


def show_results(results):
    for result in results:
        print(result["risk_id"], result["status"], "|", "; ".join(result["reasons"]))
