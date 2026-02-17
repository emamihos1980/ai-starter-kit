from pathlib import Path

def test_repo_has_expected_folders():
    root = Path(__file__).resolve().parents[1]
    assert (root / "src").exists()
    assert (root / "sql").exists()
    assert (root / "data").exists()

def test_data_keep_files_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "data" / "raw" / ".keep").exists()
    assert (root / "data" / "processed" / ".keep").exists()
