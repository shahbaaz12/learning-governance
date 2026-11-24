# Project 6: Change control

## 1. What can happen?

A prompt can change after the application was evaluated and approved.

**Example** Someone adds a sentence to the prompt but tries to reuse the old approval.

## 2. Our idea

We make a release manifest: a record of code, model configuration, prompt, dataset, and policy identities. SHA-256 gives each file a content fingerprint. Fixed fictional evaluation and approval records refer to the bundled baseline manifest. The notebook never regenerates those records.

### How we do it

1. Recalculate the baseline manifest from the actual files.
2. Check its binding to the saved fictional records.
3. Select the candidate prompt file, recalculate, and show why the old records no longer match.

## 3. How it helps

The prompt is the only changed artifact. Both previous records stop matching. Hashes detect content changes; they do not prove report quality or authenticate a reviewer. This lesson checks binding only, not full release eligibility.

## 4. Input and setup

Run these commands in PowerShell:

```powershell
# Run from the learning-governance repository root.
uv sync --locked
```

Open `6_change_control` as a folder in VS Code, then open
[change_control.ipynb](change_control.ipynb). Select the repository root's
`.venv/Scripts/python.exe` kernel. Use this numbered folder as the
notebook working directory. Restart the kernel after helper edits or switching lessons.

The standard folders are docs/dataset, docs/goldends, docs/evaluatedds,
docs/evalresults, models, prompts, and tools. Empty folders are reserved;
no artificial data, model, or prompt is needed to fill them.

| File | What it does |
| --- | --- |
| [docs/dataset/release.json](docs/dataset/release.json) | The five local artifact paths. |
| [docs/dataset/baseline_manifest.json](docs/dataset/baseline_manifest.json) | Saved baseline artifact identities. |
| [docs/dataset/release_records.json](docs/dataset/release_records.json) | Fixed synthetic evaluation and fictional approval bindings. |
| [models/demo.py](models/demo.py) | Local responder source whose bytes are fingerprinted. |
| [models/model.json](models/model.json) | Local demo model identity; no provider. |
| [prompts/answer.txt](prompts/answer.txt) | Baseline prompt. |
| [prompts/candidate_answer.txt](prompts/candidate_answer.txt) | Candidate with one additional instruction. |
| [docs/dataset/questions.json](docs/dataset/questions.json) | Fictional evaluation input. |
| [docs/dataset/policy.json](docs/dataset/policy.json) | Fictional policy artifact. |
| [tools/manifest.py](tools/manifest.py) | Builds the manifest and checks saved record bindings. |

The baseline gives bindings_match. The candidate gives needs_evaluation_and_review. Only the prompt artifact differs, and the stored baseline manifest and fictional records remain unchanged.

Changes are in memory. This notebook writes no files.

All example inputs, reports, and sample decisions are fictional teaching
fixtures. No model calls or API keys are needed. The learner's own judgments,
approvals, and run remain pending.

The notebook is prepared for your run. See the
[repository README](../README.md) for shared setup and verification. Work through one cell at a time.
