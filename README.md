# Learning governance

## 1. What can happen?

An AI assistant can have no named owner, use documents for the wrong purpose,
or change after someone has approved it. A good answer alone does not tell us
who is responsible for the application or whether it is ready to be released.

**Example** The current HR assistant is `hr-v1`, but its evaluation report
belongs to `hr-v0`. That report cannot establish how the current version behaves.

## 2. Our idea

We build small examples of **AI governance**: deciding who is responsible, what
the application may do, what evidence is needed, and how people handle changes
and incidents. We use fictional HR application records throughout the lessons.

These eight notebooks read a few JSON records, run small Python checks, and show
decisions with reasons. All lessons run locally and need no model calls or API
keys. Human judgments remain separate from technical checks.

### How we do it

1. Look at a normal record, a problematic record, and an edge case.
2. Run one check and explain its decision.
3. Change one relevant field or setting and compare the same examples.
4. Explain what the check establishes and what a person still needs to review.

## 3. How it helps

We connect policies and responsible people to visible evidence and decisions.
The examples show why complete records and passing technical checks still need
human review.

Start with a small inventory: a list of applications, their purposes, their
owners, and their next review dates. A complete record makes the application
easier to review; it does not authorize deployment.

## 4. Input and setup

Use Python 3.12, uv, and VS Code with its Python and Jupyter extensions.
To get the repository, run in PowerShell:

```powershell
git clone https://github.com/shahbaaz12/learning-governance.git
cd learning-governance
uv sync --locked
```

Open `1_system_inventory` as a folder in VS Code, then open its
[notebook](1_system_inventory/system_inventory.ipynb). Select this repository
root's `.venv/Scripts/python.exe` as the kernel. Run one code cell at a time.
Restart the kernel after changing helpers or switching lessons.

If you already have the repository, run `uv sync --locked` from its root.
All numbered projects share that environment. Do not run `uv init` inside them.
The lessons use Python's standard library; `ipykernel` runs them in VS Code.

### Projects

| Project | What you will try | Preparation |
| --- | --- | --- |
| [1. System inventory](1_system_inventory/readme.md) | Find a missing owner and a review that is due. Fill one fictional owner field and compare. | Prepared; learner run pending |
| [2. Risk register](2_risk_register/readme.md) | Record possible harm, affected people, controls, and who must review unresolved risks. | Prepared; learner run pending |
| [3. Data use policy](3_data_use_policy/readme.md) | Check permitted purposes, document access, and expiry dates. | Prepared; learner run pending |
| [4. Release evidence](4_release_evidence/readme.md) | Check that required evaluation evidence passes and belongs to this release. | Prepared; learner run pending |
| [5. Human approval](5_human_approval/readme.md) | Check reviewer authority and approval for a specific release. | Prepared; learner run pending |
| [6. Change control](6_change_control/readme.md) | Change a prompt and see why previous evidence and approval no longer match. | Prepared; learner run pending |
| [7. Incident response](7_incident_response/readme.md) | Suspend a local assistant and inspect the evidence required for recovery. | Prepared; learner run pending |
| [8. Governed HR assistant](8_governed_hr_assistant/readme.md) | Combine checks before responding and save a decision report. | Prepared; learner run pending |

Work through one project at a time. Each project README explains its inputs,
helper files, expected observations, and notebook order. All example records
are fictional; synthetic report counts are not measured model performance.

The eight notebooks contain 50 code cells. Delivered outputs are empty.
Projects 1-7 write no files. Project 8's final cell writes separate baseline
and candidate JSON/Markdown reports in its `docs/evalresults/` folder,
preserving previous reports. Learner review and approval templates start pending;
the notebooks never fill in human decisions on your behalf.

The repository fixes text line endings to LF so the file fingerprints in
Projects 6 and 8 reproduce across platforms. Those projects contain fixed,
explicitly fictional evaluation and approval bindings. Running a notebook does
not refresh them automatically to approve changed artifacts.

Verification on 24 November 2026 executed all 50 code cells and 46 focused
approval, change-control, recovery, and enforcement checks from an isolated
staged checkout. Network access was disabled. Inputs, notebook outputs, and
learner records stayed unchanged. Project 8's report writing was checked in
temporary storage outside the published tree.

The topic selection draws on the voluntary
[NIST AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).
These are small learning examples. Local records demonstrate the process;
they do not authenticate reviewers or establish organizational compliance.
