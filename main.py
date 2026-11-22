"""Write the bundled picture of one ingredient to /output/entry.png.

The picture (food.png, shipped next to this file) is a close-up of a
single ripe strawberry, glossy with water droplets. This program copies
its exact bytes to the output path, so every run produces the same file.
It uses only the standard library and makes no network calls.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "food.png"
OUTPUT = Path("/output") / "entry.png"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    main()
