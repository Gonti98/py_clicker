import json
from pathlib import Path
import tempfile

class TempSave:
    SAVE_FILE = Path(tempfile.gettempdir()) / "temp_save.json"

    @classmethod
    def save(cls, points: int) -> None:
        with open(cls.SAVE_FILE, "w") as f:
            json.dump({"points": points}, f)

    @classmethod
    def load(cls) -> int:
        if cls.SAVE_FILE.exists():
            try:
                with open(cls.SAVE_FILE, "r") as f:
                    return int(json.load(f)["points"])
            except:
                return 0
        return 0
