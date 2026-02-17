

# ai-starter-kit

A starter repo for Python + SQL + Git workflows (local-first), used as a foundation for my AI Engineer path.

## Reference (start here)
- **AI Engineer Skill Path (Reference):** [AI_ENGINEER_PATH.md](docs/AI_ENGINEER_PATH.md)

## Repo layout
- `src/` Python scripts
- `sql/` SQL queries
- `data/raw/` local raw data (not committed)
- `data/processed/` local outputs (not committed)
- `data/contoso.sqlite` local database (not committed)

## Local data & DB policy
This repo does **not** commit datasets or local databases.
- Keep datasets in `data/raw/` and outputs in `data/processed/`
- Use `.keep` files so the folders exist in GitHub
- SQLite DB is generated locally and ignored by git

## Quick start
```bash
pip install -r requirements.txt
python src/load_contoso_sqlite.py
