# Project 7: Incident response

## 1. What can happen?

A privacy incident may require stopping an assistant until recovery requirements are met.

**Example** An incident is marked resolved, but the required retest has not been linked to its recovery record.

## 2. Our idea

We use fictional incidents, recovery evidence, and sample reviewer authority. A local Python responder records actual calls in a list. The status check runs before that responder. Sample approvals are fictional; your own recovery record stays pending.

### How we do it

1. Inspect the confirmed incident and the unconfirmed report.
2. Show that the missing retest keeps the responder suspended, even though the incident says resolved.
3. Link one existing synthetic retest and compare the same request. Inspect your pending recovery template.

## 3. How it helps

The blocked request makes zero responder calls. Linking the matching passed retest completes this fictional recovery case and permits one local call. A real recovery also needs trustworthy investigation, retests, and an authenticated decision.

## 4. Input and setup

Run these commands in PowerShell:

```powershell
# Run from the learning-governance repository root.
uv sync --locked
```

Open `7_incident_response` as a folder in VS Code, then open
[incident_response.ipynb](incident_response.ipynb). Select the repository root's
`.venv/Scripts/python.exe` kernel. Use this numbered folder as the
notebook working directory. Restart the kernel after helper edits or switching lessons.

The standard folders are docs/dataset, docs/goldends, docs/evaluatedds,
docs/evalresults, models, prompts, and tools. Empty folders are reserved;
no artificial data, model, or prompt is needed to fill them.

| File | What it does |
| --- | --- |
| [docs/dataset/incidents.json](docs/dataset/incidents.json) | Confirmed and unconfirmed fictional incidents. |
| [docs/dataset/release.json](docs/dataset/release.json) | Application and release identity. |
| [docs/dataset/policy.json](docs/dataset/policy.json) | Example suspension categories and response owner. |
| [docs/dataset/reviewers.json](docs/dataset/reviewers.json) | Separate fictional recovery authority. |
| [docs/dataset/evidence.json](docs/dataset/evidence.json) | Synthetic containment and retest records. |
| [docs/dataset/recoveries.json](docs/dataset/recoveries.json) | Fictional recovery missing one retest reference. |
| [docs/dataset/learner_recovery.json](docs/dataset/learner_recovery.json) | Unfilled learner recovery record. |
| [models/demo.py](models/demo.py) | Local responder and actual invocation log. |
| [tools/incidents.py](tools/incidents.py) | Recovery checks, application state, and enforced responder boundary. |

An unconfirmed-only case remains active under this example policy. The confirmed case is suspended until the retest is linked: actual local responder calls change from 0 to 1. Status resolved alone does not reopen the assistant. Every confirmed in-scope incident needs its own recovery.

Changes are in memory. This notebook writes no files.

All example inputs, reports, and sample decisions are fictional teaching
fixtures. No model calls or API keys are needed. The learner's own judgments,
approvals, and run remain pending.

The notebook is prepared for your run. See the
[repository README](../README.md) for shared setup and verification. Work through one cell at a time.
