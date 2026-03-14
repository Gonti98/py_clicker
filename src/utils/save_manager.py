import json
from pathlib import Path
from typing import Optional
import time

class SaveManager:
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    SAVE_GAME_FILE = PROJECT_ROOT / "data" / "save.json"
    VERSION = "0.1"

    @classmethod
    def save_game(cls, coins: int, grind: Grind):
        data = {
            "version": cls.VERSION,
            "coins": coins,
            "grind": grind.to_dict(),
        }
        cls.SAVE_GAME_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(cls.SAVE_GAME_FILE, "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def load_game(cls) -> Optional[int]:
        if not cls.SAVE_GAME_FILE.exists():
            return None
        try:
            with open(cls.SAVE_GAME_FILE, "r") as file:
                data = json.load(file)
            return int(data.get("coins", 0))
        except (json.JSONDecodeError, KeyError, ValueError):
            return None
