"""Assemble the array handbook and write the HTML next to this script."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from part_00_06 import chapters_00_06
from part_07_11 import chapters_07_11
from part_12_16 import chapters_12_16
from part_17_21 import chapters_17_21
from part_22_25 import chapters_22_25
from part_front import cover, how_to_study
from theme import CSS

OUT = ROOT / "array-2d-cheatsheet.html"


def main():
    parts = [
        cover(),
        how_to_study(),
        *chapters_00_06(),
        *chapters_07_11(),
        *chapters_12_16(),
        *chapters_17_21(),
        *chapters_22_25(),
    ]
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>From zero to the interview — arrays and matrices</title>
<style>
{CSS}
.cover {{ min-height: 0; }}
.cover h1 {{ margin: 8mm 0 6px; font-size: 30pt; }}
.deck {{ margin-bottom: 8px; }}
.meta {{ margin-bottom: 8px; }}
.rule {{ margin: 8px 0; }}
.path {{ gap: 0 16px; }}
.path li {{ padding: 3px 0 3px; }}
</style>
</head>
<body>
{''.join(parts)}
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
