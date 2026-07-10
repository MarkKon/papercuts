from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


def repository_root(start: Path) -> Path:
    """Return the nearest Git root, or ``start`` when outside a repository."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return start
    return Path(result.stdout.strip())


def append_papercut(path: Path, message: str, now: datetime | None = None) -> None:
    """Append one timestamped entry, creating the small document if needed."""
    timestamp = (now or datetime.now().astimezone()).isoformat(timespec="seconds")
    if path.exists() and path.stat().st_size:
        prefix = "" if path.read_bytes().endswith(b"\n") else "\n"
    else:
        prefix = "# Papercuts\n\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"{prefix}- {timestamp} — {message}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="papercut",
        description="Append a small workflow papercut to PAPERCUTS.md.",
    )
    parser.add_argument("message", help="one concise description of the friction")
    parser.add_argument(
        "--file",
        type=Path,
        help="override the output path (default: PAPERCUTS.md at the Git root)",
    )
    args = parser.parse_args()

    output = args.file or repository_root(Path.cwd()) / "PAPERCUTS.md"
    append_papercut(output, args.message)
    print(output)
