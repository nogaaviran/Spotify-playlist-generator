import yaml
from pathlib import Path

PRESETS_PATH = Path(__file__).parent / "mapping" / "presets.yml"

def load_presets():
    with open(PRESETS_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
