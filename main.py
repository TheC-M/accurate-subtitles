# Accurate Subtitles
# By TheC-M

# /src is used for my Python modules

from src.utilities import file_picker
from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve()
INPUT_DIR = ROOT_DIR / "data/input"
OUTPUT_DIR = ROOT_DIR / "data/output"

file_paths = file_picker("audio/video", INPUT_DIR)
print(file_paths)


