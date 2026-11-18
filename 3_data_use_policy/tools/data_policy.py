"""Check fictional document metadata and preview retention work without deleting."""

from datetime import date


def check_document(document, context, policy, as_of):
    reasons = []
    classification = document["classification"]
    if classification not in policy["classification_audiences"]:
        reasons.append("unknown classification")
    if context["purpose"] not in document["permitted_purposes"]:
        reasons.append("purpose not permitted")
    permitted = policy["classification_audiences"].get(classification, [])
    if context["audience"] not in permitted or context["audience"] not in document["permitted_audiences"]:
        reasons.append("audience not permitted")
    if date.fromisoformat(document["expires_on"]) <= as_of:
        reasons.append("retention expiry reached")
    return {
        "data_id": document["data_id"],
        "decision": "block" if reasons else "allow",
        "reasons": reasons or ["purpose, audience, and expiry checks passed"],
    }


def check_documents(documents, context, policy, as_of):
    return [check_document(document, context, policy, as_of) for document in documents]


def retention_preview(documents, as_of):
    return [
        {"data_id": item["data_id"], "action": "review_retention", "expires_on": item["expires_on"]}
        for item in documents
        if date.fromisoformat(item["expires_on"]) <= as_of
    ]


def show_results(results):
    for result in results:
        print(result["data_id"], result["decision"], "|", "; ".join(result["reasons"]))
