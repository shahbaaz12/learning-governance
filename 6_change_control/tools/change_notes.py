"""Check the context recorded for a change; this grants no release approval."""


def check_change_note(note, before_manifest, after_manifest):
    links_match = (
        note.get("before_manifest_id") == before_manifest["manifest_id"]
        and note.get("after_manifest_id") == after_manifest["manifest_id"]
    )
    issues = []
    if not links_match:
        issues.append("change note does not identify these before/after versions")
    for field in ("reason", "expected_behavior"):
        value = note.get(field)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"{field} is missing")

    planned = note.get("planned_retests", [])
    planned_ids = [case.get("case_id") for case in planned]
    if (
        not planned_ids
        or any(not isinstance(case_id, str) or not case_id.strip() for case_id in planned_ids)
        or len(set(planned_ids)) != len(planned_ids)
    ):
        issues.append("planned retest IDs must be present and unique")

    results = note.get("retest_results", [])
    retest_status = note.get("retest_status")
    if retest_status == "pending":
        if results:
            issues.append("pending retests must not claim completed results")
    elif retest_status == "completed":
        result_ids = [result.get("case_id") for result in results]
        if len(result_ids) != len(planned_ids) or set(result_ids) != set(planned_ids):
            issues.append("completed retests need one result for every planned case")
        for result in results:
            if result.get("outcome") not in ("pass", "fail"):
                issues.append("each recorded result needs a pass/fail outcome")
            for field in ("observation", "evidence_ref"):
                value = result.get(field)
                if not isinstance(value, str) or not value.strip():
                    issues.append(f"each recorded result needs {field}")
    else:
        issues.append("retest_status must be pending or completed")

    return {"links_match": links_match, "issues": issues, "retest_status": retest_status}
