# Project 3: Data use policy

## 1. What can happen?

An assistant might use a document for the wrong purpose, expose a restricted record, or keep using expired material.

**Example** A policy document is suitable for HR answers but is being selected for marketing.

## 2. Our idea

We inspect fictional document metadata and an application-owned context. Ordinary Python checks purpose, audience, classification, and expiry. A separate retention preview lists work to review without deleting anything.

### How we do it

1. Check documents with the original marketing purpose.
2. Change only the context purpose to answer_hr_policy.
3. Compare decisions and preview expired records.

## 3. How it helps

The public policy becomes allowed. The restricted employee record and expired policy stay blocked. Metadata checks depend on trustworthy classification and application context; they do not authenticate a user.

## 4. Input and setup

Run these commands in PowerShell:

```powershell
# Run from the learning-governance repository root.
uv sync --locked
```

Open `3_data_use_policy` as a folder in VS Code, then open
[data_use_policy.ipynb](data_use_policy.ipynb). Select the repository root's
`.venv/Scripts/python.exe` kernel. Use this numbered folder as the
notebook working directory. Restart the kernel after helper edits or switching lessons.

The standard folders are docs/dataset, docs/goldends, docs/evaluatedds,
docs/evalresults, models, prompts, and tools. Empty folders are reserved;
no artificial data, model, or prompt is needed to fill them.

| File | What it does |
| --- | --- |
| [docs/dataset/documents.json](docs/dataset/documents.json) | Fictional document metadata, not employee contents. |
| [docs/dataset/policy.json](docs/dataset/policy.json) | Example classification/audience rules. |
| [docs/dataset/request_context.json](docs/dataset/request_context.json) | Separate app-owned purpose and audience fixture. |
| [tools/data_policy.py](tools/data_policy.py) | Purpose/access/expiry checks and retention dry run. |

Baseline: all three documents are blocked. After the purpose change, POLICY-1 is allowed; EMPLOYEE-1 and OLD-POLICY remain blocked. Expiry is inclusive: expires_on <= 2026-11-15 is expired.

Changes are in memory. This notebook writes no files.

All example inputs, reports, and sample decisions are fictional teaching
fixtures. No model calls or API keys are needed. The learner's own judgments,
approvals, and run remain pending.

The notebook is prepared for your run. See the
[repository README](../README.md) for shared setup and verification. Work through one cell at a time.
