---
title: Api Migration Env
emoji: 🚀
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
app_port: 8000
---

# Legacy API Migration Environment

This environment simulates a real-world software engineering task: migrating legacy data structures into modern, type-safe JSON formats.

## Action & Observation Space
- **Action**: A `MigrationAction` containing a dictionary of transformed data.
- **Observation**: A `MigrationObservation` providing the source data, the target schema, and feedback from the grader.

## Tasks
1. **Easy**: Field renaming (e.g., snake_case to camelCase).
2. **Medium**: Type casting and data formatting (Strings to Floats/Lists).
3. **Hard**: Complex conditional logic and data joining.

## Setup & Usage
1. `uv venv && source .venv/bin/activate`
2. `uv pip install -e .`
3. `export HF_TOKEN="your_token"`
4. `python client.py`

## Baseline Scores
- **Easy**: 1.00
- **Medium**: 1.00
- **Hard**: 1.00
*(Measured using Qwen 2.5 72B Instruct)*