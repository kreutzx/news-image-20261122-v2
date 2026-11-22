# Renderer: builds entry.png (1024x1024) from stories.py + art.py.
# Deterministic: no clock, no randomness, no network. Run: python3 build.py
import os
from PIL import Image, ImageDraw, ImageFont

import art
import stories

W = H = 1024
PAPER = (247, 241, 227)
CARD_BG = (253, 250, 240)
INK = (20, 26, 44)
GREY = (96, 96, 100)
RED = (178, 32, 44)
GOLD = (160, 120, 30)
NAVY = (16, 32, 58)

FONT_DIR = "/usr/share/fonts/truetype/noto/"
SERIF_BLACK = FONT_DIR + "NotoSerif-Black.ttf"
SERIF_BOLD = FONT_DIR + "NotoSerif-Bold.ttf"
SANS = FONT_DIR + "NotoSans-Regular.ttf"
SANS_BOLD = FONT_DIR + "NotoSans-Bold.ttf"
SANS_SEMI = FONT_DIR + "NotoSans-SemiBold.ttf"

CERT_COLOURS = {
    "CONFIRMED": (40, 108, 62),
    "REPORTED": (36, 82, 148),
    "DEVELOPING": (172, 106, 18),
    "CLAIM": (178, 32, 44),
    "FORECAST": (108, 58, 148),
}
SECTION_COLOURS = {
    "world": (22, 58, 110),
    "money": (16, 102, 84),
    "science": (88, 52, 140),
    "society": (168, 84, 24),
    "sport": (150, 28, 44),
}

_cache = {}


def F(path, size):
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size)
    return _cache[key]


def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if d.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, text, font, fill, max_w, leading, max_lines=None):
    lines = wrap(d, text, font, max_w)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def cert_chip(d, x, y, cert):
    f = F(SANS_BOLD, 10)
    label = cert
    w = d.textlength(label, font=f) + 10
    d.rounded_rectangle([x, y, x + w, y + 15], 3, fill=CERT_COLOURS[cert])
    d.text((x + 5, y + 2), label, font=f, fill=(255, 255, 255))
    return x + w


def drawn_count():
    n = len(stories.HEROES)
    groups = [cards for _n, _k, cards in stories.SECTIONS] + [stories.SPORT]
    for cards in groups:
        for c in cards:
            if c[4] in art.DRAWN_ICONS:
                n += 1
    return n


def masthead(d, img):
    d.rectangle([0, 0, W, 4], fill=RED)
    f_small = F(SANS_BOLD, 12)
    line = "SUNDAY 22 NOVEMBER 2026  ·  ALL TIMES UTC  ·  ONE PAGE, THE WHOLE DAY"
    d.text(((W - d.textlength(line, font=f_small)) / 2, 10), line, font=f_small, fill=RED)
    f_title = F(SERIF_BLACK, 55)
    title = stories.PAPER
    d.text(((W - d.textlength(title, font=f_title)) / 2, 26), title, font=f_title, fill=INK)
    total = stories.story_count()
    regions = stories.region_counts()
    certs = stories.cert_counts()
    region_line = "  ·  ".join(f"{r.upper()} {n}" for r, n in
                                sorted(regions.items(), key=lambda kv: -kv[1]))
    acct = (f"{total} STORIES · {len(regions)} REGIONS · {drawn_count()} DRAWN · "
            f"EVERY STORY SOURCED · CERTAINTY: " +
            " ".join(f"{k} {v}" for k, v in sorted(certs.items())))
    f_acct = F(SANS_BOLD, 12)
    d.text(((W - d.textlength(acct, font=f_acct)) / 2, 88), acct, font=f_acct, fill=NAVY)
    f_reg = F(SANS, 11)
    d.text(((W - d.textlength(region_line, font=f_reg)) / 2, 104), region_line, font=f_reg, fill=GREY)
    d.line([16, 122, W - 16, 122], fill=INK, width=2)


def timeline(d):
    y0, y1 = 126, 158
    d.rectangle([16, y0, W - 16, y1], fill=NAVY)
    f_t = F(SANS_BOLD, 11)
    f_b = F(SANS_BOLD, 11)
    f_l = F(SANS, 10)
    d.text((24, y0 + 10), "THE DAY IN UTC", font=f_t, fill=(240, 200, 90))
    items = stories.TIMELINE
    half = (len(items) + 1) // 2
    col_w = (W - 150) // half
    for row in range(2):
        for i, (hhmm, label) in enumerate(items[row * half:(row + 1) * half]):
            x = 140 + i * col_w
            y = y0 + 4 + row * 15
            d.text((x, y), hhmm, font=f_b, fill=(240, 200, 90))
            max_w = col_w - 44
            while label and d.textlength(label, font=f_l) > max_w:
                label = label[:-1]
            d.text((x + 40, y), label, font=f_l, fill=(235, 235, 230))


def hero(d, img, x, hero):
    w = 492
    d.rectangle([x, 162, x + w, 412], fill=CARD_BG, outline=INK, width=1)
    d.rectangle([x, 162, x + w, 166], fill=RED)
    art_box = [x + 8, 170, x + w - 8, 282]
    if hero["art"] == "cop31":
        art.hero_cop31(img, art_box)
    else:
        art.hero_ukraine(img, art_box)
    d = ImageDraw.Draw(img)
    d.text((x + 12, 288), hero["kicker"], font=F(SANS_BOLD, 12), fill=RED)
    # source + certainty chip on the kicker row, right-aligned
    f_src = F(SANS, 11)
    src_w = d.textlength(hero["source"], font=f_src)
    cert_w = d.textlength(hero["cert"], font=F(SANS_BOLD, 10)) + 10
    cert_chip(d, x + w - 12 - cert_w, 287, hero["cert"])
    d.text((x + w - 20 - cert_w - src_w, 289), hero["source"], font=f_src, fill=GREY)
    y = text_block(d, x + 12, 306, hero["headline"], F(SERIF_BOLD, 23), INK, w - 24, 27, max_lines=2)
    text_block(d, x + 12, y + 3, hero["deck"], F(SANS, 11), (40, 40, 48), w - 24, 14, max_lines=3)


def numbers_band(d):
    y0, y1 = 418, 450
    d.rectangle([16, y0, W - 16, y1], fill=INK)
    items = stories.NUMBERS
    col_w = (W - 32) // len(items)
    for i, (value, label) in enumerate(items):
        x = 16 + i * col_w + 8
        d.text((x, y0 + 3), value, font=F(SERIF_BOLD, 18), fill=(240, 200, 90))
        d.text((x, y0 + 24), label.upper()[:20], font=F(SANS_BOLD, 8), fill=(225, 225, 220))


def card(d, img, x, y, w, story):
    headline, source, cert, _region, icon_name = story
    art.icon(img, [x, y + 2, x + 30, y + 32], icon_name)
    d = ImageDraw.Draw(img)
    tx = x + 38
    y_end = text_block(d, tx, y, headline, F(SANS_SEMI, 12), INK, w - 40, 14, max_lines=2)
    sx = tx
    f_src = F(SANS, 9)
    d.text((sx, y + 26), source.upper(), font=f_src, fill=GREY)
    sx += d.textlength(source.upper(), font=f_src) + 6
    f_c = F(SANS_BOLD, 9)
    d.text((sx, y + 26), cert, font=f_c, fill=CERT_COLOURS[cert])
    return y_end


def section_header(d, x, y, w, name, key, count):
    d.rectangle([x, y, x + w, y + 20], fill=SECTION_COLOURS[key])
    d.text((x + 8, y + 4), name, font=F(SANS_BOLD, 12), fill=(255, 255, 255))
    label = f"{count} STORIES"
    d.text((x + w - 8 - d.textlength(label, font=F(SANS_BOLD, 10)), y + 5),
           label, font=F(SANS_BOLD, 10), fill=(255, 255, 255))
    return y + 24


def column(d, img, x, w, blocks, card_h=40):
    y = 456
    for name, key, cards in blocks:
        y = section_header(d, x, y, w, name, key, len(cards))
        for story in cards:
            card(d, img, x, y, w, story)
            y += card_h
        y += 6
    return y


def wire(d):
    y0 = 900
    d.rectangle([16, y0, W - 16, 1016], fill=(250, 244, 228), outline=RED, width=2)
    d.rectangle([16, y0, W - 16, y0 + 20], fill=RED)
    d.text((24, y0 + 4), "LATE WIRE — LATEST REPORTS BEFORE THIS PAGE CLOSED",
           font=F(SANS_BOLD, 12), fill=(255, 255, 255))
    note = "DRAWN AND SET IN CODE · NO PHOTOGRAPHS"
    d.text((W - 24 - d.textlength(note, font=F(SANS_BOLD, 9)), y0 + 6),
           note, font=F(SANS_BOLD, 9), fill=(255, 220, 220))
    y = y0 + 27
    for headline, source, cert, _region in stories.WIRE:
        d.text((24, y), "» " + headline, font=F(SANS_SEMI, 12), fill=INK)
        tail = f"  — {source} · {cert}"
        hx = 24 + d.textlength("» " + headline, font=F(SANS_SEMI, 12))
        d.text((hx, y + 1), tail, font=F(SANS, 10), fill=GREY)
        y += 18


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d, img)
    timeline(d)
    hero(d, img, 16, stories.HEROES[0])
    hero(d, img, 516, stories.HEROES[1])
    d = ImageDraw.Draw(img)
    numbers_band(d)
    secs = {name: (name, key, cards) for name, key, cards in stories.SECTIONS}
    column(d, img, 16, 328, [secs["WORLD"]], card_h=40)
    column(d, img, 352, 328, [secs["MONEY & TECH"], secs["SCIENCE & PLANET"]], card_h=40)
    column(d, img, 688, 320, [secs["SOCIETY & CULTURE"], ("SPORT", "sport", stories.SPORT)], card_h=38)
    wire(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, optimize=True)
    img.resize((300, 300)).save(os.path.join(os.path.dirname(out), "preview300.png"))
    print("stories:", stories.story_count(), "drawn:", drawn_count(),
          "bytes:", os.path.getsize(out))


if __name__ == "__main__":
    main()
