"""Demonstrate authority checks on explicitly fictional approval records."""


def check_approval(release, approval, reviewers):
    if not approval or approval.get("decision") == "pending":
        return {"decision": "pending", "reasons": ["human approval pending"]}

    reasons = []
    reviewer_id = approval.get("reviewer_id")
    reviewer = reviewers.get(reviewer_id, {})
    if reviewer.get("active") is not True or "release_reviewer" not in reviewer.get("roles", []):
        reasons.append("reviewer has no active release-review authority")
    if reviewer_id == release.get("author_id"):
        reasons.append("the example policy requires a separate reviewer")
    if approval.get("release_id") != release["release_id"]:
        reasons.append("approval belongs to another release")
    if reasons:
        return {"decision": "blocked", "reasons": reasons}
    if approval.get("decision") == "rejected":
        return {"decision": "rejected", "reasons": ["authorized reviewer rejected this release"]}
    if approval.get("decision") != "approved":
        return {"decision": "blocked", "reasons": ["explicit approval missing"]}
    return {"decision": "approved", "reasons": ["fictional authorized approval matches this release"]}


def check_cases(release, approvals, reviewers):
    return {name: check_approval(release, approval, reviewers) for name, approval in approvals.items()}


def show_results(results):
    for name, result in results.items():
        print(name, result["decision"], "|", "; ".join(result["reasons"]))
