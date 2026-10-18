#!/usr/bin/env python3

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

GLYPHS = {
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "B": ("11110", "10001", "10001", "11110", "10001", "10001", "11110"),
    "C": ("01110", "10001", "10000", "10000", "10000", "10001", "01110"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "G": ("01110", "10001", "10000", "10111", "10001", "10001", "01111"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "I": ("11111", "00100", "00100", "00100", "00100", "00100", "11111"),
    "J": ("00111", "00010", "00010", "00010", "00010", "10010", "01100"),
    "K": ("10001", "10010", "10100", "11000", "10100", "10010", "10001"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "10101", "01010"),
    "X": ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    "Y": ("10001", "10001", "01010", "00100", "00100", "00100", "00100"),
    "Z": ("11111", "00001", "00010", "00100", "01000", "10000", "11111"),
    "0": ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    "1": ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    "2": ("01110", "10001", "00001", "00010", "00100", "01000", "11111"),
    "3": ("11110", "00001", "00001", "01110", "00001", "00001", "11110"),
    "4": ("00010", "00110", "01010", "10010", "11111", "00010", "00010"),
    "5": ("11111", "10000", "11110", "00001", "00001", "10001", "01110"),
    "6": ("00110", "01000", "10000", "11110", "10001", "10001", "01110"),
    "7": ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    "8": ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    "9": ("01110", "10001", "10001", "01111", "00001", "00010", "01100"),
    "-": ("00000", "00000", "00000", "11111", "00000", "00000", "00000"),
    ".": ("00000", "00000", "00000", "00000", "00000", "01100", "01100"),
    ":": ("00000", "01100", "01100", "00000", "01100", "01100", "00000"),
    "/": ("00001", "00010", "00010", "00100", "01000", "01000", "10000"),
    "!": ("00100", "00100", "00100", "00100", "00100", "00000", "00100"),
    "?": ("01110", "10001", "00001", "00110", "00100", "00000", "00100"),
    "&": ("01100", "10010", "10100", "01000", "10101", "10010", "01101"),
    "#": ("01010", "01010", "11111", "01010", "11111", "01010", "01010"),
    "*": ("00000", "10101", "01110", "11111", "01110", "10101", "00000"),
    "'": ("00100", "00100", "01000", "00000", "00000", "00000", "00000"),
    ",": ("00000", "00000", "00000", "00000", "01100", "00100", "01000"),
    "(": ("00010", "00100", "01000", "01000", "01000", "00100", "00010"),
    ")": ("01000", "00100", "00010", "00010", "00010", "00100", "01000"),
    "[": ("01110", "01000", "01000", "01000", "01000", "01000", "01110"),
    "]": ("01110", "00010", "00010", "00010", "00010", "00010", "01110"),
    "+": ("00000", "00100", "00100", "11111", "00100", "00100", "00000"),
    "=": ("00000", "00000", "11111", "00000", "11111", "00000", "00000"),
    ">": ("01000", "00100", "00010", "00001", "00010", "00100", "01000"),
    "<": ("00010", "00100", "01000", "10000", "01000", "00100", "00010"),
    "_": ("00000", "00000", "00000", "00000", "00000", "00000", "11111"),
    "@": ("01110", "10001", "10111", "10101", "10111", "10000", "01110"),
    "%": ("11001", "11010", "00010", "00100", "01000", "01011", "10011"),
}

PALETTES = {
    "light": {
        "bg": "#f5f3ff",
        "surface": "#ffffff",
        "surface2": "#f1efff",
        "ink": "#302c4d",
        "muted": "#7d7899",
        "line": "#ded9f4",
        "cyan": "#2bb9b1",
        "yellow": "#ffc857",
        "green": "#45c58a",
        "orange": "#ff9b62",
        "red": "#f06f78",
        "purple": "#7767e8",
        "pink": "#f58bb8",
        "shadow": "#c9c2e7",
    },
    "dark": {
        "bg": "#17172a",
        "surface": "#24233a",
        "surface2": "#2d2b48",
        "ink": "#f7f4ff",
        "muted": "#aaa4c7",
        "line": "#403d60",
        "cyan": "#5edbd3",
        "yellow": "#ffd66e",
        "green": "#67dca1",
        "orange": "#ffad73",
        "red": "#ff8992",
        "purple": "#9b8cff",
        "pink": "#ff9bc5",
        "shadow": "#0d0c1d",
    },
}

SPRITE_INK = "#3a3155"

STYLE = (
    "<style>"
    ".blink{animation:pxblink 1.3s steps(2, end) infinite}"
    ".twinkle{animation:pxtwinkle 2.4s steps(2, end) infinite}"
    ".twinkle2{animation:pxtwinkle 3.1s steps(2, end) infinite .7s}"
    "@keyframes pxblink{50%{opacity:.15}}"
    "@keyframes pxtwinkle{50%{opacity:.2}}"
    "</style>"
)


def rect(x, y, w, h, fill=None, rx=None, stroke=None, sw=None, op=None, cls=None):
    attrs = [f'x="{x}"', f'y="{y}"', f'width="{w}"', f'height="{h}"']
    if fill is not None:
        attrs.append(f'fill="{fill}"')
    if rx is not None:
        attrs.append(f'rx="{rx}"')
    if stroke is not None:
        attrs.append(f'stroke="{stroke}"')
    if sw is not None:
        attrs.append(f'stroke-width="{sw}"')
    if op is not None:
        attrs.append(f'opacity="{op}"')
    if cls is not None:
        attrs.append(f'class="{cls}"')
    return "<rect " + " ".join(attrs) + "/>"


def text_width(text, scale, spacing=1):
    return len(text) * (5 + spacing) * scale - spacing * scale


def pixel_text(text, x, y, scale, fill, spacing=1, op=None):
    out = []
    cx = x
    for ch in text.upper():
        if ch == " ":
            cx += (5 + spacing) * scale
            continue
        rows = GLYPHS.get(ch, GLYPHS["?"])
        for ri, row in enumerate(rows):
            i = 0
            while i < 5:
                if row[i] == "1":
                    j = i
                    while j < 5 and row[j] == "1":
                        j += 1
                    out.append(rect(cx + i * scale, y + ri * scale, (j - i) * scale, scale, fill=fill, op=op))
                    i = j
                else:
                    i += 1
        cx += (5 + spacing) * scale
    return "\n".join(out)


def banner(theme):
    p = PALETTES[theme]
    W, H = 1200, 300
    panel = rect(8, 8, 1160, 256, fill=p["surface"], rx=10, stroke=p["line"], sw=3)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        STYLE,
        "<defs>",
        f'<pattern id="pxgrid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M 24 0 L 0 0 0 24" fill="none" stroke="{p["purple"]}" stroke-opacity=".07" stroke-width="1.5"/></pattern>',
        f'<radialGradient id="glowPink"><stop offset="0" stop-color="{p["pink"]}" stop-opacity=".20"/><stop offset="1" stop-color="{p["pink"]}" stop-opacity="0"/></radialGradient>',
        f'<radialGradient id="glowCyan"><stop offset="0" stop-color="{p["cyan"]}" stop-opacity=".16"/><stop offset="1" stop-color="{p["cyan"]}" stop-opacity="0"/></radialGradient>',
        f'<clipPath id="panelClip">{panel}</clipPath>',
        "</defs>",
        rect(20, 20, 1160, 256, fill=p["shadow"], rx=10),
        panel,
        '<g clip-path="url(#panelClip)">',
        rect(8, 8, 1160, 256, fill="url(#pxgrid)"),
        '<circle cx="130" cy="40" r="130" fill="url(#glowPink)"/>',
        '<circle cx="1090" cy="30" r="120" fill="url(#glowCyan)"/>',
        '<g opacity=".4">',
        rect(1082, 26, 10, 10, fill=p["purple"]),
        rect(1098, 26, 10, 10, fill="none", stroke=p["purple"], sw=2.5),
        rect(1114, 26, 10, 10, fill=p["pink"]),
        "</g>",
        rect(64, 54, 124, 40, fill="none", rx=4, stroke=p["green"], sw=3),
        rect(82, 68, 12, 12, fill=p["green"], cls="blink"),
        pixel_text("ONLINE", 104, 67, 2, p["green"]),
        pixel_text("MERCURY", 64, 127, 9, p["cyan"]),
        pixel_text("MERCURY", 73, 118, 9, p["pink"]),
        pixel_text("MERCURY", 64, 118, 9, p["ink"]),
    ]
    tx = 64
    for run, color in (("VIBE CODER", p["ink"]), ("//", p["muted"]), ("STUDENT", p["muted"])):
        parts.append(pixel_text(run, tx, 200, 3, color))
        tx += text_width(run, 3) + 36
    hint = "PLAYER 1 - INSERT COIN"
    parts.append(pixel_text(hint, 64, 240, 2, p["muted"]))
    parts.append(rect(64 + text_width(hint, 2) + 12, 238, 10, 18, fill=p["purple"], cls="blink"))
    parts.append(f'<line x1="900" y1="48" x2="900" y2="228" stroke="{p["line"]}" stroke-width="2.5" stroke-dasharray="4 9"/>')
    parts.append(rect(988, 72, 132, 132, fill=p["shadow"], rx=8))
    parts.append(rect(980, 64, 132, 132, fill=p["yellow"], rx=8, stroke=SPRITE_INK, sw=5))
    parts.append(rect(1012, 104, 17, 20, fill=SPRITE_INK))
    parts.append(rect(1063, 104, 17, 20, fill=SPRITE_INK))
    parts.append(rect(1017, 162, 57, 11, fill=SPRITE_INK))
    cap = "MERCURY"
    cap_w = text_width(cap, 2)
    parts.append(pixel_text(cap, 980 + (132 - cap_w) // 2, 210, 2, p["purple"]))
    parts.append(pixel_text("PLAYER 1", 999, 232, 2, p["muted"]))
    parts.append('<g class="twinkle">' + rect(930, 68, 24, 8, fill=p["yellow"]) + rect(938, 60, 8, 24, fill=p["yellow"]) + "</g>")
    parts.append(rect(1146, 146, 8, 8, fill="none", stroke=p["cyan"], sw=2.5, cls="twinkle2"))
    parts.append(rect(952, 236, 8, 8, fill=p["pink"], cls="twinkle2"))
    parts.append("</g>")
    parts.append("</svg>")
    return "\n".join(parts)


def sprite(theme):
    p = PALETTES[theme]
    W = H = 176
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        rect(18, 18, 156, 156, fill=p["shadow"], rx=10),
        rect(6, 6, 156, 156, fill=p["yellow"], rx=10, stroke=SPRITE_INK, sw=5),
        rect(43, 53, 20, 24, fill=SPRITE_INK),
        rect(105, 53, 20, 24, fill=SPRITE_INK),
        rect(50, 122, 68, 13, fill=SPRITE_INK),
        "</svg>",
    ]
    return "\n".join(parts)


def title(text, index, theme):
    p = PALETTES[theme]
    W, H = 1200, 64
    chip_x = 40 + text_width(text, 4) + 18
    num = f"{index:02d}"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        "<defs>",
        f'<linearGradient id="barGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p["purple"]}"/><stop offset="1" stop-color="{p["pink"]}"/></linearGradient>',
        "</defs>",
        rect(15, 19, 10, 32, fill=p["shadow"]),
        rect(12, 16, 10, 32, fill="url(#barGrad)"),
        pixel_text(text, 43, 21, 4, p["shadow"]),
        pixel_text(text, 40, 18, 4, p["ink"]),
        rect(chip_x, 18, 48, 28, fill="none", rx=3, stroke=p["yellow"], sw=2.5),
        pixel_text(num, chip_x + (48 - text_width(num, 2)) // 2, 25, 2, p["yellow"]),
        f'<line x1="{chip_x + 66}" y1="32" x2="1096" y2="32" stroke="{p["line"]}" stroke-width="3" stroke-dasharray="2 7"/>',
        rect(1112, 26, 12, 12, fill=p["purple"]),
        rect(1131, 26, 12, 12, fill="none", stroke=p["purple"], sw=2.5),
        rect(1150, 26, 12, 12, fill=p["pink"]),
        "</svg>",
    ]
    return "\n".join(parts)


def divider(theme):
    p = PALETTES[theme]
    W, H = 1200, 40
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<line x1="12" y1="20" x2="544" y2="20" stroke="{p["line"]}" stroke-width="3" stroke-dasharray="2 7"/>',
        f'<line x1="656" y1="20" x2="1188" y2="20" stroke="{p["line"]}" stroke-width="3" stroke-dasharray="2 7"/>',
        rect(568, 14, 12, 12, fill=p["purple"]),
        rect(594, 14, 12, 12, fill="none", stroke=p["purple"], sw=3),
        rect(620, 14, 12, 12, fill=p["pink"]),
        "</svg>",
    ]
    return "\n".join(parts)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    titles = [("PLAYER CARD", 1), ("SKILL TREE", 2), ("SAVE DATA", 3), ("MULTIPLAYER", 4)]
    for theme in ("light", "dark"):
        (ASSETS / f"banner-{theme}.svg").write_text(banner(theme), encoding="utf-8")
        (ASSETS / f"sprite-{theme}.svg").write_text(sprite(theme), encoding="utf-8")
        (ASSETS / f"divider-{theme}.svg").write_text(divider(theme), encoding="utf-8")
        for label, idx in titles:
            slug = label.lower().replace(" ", "-")
            (ASSETS / f"title-{slug}-{theme}.svg").write_text(title(label, idx, theme), encoding="utf-8")
    for f in sorted(ASSETS.glob("*.svg")):
        print("written", f.name)


if __name__ == "__main__":
    main()
