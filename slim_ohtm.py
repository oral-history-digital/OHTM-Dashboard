"""
Strip fields the dashboard never reads from an .ohtm file.

Usage: python slim_ohtm.py ohd.ohtm ohd_slim.ohtm

Removes `cleaned` (a list of token strings per sentence, ~138 MiB) and
`model_base`. Neither is referenced anywhere in ohtm_dash_function.py or
functions/. On the production file this takes resident memory from 971 to
730 MiB and peak from 1191 to 923 MiB, before the string sharing in
ohtm_dash_server.py takes it further.

This is a stopgap for as long as the producer still emits those fields --
the real fix is to stop writing them in the first place.
"""

import json
import sys
from pathlib import Path

DROP_FROM_SENTENCE = ("cleaned",)
DROP_FROM_INTERVIEW = ("model_base",)


def slim(data):
    removed = 0
    for archive in data["corpus"].values():
        for interview in archive.values():
            for key in DROP_FROM_INTERVIEW:
                removed += interview.pop(key, None) is not None
            for sentence in interview["sent"].values():
                for key in DROP_FROM_SENTENCE:
                    removed += sentence.pop(key, None) is not None
    return removed


def main(src, dst):
    src, dst = Path(src), Path(dst)
    with open(src) as f:
        data = json.load(f)
    removed = slim(data)
    with open(dst, "w") as f:
        json.dump(data, f)
    before = src.stat().st_size / 1024 / 1024
    after = dst.stat().st_size / 1024 / 1024
    print(f"{src.name}  {before:.0f} MiB  ->  {dst.name}  {after:.0f} MiB"
          f"   ({removed:,} fields removed)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__.strip())
    main(sys.argv[1], sys.argv[2])
