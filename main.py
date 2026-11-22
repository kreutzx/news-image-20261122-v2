# Entrypoint (Python 3.13, standard library only).
# The repository holds entry.png — the front page rendered by build.py from
# stories.py/art.py — and this program copies it to the output directory,
# validating the PNG magic and the 1 MiB cap on the way. Deterministic:
# the same bytes come out on every run.
import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def png_size(data):
    """(width, height) from the PNG IHDR chunk, or None if not a PNG."""
    if not data.startswith(PNG_MAGIC) or data[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", data[16:24])


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as fh:
        data = fh.read()
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        sys.exit("entry.png is not a PNG or JPEG")
    if len(data) > MAX_BYTES:
        sys.exit("entry.png exceeds the 1 MiB cap")
    size = png_size(data)
    if size and (size[0] > MAX_SIDE or size[1] > MAX_SIDE):
        sys.exit("entry.png exceeds the 1024x1024 cap")
    with open(dst, "wb") as fh:
        fh.write(data)
    print(f"wrote {dst} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
