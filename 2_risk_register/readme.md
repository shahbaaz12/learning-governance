# Project 2: Risk register

## 1. What can happen?

An application can have a named owner while individual risks have nobody responsible for reviewing them.

**Example** The draft privacy risk describes a control but has no owner.

## 2. Our idea

We load three draft risks and two fictional evidence references. A risk register records possible harm, affected people, controls, and unresolved concerns. The helper checks documentation gaps; it never accepts a risk.

### How we do it

1. Read the risks and their fictional evidence references.
2. List missing owners or unknown evidence and keep human review visible.
3. Fill only the privacy risk's owner in a copy and compare.

## 3. How it helps

The owner gap closes, but human review remains pending. A reference existing does not establish that a control works. The contractor risk still has no matching evidence.

## 4. Input and setup

Run these commands in PowerShell:

```powershell
# Run from the learning-governance repository root.
uv sync --locked
```

Open `2_risk_register` as a folder in VS Code, then open
[risk_register.ipynb](risk_register.ipynb). Select the repository root's
`.venv/Scripts/python.exe` kernel. Use this numbered folder as the
notebook working directory. Restart the kernel after helper edits or switching lessons.

The standard folders are docs/dataset, docs/goldends, docs/evaluatedds,
docs/evalresults, models, prompts, and tools. Empty folders are reserved;
no artificial data, model, or prompt is needed to fill them.

| File | What it does |
| --- | --- |
| [docs/dataset/risks.json](docs/dataset/risks.json) | Draft risks, affected people, owners, and concerns. |
| [docs/dataset/evidence.json](docs/dataset/evidence.json) | Fictional observations; not real test results. |
| [docs/dataset/learner_review.json](docs/dataset/learner_review.json) | Blank learner review records; the notebook only reads them. |
| [tools/risks.py](tools/risks.py) | Checks documentation gaps and prints reasons. |

Baseline: R-001 needs_human_review; R-002 and R-003 need information. After assigning the fictional owner, only R-002 changes to needs_human_review. No risk becomes accepted.

Changes are in memory. This notebook writes no files.

All example inputs, reports, and sample decisions are fictional teaching
fixtures. No model calls or API keys are needed. The learner's own judgments,
approvals, and run remain pending.

The notebook is prepared for your run. See the
[repository README](../README.md) for shared setup and verification. Work through one cell at a time.
