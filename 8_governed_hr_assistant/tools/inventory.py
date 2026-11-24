"""Check fictional inventory records; this does not authorize deployment."""

from datetime import date


REQUIRED_FIELDS = ("system_id", "name", "purpose", "owner", "next_review_on")


def check_system(system, as_of):
    """Return a documentation decision for one record with ISO-format dates."""
    missing = [
        field
        for field in REQUIRED_FIELDS
        if not isinstance(system.get(field), str) or not system[field].strip()
    ]

    if missing:
        status = "incomplete"
        reason = "Missing or blank: " + ", ".join(missing)
    elif date.fromisoformat(system["next_review_on"]) <= as_of:
        status = "review_due"
        reason = f"Review due on {system['next_review_on']} (sample date: {as_of})."
    else:
        status = "complete"
        reason = "Required fields present; next review is in the future."

    return {"system_id": system.get("system_id", "(missing)"), "status": status, "reason": reason}


def check_inventory(systems, as_of):
    """Check each record without changing the supplied inventory."""
    return [check_system(system, as_of) for system in systems]


def show_results(results):
    """Print each decision with its reason."""
    for result in results:
        print(f"{result['system_id']}: {result['status']} | {result['reason']}")
