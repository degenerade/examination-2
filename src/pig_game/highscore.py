"""highscore, this is a persistent high score manager"""

import json
import os
from typing import List, Tuple

HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscores.json")


class HighScore:
    """here we manage simple high score persistence"""

    def __init__(self, path: str = HIGHSCORE_FILE):
        self.path = path
        # ensure file exists
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as fh:
                json.dump([], fh)

    def _read(self) -> List[Tuple[str, int]]:
        try:
            with open(self.path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            #so, we expect list of [name, score] or objects; normalize
            entries = []
            for item in data:
                if isinstance(item, list) and len(item) == 2:
                    entries.append((str(item[0]), int(item[1])))
                elif isinstance(item, dict):
                    entries.append((str(item.get("name", "unknown")), int(item.get("score", 0))))
            return entries
        except Exception:
            return []

    def _write(self, entries: List[Tuple[str, int]]) -> None:
        out = [{"name": name, "score": score} for name, score in entries]
        with open(self.path, "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=2)

    def add(self, name: str, score: int) -> None:
        entries = self._read()
        entries.append((name, int(score)))
        #descending
        entries.sort(key=lambda x: x[1], reverse=True)
        #keep-top-50
        entries = entries[:50]
        self._write(entries)

    def top(self, n: int = 10):
        return self._read()[:n]
    