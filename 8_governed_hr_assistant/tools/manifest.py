"""Identify local release artifacts and compare explicitly fictional records."""

import hashlib
import json


def build_manifest(project_dir, release):
    artifacts = {}
    for kind, relative_path in release["artifacts"].items():
        content = (project_dir / relative_path).read_bytes()
        artifacts[kind] = {"path": relative_path, "sha256": hashlib.sha256(content).hexdigest()}
    manifest = {"release_id": release["release_id"], "artifacts": artifacts}
    content = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
    manifest["manifest_id"] = hashlib.sha256(content).hexdigest()
    return manifest


def check_bindings(manifest, records):
    reasons = []
    for name, field, required in (("evaluation", "status", "passed"), ("approval", "decision", "approved")):
        record = records.get(name) or {}
        if record.get("release_id") != manifest["release_id"]:
            reasons.append(f"{name} release ID mismatch")
        if record.get("manifest_id") != manifest["manifest_id"]:
            reasons.append(f"{name} does not cover these artifacts")
        if record.get(field) != required:
            reasons.append(f"{name} is not {required}")
    return {
        "decision": "needs_evaluation_and_review" if reasons else "bindings_match",
        "reasons": reasons or ["fictional records match these artifact identities"],
    }
