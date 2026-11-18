# Project 4: Release evidence

## 1. What can happen?

A report may look good but describe a different release or cover too few examples.

**Example** The current assistant is hr-v1, but a passing report belongs to hr-v0.

## 2. Our idea

We load four explicitly synthetic report cases and an example release policy. A release gate checks evidence before handing the release to a person for review. This lesson does not run an evaluation or deploy an application.

### How we do it

1. Inspect missing, failing, wrong-version, and passing reports.
2. Check version, dataset identity, coverage, accuracy, and observed privacy failures.
3. Replace only the wrong-version evidence selection with the existing current-version report and compare.

## 3. How it helps

A current passing report makes a release ready for human review. It provides no human approval. Zero privacy failures describes only this fixture's test set, not a guarantee.

## 4. Input and setup

Run these commands in PowerShell:

```powershell
# Run from the learning-governance repository root.
uv sync --locked
```

Open `4_release_evidence` as a folder in VS Code, then open
[release_evidence.ipynb](release_evidence.ipynb). Select the repository root's
`.venv/Scripts/python.exe` kernel. Use this numbered folder as the
notebook working directory. Restart the kernel after helper edits or switching lessons.

The standard folders are docs/dataset, docs/goldends, docs/evaluatedds,
docs/evalresults, models, prompts, and tools. Empty folders are reserved;
no artificial data, model, or prompt is needed to fill them.

| File | What it does |
| --- | --- |
| [docs/dataset/release.json](docs/dataset/release.json) | The release being considered. |
| [docs/dataset/policy.json](docs/dataset/policy.json) | Illustrative thresholds and required dataset identities. |
| [docs/dataset/reports.json](docs/dataset/reports.json) | Synthetic counts and explicit missing/failing/mismatched/passing cases. |
| [tools/evidence.py](tools/evidence.py) | Checks coverage and report identity before allowing human review. |

Initially only passing is ready_for_human_review. Selecting the current-version report for wrong_version makes that case ready too. Missing and failing cases stay blocked. Do not relabel an old report as fresh evidence.

Changes are in memory. This notebook writes no files.

All example inputs, reports, and sample decisions are fictional teaching
fixtures. No model calls or API keys are needed. The learner's own judgments,
approvals, and run remain pending.

The notebook is prepared for your run. See the
[repository README](../README.md) for shared setup and verification. Work through one cell at a time.
