from datetime import datetime
from pathlib import Path

from papercuts.cli import append_papercut


def test_append_creates_document(tmp_path: Path) -> None:
    path = tmp_path / "PAPERCUTS.md"

    append_papercut(path, "a confusing setup step", datetime(2026, 7, 10, 12, 30))

    assert path.read_text() == (
        "# Papercuts\n\n"
        "- 2026-07-10T12:30:00 — a confusing setup step\n"
    )


def test_append_preserves_existing_content(tmp_path: Path) -> None:
    path = tmp_path / "PAPERCUTS.md"
    path.write_text("# Papercuts\n\n- existing\n")

    append_papercut(path, "a stale cache", datetime(2026, 7, 10, 12, 31))

    assert path.read_text().endswith(
        "- existing\n- 2026-07-10T12:31:00 — a stale cache\n"
    )
