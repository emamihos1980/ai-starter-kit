**Jump to:** [Repo conventions](#repo-conventions) | [How to run](#how-to-run) | [Skill roadmap](#skill-roadmap-what-to-learn-in-order) | [Operating rules](#operating-rules-so-we-dont-repeat-discussions)

# AI Engineer Skill Path (Reference)

## Goal
Become an AI Engineer by building strong fundamentals + a portfolio with production-style projects.

## Current status (snapshot)
- Program: APUS BS Data Science (Deep Learning concentration)
- Pace: 3 courses / 8 weeks (9 credits/session)
- Current courses: ARAB100, PSYC101, MATH210 (Discrete Math)
- Completed: ENGL110, COMM120, MATH225 (Calc I), MATH220 (Linear Algebra), STEM380, MATH112 (Pre-Calc)
- Certificates in progress (Coursera):
  - Google: Git and GitHub
  - UC Davis: SQL for Data Science
  - UMich: Programming for Everybody (Python)

## Portfolio strategy (4 core repos)
1) Business ML
   - regression/classification, metrics, feature engineering, model cards
2) Deep Learning
   - PyTorch, CNN/RNN/Transformers basics, training loops, experiment tracking
3) RAG
   - embeddings, vector DB, chunking, eval, hallucination controls, citations
4) Deployment
   - FastAPI, Docker, CI, tests, simple cloud deploy

## Current “starter” repo (this repo)
Repo: ai-starter-kit
Purpose: repeatable workflow for Python + SQL + Git

### Repo conventions
- data/raw and data/processed are NOT committed (use .keep)
- local sqlite DB is NOT committed
- scripts live in src/
- queries live in sql/
- notebooks are optional (notebooks/)

### How to run
- Create DB locally from CSVs:
  - `python src/load_contoso_sqlite.py`
- Database location:
  - `data/contoso.sqlite` (local only; ignored by git)
- If the DB already exists and is huge, delete it and regenerate from CSVs

## Skill roadmap (what to learn, in order)
### Phase 0 — Workflow (now)
- Git basics, branches, PRs, README/docs habit
- Python env + pip/requirements
- SQL: SELECT/JOIN/GROUP BY, window funcs

### Phase 1 — Core Python for data
- functions, classes, typing, pathlib
- pandas basics, EDA, input validation
- testing with pytest (unit tests for helpers)

### Phase 2 — ML Foundations
- sklearn pipelines, preprocessing, leakage avoidance
- evaluation: cross-val, ROC/AUC, PR, calibration
- explainability: feature importance / SHAP (basic)

### Phase 3 — Deep Learning
- PyTorch, datasets/dataloaders
- training loop + checkpoints
- GPU basics, mixed precision (optional)

### Phase 4 — LLM / RAG
- prompt basics, system vs user messages
- embeddings + retrieval + re-ranking
- RAG evaluation: groundedness, faithfulness, answer quality

### Phase 5 — Deploy + MLOps-lite
- FastAPI inference service
- Docker + compose
- CI: lint + tests
- logging + simple monitoring

## Operating rules (so we don’t repeat discussions)
When asking for help, always include:
1) What repo + file name
2) What command you ran
3) Full error text (copy/paste)
4) What you expected to happen
5) Your environment (Windows/Anaconda/venv)

## Next 2 concrete tasks
- [ ] Add a README section: “Local data & DB policy”
- [ ] Add 1 pytest test (example: path validation or CSV discovery)
