"""Save observations from a local run, preserving previous reports."""

import json
from datetime import datetime, timezone
from uuid import uuid4


def save_report(results, output_dir, label):
    assert label in ("baseline", "candidate"), "Choose the baseline or candidate label."
    output_dir.mkdir(parents=True, exist_ok=True)
    created_at = datetime.now(timezone.utc)
    stem = created_at.strftime("%Y%m%dT%H%M%S%fZ") + "_" + label + "_" + uuid4().hex[:8]
    payload = {
        "created_at": created_at.isoformat(),
        "experiment": label,
        "provenance": "actual local check execution on fictional governance inputs; no real approval or model call",
        "results": results,
    }
    json_path = output_dir / (stem + ".json")
    markdown_path = output_dir / (stem + ".md")
    with json_path.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, indent=2)
    lines = [
        f"# Governance decision report: {label}",
        "",
        "Actual local checks on fictional inputs. Learner decisions remain pending.",
        f"Created at (UTC): {created_at.isoformat()}",
        "",
        "| Case | Release | Decision | Local calls | Manifest | Reasons |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for result in results:
        lines.append(f"| {result['case_id']} | {result['release_id']} | {result['decision']} | {result['local_responder_calls']} | {result['manifest']['manifest_id'][:12]} | {'; '.join(result['reasons'])} |")
    lines += ["", "The JSON companion contains full artifact identities, check results, input references, and outstanding work.", "These files are editable local observations, not authenticated or tamper-proof audit storage."]
    with markdown_path.open("x", encoding="utf-8") as stream:
        stream.write("\n".join(lines) + "\n")
    return {"json": str(json_path), "markdown": str(markdown_path)}
