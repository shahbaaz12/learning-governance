# Project 5: Human approval

## 1. What can happen?

A passing report does not tell us whether an authorized person approved this release.

**Example** A developer submits a sample approval that claims an HR reviewer role.

## 2. Our idea

We load a fictional reviewer table separately from six sample approval records. The example policy requires an active release reviewer who is different from the author. Local files demonstrate the checks; they do not authenticate people.

### How we do it

1. Compare pending, rejected, unauthorized, wrong-version, approved, and inactive-reviewer fixtures.
2. Use authority from the separate reviewer table; ignore a role claimed inside an approval.
3. Change only the approved sample's release ID and compare. Read your own pending template separately.

## 3. How it helps

Only the authorized sample for this exact release is approved. Changing its release ID blocks it. Technical evidence is a separate prerequisite, and no deployment occurs here.

## 4. Input and setup

Run these commands in PowerShell:

```powershell
# Run from the learning-governance repository root.
uv sync --locked
```

Open `5_human_approval` as a folder in VS Code, then open
[human_approval.ipynb](human_approval.ipynb). Select the repository root's
`.venv/Scripts/python.exe` kernel. Use this numbered folder as the
notebook working directory. Restart the kernel after helper edits or switching lessons.

The standard folders are docs/dataset, docs/goldends, docs/evaluatedds,
docs/evalresults, models, prompts, and tools. Empty folders are reserved;
no artificial data, model, or prompt is needed to fill them.

| File | What it does |
| --- | --- |
| [docs/dataset/release.json](docs/dataset/release.json) | Release ID and author in the example. |
| [docs/dataset/reviewers.json](docs/dataset/reviewers.json) | Separate fictional authority records. |
| [docs/dataset/approvals.json](docs/dataset/approvals.json) | Clearly labelled sample decisions, including an unauthorized role claim. |
| [docs/dataset/learner_approval.json](docs/dataset/learner_approval.json) | Your unfilled approval template; never written by the notebook. |
| [tools/approvals.py](tools/approvals.py) | Authority, separate-reviewer, decision, and release checks. |

Only approved_fixture passes the baseline approval check. A pending decision stays pending and an authorized rejection stays rejected. After changing the sample's release ID, approved_fixture becomes blocked. Your own record stays pending.

Changes are in memory. This notebook writes no files.

All example inputs, reports, and sample decisions are fictional teaching
fixtures. No model calls or API keys are needed. The learner's own judgments,
approvals, and run remain pending.

The notebook is prepared for your run. See the
[repository README](../README.md) for shared setup and verification. Work through one cell at a time.
