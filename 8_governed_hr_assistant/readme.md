# Project 8: Governed HR assistant

## 1. What can happen?

An assistant can pass one check while missing evidence, carrying an old approval, or being suspended after an incident.

**Example** The prompt changes but the selected evaluation and approval still describe the baseline artifacts.

## 2. Our idea

We combine the earlier small checks around a local Python responder. Four fictional cases use the same question. Sample risk acceptance and approval are clearly fictional; the learner's separate approval template is pending. This capstone blocks confirmed privacy incidents; the explicit recovery workflow is studied in Project 7.

### How we do it

1. Inspect the shared fictional application records and four cases.
2. Run inventory, risk, data, evaluation, artifact-binding, approval, and incident checks before the responder.
3. Select existing current evidence for one case and compare the same requests.
4. Save local decision reports with full version identities and remaining work.

## 3. How it helps

Only eligible cases reach the local responder. The logs prove the boundary ran. Passing fixtures do not establish real approvals, authenticated identities, or compliance. Risk concerns remain visible in the source records even when a fictional reviewer accepted them.

## 4. Input and setup

Run these commands in PowerShell:

```powershell
# Run from the learning-governance repository root.
uv sync --locked
```

Open `8_governed_hr_assistant` as a folder in VS Code, then open
[governed_hr_assistant.ipynb](governed_hr_assistant.ipynb). Select the repository root's
`.venv/Scripts/python.exe` kernel. Use this numbered folder as the
notebook working directory. Restart the kernel after helper edits or switching lessons.

The standard folders are docs/dataset, docs/goldends, docs/evaluatedds,
docs/evalresults, models, prompts, and tools. Empty folders are reserved;
no artificial data, model, or prompt is needed to fill them.

| File | What it does |
| --- | --- |
| [docs/dataset/base.json](docs/dataset/base.json) | Shared fictional profile, risks, authority, data, reports, and sample approval. |
| [docs/dataset/cases.json](docs/dataset/cases.json) | Ready, missing-evidence, changed-prompt, and suspended scenarios. |
| [docs/dataset/policy.json](docs/dataset/policy.json) | Policy artifact loaded directly for both fingerprinting and checks. |
| [docs/dataset/baseline_manifest.json](docs/dataset/baseline_manifest.json) | Pinned baseline file identities. |
| [docs/dataset/questions.json](docs/dataset/questions.json) | The fictional question artifact. |
| [docs/dataset/learner_approval.json](docs/dataset/learner_approval.json) | Learner-owned pending approval. |
| [models/demo.py](models/demo.py) | Actual local responder call log. |
| [models/model.json](models/model.json) | Local demo identity; no external provider. |
| [prompts/answer.txt](prompts/answer.txt) | Baseline prompt artifact. |
| [prompts/candidate_answer.txt](prompts/candidate_answer.txt) | One changed instruction. |
| [tools/governance.py](tools/governance.py) | Composes checks and enforces the decision before responding. |
| [tools/inventory.py](tools/inventory.py) | Same small inventory check used in Project 1, copied locally. |
| [tools/data_policy.py](tools/data_policy.py) | Same small data-use checks used in Project 3, copied locally. |
| [tools/evidence.py](tools/evidence.py) | Same small coverage and release checks used in Project 4, copied locally. |
| [tools/approvals.py](tools/approvals.py) | Same small authority checks used in Project 5, copied locally. |
| [tools/manifest.py](tools/manifest.py) | Same small artifact binding checks used in Project 6, copied locally. |
| [tools/reports.py](tools/reports.py) | Writes timestamped JSON and Markdown observations without overwriting earlier reports. |

Baseline: only ready_fixture runs, with 1 actual local responder call. After selecting current evidence for missing_evidence, 2 cases run. changed_prompt and suspended remain blocked. No real model/API calls occur.

Only the final cell writes files: a timestamped baseline JSON/Markdown pair and a separate candidate pair in docs/evalresults. Previous reports, source fixtures, and learner approval remain unchanged.

All example inputs, reports, and sample decisions are fictional teaching
fixtures. No model calls or API keys are needed. The learner's own judgments,
approvals, and run remain pending.

The notebook is prepared for your run. See the
[repository README](../README.md) for shared setup and verification. Work through one cell at a time.
