"""highscore, this is a persistent high score manager"""

import json
import os
from typing import Dict, List, Optional

HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscores.json")


class HighScore:
    """here we manage simple high score persistence"""

    def __init__(self, path: str = HIGHSCORE_FILE):
        self.path = path
        self.data = self._read()
        self._write()

    # ------------------------------------------------------------------
    # persistence helpers
    # ------------------------------------------------------------------
    def _read(self) -> Dict[str, List[Dict]]:
        """Read highscore data from the JSON file and normalize it.

        Returns a dict with a 'players' list even when file is missing or invalid.
        """
        if not os.path.exists(self.path):
            return {"players": []}
        try:
            with open(self.path, "r", encoding="utf-8") as fh:
                stored = json.load(fh)
        except (OSError, json.JSONDecodeError):
            return {"players": []}
        return self._normalize(stored)

    def _write(self) -> None:
        """Write current highscore data back to the JSON file.

        Creates directories as needed.
        """
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as fh:
            json.dump(self.data, fh, indent=2)


    # ------------------------------------------------------------------
    # public API
    # ------------------------------------------------------------------
    def register(self, name: str) -> None:
        """Ensure a player entry exists."""
        self._get_or_create(name)
        self._write()

    def add(self, name: str, score: int) -> None:
        """Backward compatible winner registration."""
        self.record_game(name, int(score), won=True)

    def record_game(self, name: str, score: int, won: bool = False) -> None:
        """Store result for a player."""
        entry = self._get_or_create(name)
        entry["display_name"] = name.strip() or entry["display_name"]
        entry["games_played"] += 1
        if won:
            entry["wins"] += 1
        score = max(0, int(score))
        entry["scores"].append(score)
        entry["scores"] = entry["scores"][-20:]
        entry["best_score"] = max(entry["best_score"], score)
        entry["total_score"] += score
        self._write()

    def rename(self, old_name: str, new_name: str) -> None:
        """Keep statistics when a player changes their name."""
        new_name = new_name.strip()
        if not new_name:
            return
        entry = self._find_by_alias(old_name) or self._get_or_create(old_name)
        self._add_alias(entry, old_name)
        entry["display_name"] = new_name
        self._add_alias(entry, new_name)
        self._write()

    def top(self, n: int = 10):
        """Return best players with statistics."""
        players = sorted(
            self.data["players"],
            key=lambda item: (
                item["best_score"],
                item["wins"],
                item["total_score"],
            ),
            reverse=True,
        )
        return players[:n]

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------
    def _normalize(self, stored) -> Dict[str, List[Dict]]:
        """Normalize legacy or current stored representations into a players list."""
        players = []
        if isinstance(stored, dict) and "players" in stored:
            for entry in stored["players"]:
                players.append(
                    self._build_entry(entry.get("display_name", "unknown"), entry)
                )
            return {"players": players}

        if isinstance(stored, list):
            for item in stored:
                if isinstance(item, list) and len(item) == 2:
                    name, score = item
                elif isinstance(item, dict):
                    name = item.get("name", "unknown")
                    score = item.get("score", 0)
                else:
                    continue
                players.append(
                    self._build_entry(
                        str(name),
                        {
                            "best_score": int(score),
                            "total_score": int(score),
                            "scores": [int(score)],
                            "games_played": 1,
                            "wins": 1,
                        },
                    )
                )
        return {"players": players}

    def _build_entry(self, name: str, base: Optional[Dict] = None) -> Dict:
        """Construct a consistent player entry dict from a base mapping."""
        name = name.strip() or "unknown"
        entry = {
            "display_name": name,
            "aliases": [],
            "games_played": int(base.get("games_played", 0)) if base else 0,
            "wins": int(base.get("wins", 0)) if base else 0,
            "scores": list(base.get("scores", [])) if base else [],
            "best_score": int(base.get("best_score", 0)) if base else 0,
            "total_score": int(base.get("total_score", 0)) if base else 0,
        }
        for alias in base.get("aliases", []) if base else []:
            self._add_alias(entry, alias)
        if not entry["scores"]:
            entry["scores"] = []
        self._add_alias(entry, name)
        return entry

    def _get_or_create(self, name: str) -> Dict:
        """Return existing player entry by name or create a new one."""
        entry = self._find_by_alias(name)
        if entry is None:
            entry = self._build_entry(name)
            self.data["players"].append(entry)
        return entry

    def _find_by_alias(self, name: str) -> Optional[Dict]:
        """Find a player entry by any known alias (normalized)."""
        norm = self._normalize_name(name)
        for entry in self.data["players"]:
            if norm in entry.get("aliases", []):
                return entry
        return None

    def _add_alias(self, entry: Dict, name: str) -> None:
        """Add a normalized alias to a player's alias list (de-duplicated)."""
        norm = self._normalize_name(name)
        aliases = entry.setdefault("aliases", [])
        if norm and norm not in aliases:
            aliases.append(norm)

    @staticmethod
    def _normalize_name(name: str) -> str:
        """Normalize a name for alias matching (strip and lowercase)."""
        return str(name).strip().lower()
