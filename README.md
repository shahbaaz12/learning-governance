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

These four notebooks read a few JSON records, run small Python checks, and show
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

Work through one project at a time. Each project README explains its inputs,
helper files, expected observations, and notebook order. All example records
are fictional; synthetic report counts are not measured model performance.

The four notebooks contain 24 code cells. Delivered outputs are empty, and
the notebooks write no files or human decisions. The review template in
Project 2 starts pending so you can record your own judgment separately.

Verification on 18 November 2026 executed all 24 code cells and 55 focused
checks from an isolated copy of the published files. Network access was
disabled. The checks passed without changing inputs, notebook outputs, or
learner review records.

The topic selection draws on the voluntary
[NIST AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).
These are small learning examples. Local records demonstrate the process;
they do not authenticate reviewers or establish organizational compliance.
