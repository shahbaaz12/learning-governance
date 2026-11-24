"""Check explicitly synthetic reports against an example release policy."""


def check_evidence(release, report, policy):
    if report is None:
        return {"decision": "blocked", "reasons": ["evaluation report missing"]}

    required = ("release_id", "quality_dataset", "privacy_dataset", "correct", "total", "privacy_failures", "privacy_tests")
    missing = [field for field in required if field not in report]
    if missing:
        return {"decision": "blocked", "reasons": ["report fields missing: " + ", ".join(missing)]}

    counts = ("correct", "total", "privacy_failures", "privacy_tests")
    if any(type(report[field]) is not int or report[field] < 0 for field in counts):
        return {"decision": "blocked", "reasons": ["report counts must be nonnegative integers"]}
    if report["total"] == 0 or report["privacy_tests"] == 0:
        return {"decision": "blocked", "reasons": ["test coverage is empty"]}
    if report["correct"] > report["total"] or report["privacy_failures"] > report["privacy_tests"]:
        return {"decision": "blocked", "reasons": ["inconsistent report counts"]}

    reasons = []
    if report["release_id"] != release["release_id"]:
        reasons.append("report belongs to another release")
    if report["quality_dataset"] != policy["quality_dataset"] or report["privacy_dataset"] != policy["privacy_dataset"]:
        reasons.append("unexpected test dataset")
    if report["total"] < policy["min_quality_tests"] or report["privacy_tests"] < policy["min_privacy_tests"]:
        reasons.append("required test coverage missing")
    if report["correct"] / report["total"] < policy["min_accuracy"]:
        reasons.append("accuracy below the example requirement")
    if report["privacy_failures"] > policy["max_privacy_failures"]:
        reasons.append("observed privacy failures exceed the example requirement")

    return {
        "decision": "blocked" if reasons else "ready_for_human_review",
        "reasons": reasons or ["matching evidence passed; human approval still required"],
    }


def check_cases(release, reports, policy):
    return {name: check_evidence(release, report, policy) for name, report in reports.items()}


def show_results(results):
    for name, result in results.items():
        print(name, result["decision"], "|", "; ".join(result["reasons"]))
