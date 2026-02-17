from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CSV_DIR = ROOT / "data" / "raw" / "contoso"
DB_PATH = ROOT / "data" / "contoso.sqlite"

def main():
    if not CSV_DIR.exists():
        raise FileNotFoundError(f"Put Contoso CSVs in: {CSV_DIR}")

    csv_files = sorted(CSV_DIR.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in: {CSV_DIR}")

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")

    for f in csv_files:
        table = f.stem  # table name = filename (without .csv)
        df = pd.read_csv(f, low_memory=False)
        df.to_sql(table, conn, if_exists="replace", index=False, chunksize=2000)
        print(f"Loaded {table}: {df.shape}")

    conn.close()
    print(f"\nSQLite DB created at: {DB_PATH}")

if __name__ == "__main__":
    main()
