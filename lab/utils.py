from pathlib import Path


def load_all_wordlists_from_dir(directory: Path) -> list[str]:
    words: list[str] = []
    seen: set[str] = set()

    if not directory.exists():
        return words

    for file_path in sorted(directory.glob("*.txt")):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                lowered = word.lower()
                if lowered not in seen:
                    seen.add(lowered)
                    words.append(word)

    return words

import json
from pathlib import Path
from typing import Iterable, Any


def ensure_directories(paths: Iterable[Path]) -> None:
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_wordlist(path: Path) -> list[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]
