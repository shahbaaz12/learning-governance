# Project 1: System inventory

## 1. What can happen?

An organization has several AI helpers, but one has no named owner and another
is due for review. It is hard to know who should check them next.

**Example** The leave request helper has a purpose and a next review date,
but its owner field is blank.

## 2. Our idea

We start with three made-up HR application records saved in a JSON file. This
list is an **inventory**. Each record has an ID, name, purpose, owner, and next
review date. This lesson runs locally and makes no model calls.

We write a Python check that finds missing information and reviews that are
due. Then we fill one blank owner field in a copy of the records and compare.

### How we do it

1. Load the three saved records and choose the fixed sample date `2026-11-15`.
2. Check required fields. A missing or blank field produces `incomplete`.
3. For a record with all fields, check its next review date. A review on or
   before the sample date produces `review_due`; a future review gives `complete`.
4. Fill the second record's blank owner in memory. Run the same check and compare.

## 3. How it helps

We can see which record needs an owner and which needs a review. Filling one
owner field improves that record without hiding the other application's due review.

The check verifies that text is present, not whether it is true. Typing an
owner's name does not show that they accepted responsibility. `complete` means
the record passes this small documentation check; it does not approve deployment.

## 4. Input and setup

The [sample inventory](docs/dataset/systems.json) contains three fictional
applications. IDs are unique and dates use `YYYY-MM-DD`. No real ownership,
approval, or organizational policy is asserted by these examples.

From PowerShell, run:

```powershell
# Run from the learning-governance repository root.
uv sync --locked
```

Open `1_system_inventory` as a folder in VS Code. Open the
[notebook](system_inventory.ipynb) and select the repository root's
`.venv/Scripts/python.exe` as its kernel. The notebook uses this numbered
folder as its working directory. Restart the kernel after helper edits.

| File | What it does |
| --- | --- |
| [docs/dataset/systems.json](docs/dataset/systems.json) | Three fictional application records: complete, missing an owner, and review due today. |
| [tools/inventory.py](tools/inventory.py) | Checks required fields and review dates, then prints decisions with reasons. |
| [system_inventory.ipynb](system_inventory.ipynb) | Loads the records, runs the baseline, fills one owner, and compares the results. |

The retained folder structure is:

```text
1_system_inventory/
├── docs/
│   ├── dataset/
│   │   └── systems.json
│   ├── goldends/
│   ├── evaluatedds/
│   └── evalresults/
├── models/
├── prompts/
├── tools/
│   └── inventory.py
├── readme.md
└── system_inventory.ipynb
```

The unused folders are reserved for future needs. There are no reference
judgments, model outputs, prompts, or reports to create for this lesson.

Run one code cell at a time. Expect these observations:

| Record | Baseline | After filling one owner |
| --- | --- | --- |
| HR-001 | `complete` | `complete` |
| HR-002 | `incomplete` | `complete` |
| HR-003 | `review_due` | `review_due` |

The sample date is fixed so results stay reproducible. A review scheduled for
that day is already due. The candidate changes only a fictional owner in memory;
the input JSON and original baseline remain unchanged. No results are saved.

All six code cells passed local execution on 15 November 2026. The delivered
notebook has empty outputs and is ready for your run. Explain why the due review
remains and what `complete` cannot prove before choosing to start Project 2.
