"""Write the bundled picture of one ingredient to /output/entry.png.

The picture (food.png, shipped next to this file) is a close-up of a
single ripe strawberry, glossy with water droplets. This program copies
its exact bytes to the output path, so every run produces the same file.
After copying, it verifies the written file byte-for-byte against the
source by comparing SHA-256 digests, and fails loudly if they differ.
It uses only the standard library and makes no network calls.
"""

import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "food.png"
OUTPUT = Path("/output") / "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    source_digest = _sha256(SOURCE)
    output_digest = _sha256(OUTPUT)
    if output_digest != source_digest:
        raise SystemExit(
            f"entry.png verification failed: output sha256 {output_digest} "
            f"does not match source sha256 {source_digest}"
        )


if __name__ == "__main__":
    main()
