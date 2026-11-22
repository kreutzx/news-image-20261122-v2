# Flat vector-style illustrations drawn in code with PIL (no photos, no stock).
# Two hero scenes plus small spot icons for the section cards.
from PIL import Image, ImageDraw


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vgrad(img, box, top, bottom):
    """Vertical gradient fill inside box (drawn as 1px lines, few steps)."""
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    steps = max(2, (y1 - y0) // 6)
    for i in range(steps):
        t0, t1 = i / steps, (i + 1) / steps
        d.rectangle([x0, y0 + (y1 - y0) * t0, x1, y0 + (y1 - y0) * t1 + 1],
                    fill=_lerp(top, bottom, (t0 + t1) / 2))
    return d


def hero_cop31(img, box):
    """Antalya climate talks: globe, rising thermometer, delegate silhouettes."""
    x0, y0, x1, y1 = box
    d = vgrad(img, box, (16, 42, 74), (38, 92, 128))
    w, h = x1 - x0, y1 - y0
    # sun / heat disc
    d.ellipse([x0 + w * 0.70, y0 + h * 0.08, x0 + w * 0.86, y0 + h * 0.40], fill=(240, 178, 60))
    # globe
    cx, cy, r = x0 + w * 0.30, y0 + h * 0.46, int(h * 0.34)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(64, 145, 108), outline=(220, 235, 220), width=3)
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 200, 320, fill=(38, 110, 80))
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 20, 110, fill=(46, 124, 88))
    d.arc([cx - r, cy - int(r * 0.45), cx + r, cy + int(r * 0.45)], 0, 360, fill=(220, 235, 220), width=2)
    # thermometer
    tx = x0 + w * 0.60
    d.rounded_rectangle([tx, y0 + h * 0.16, tx + 14, y0 + h * 0.66], 7, fill=(235, 230, 215))
    d.rounded_rectangle([tx + 3, y0 + h * 0.30, tx + 11, y0 + h * 0.66], 4, fill=(198, 44, 44))
    d.ellipse([tx - 6, y0 + h * 0.60, tx + 20, y0 + h * 0.86], fill=(198, 44, 44))
    # conference table + delegates
    ty = y0 + h * 0.80
    d.rectangle([x0 + w * 0.06, ty, x1 - w * 0.06, ty + 8], fill=(24, 30, 44))
    for i in range(6):
        px = x0 + w * (0.12 + i * 0.13)
        d.ellipse([px, ty - 20, px + 13, ty - 7], fill=(12, 16, 26))
        d.rectangle([px + 1, ty - 8, px + 12, ty + 1], fill=(12, 16, 26))
    d.rectangle([x0, y1 - 3, x1, y1], fill=(10, 14, 24))
    return d


def hero_ukraine(img, box):
    """Night barrage over a city: skyline, drones, missile trails, searchlights."""
    x0, y0, x1, y1 = box
    d = vgrad(img, box, (8, 10, 26), (30, 24, 44))
    w, h = x1 - x0, y1 - y0
    # moon
    d.ellipse([x0 + w * 0.84, y0 + h * 0.07, x0 + w * 0.92, y0 + h * 0.24], fill=(226, 222, 200))
    d.ellipse([x0 + w * 0.865, y0 + h * 0.06, x0 + w * 0.925, y0 + h * 0.22], fill=(14, 16, 34))
    # searchlight beams
    for bx in (0.16, 0.55):
        d.polygon([(x0 + w * bx, y1 - h * 0.24), (x0 + w * (bx + 0.16), y0 + h * 0.06),
                   (x0 + w * (bx + 0.24), y0 + h * 0.10)], fill=(70, 74, 96))
    # drones (simple X silhouettes)
    for (dx, dy, s) in [(0.24, 0.20, 13), (0.42, 0.13, 10), (0.63, 0.24, 15), (0.74, 0.15, 9)]:
        cx, cy = x0 + w * dx, y0 + h * dy
        d.line([cx - s, cy - s, cx + s, cy + s], fill=(200, 60, 50), width=3)
        d.line([cx - s, cy + s, cx + s, cy - s], fill=(200, 60, 50), width=3)
        d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(230, 90, 70))
    # missile trails
    for (sx, sy, ex, ey) in [(0.05, 0.05, 0.30, 0.45), (0.95, 0.30, 0.70, 0.62)]:
        d.line([x0 + w * sx, y0 + h * sy, x0 + w * ex, y0 + h * ey], fill=(240, 170, 80), width=3)
        d.ellipse([x0 + w * ex - 4, y0 + h * ey - 4, x0 + w * ex + 4, y0 + h * ey + 4], fill=(250, 200, 110))
    # skyline
    base = y1 - int(h * 0.22)
    xs = x0 + 6
    heights = [0.30, 0.42, 0.26, 0.50, 0.34, 0.44, 0.28, 0.38, 0.31, 0.46]
    i = 0
    while xs < x1 - 30:
        bw = 26 + (i * 7) % 14
        bh = int(h * heights[i % len(heights)])
        d.rectangle([xs, base - bh, xs + bw, y1], fill=(10, 12, 22))
        for wy in range(base - bh + 6, y1 - 8, 11):
            for wx in range(xs + 4, xs + bw - 4, 9):
                if (wx * 7 + wy * 13) % 5 == 0:
                    d.rectangle([wx, wy, wx + 3, wy + 4], fill=(240, 196, 92))
        xs += bw + 5
        i += 1
    # ground fires
    for fx in (0.30, 0.68):
        gx, gy = x0 + w * fx, y1 - 4
        d.polygon([(gx - 10, gy), (gx, gy - 18), (gx + 10, gy)], fill=(232, 110, 44))
        d.polygon([(gx - 5, gy), (gx, gy - 10), (gx + 5, gy)], fill=(246, 178, 60))
    return d


# --- spot icons: drawn in a 36x36 box, single ink colour + one accent -------

def _icon_base(img, box, bg):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(box, 6, fill=bg)
    return d


def icon(img, box, name, ink=(20, 26, 44), accent=(178, 32, 44)):
    x0, y0, x1, y1 = box
    w = x1 - x0
    u = w / 36.0  # unit
    d = _icon_base(img, box, (238, 231, 208))

    def P(px, py):
        return (x0 + px * u, y0 + py * u)

    if name == "shield":
        d.polygon([P(18, 5), P(29, 9), P(29, 19), P(18, 31), P(7, 19), P(7, 9)], outline=ink, width=2)
        d.line([P(12, 18), P(16, 22), P(25, 12)], fill=accent, width=3)
    elif name == "radar":
        d.arc([x0 + 8 * u, y0 + 6 * u, x0 + 28 * u, y0 + 26 * u], 270, 360, fill=ink, width=2)
        d.arc([x0 + 13 * u, y0 + 11 * u, x0 + 28 * u, y0 + 26 * u], 270, 360, fill=ink, width=2)
        d.line([P(10, 28), P(24, 14)], fill=accent, width=3)
        d.ellipse([x0 + 8 * u, y0 + 26 * u, x0 + 12 * u, y0 + 30 * u], fill=ink)
    elif name == "missile":
        d.polygon([P(24, 6), P(29, 11), P(16, 24), P(11, 19)], fill=ink)
        d.polygon([P(11, 19), P(7, 27), P(13, 25)], fill=accent)
        d.polygon([P(16, 24), P(24, 27), P(19, 29)], fill=accent)
    elif name == "tanker":
        d.polygon([P(5, 22), P(31, 22), P(28, 29), P(9, 29)], fill=ink)
        d.rectangle([x0 + 13 * u, y0 + 15 * u, x0 + 24 * u, y0 + 22 * u], fill=accent)
        d.line([P(4, 32), P(12, 30), P(20, 32), P(28, 30), P(32, 32)], fill=(52, 110, 160), width=2)
    elif name == "jet":
        d.polygon([P(5, 24), P(20, 10), P(31, 8), P(24, 18), P(28, 26), P(20, 22), P(12, 28)], fill=ink)
        d.ellipse([x0 + 22 * u, y0 + 11 * u, x0 + 26 * u, y0 + 15 * u], fill=accent)
    elif name == "ship":
        d.polygon([P(4, 23), P(32, 23), P(29, 30), P(8, 30)], fill=ink)
        d.rectangle([x0 + 15 * u, y0 + 12 * u, x0 + 19 * u, y0 + 23 * u], fill=accent)
        d.rectangle([x0 + 8 * u, y0 + 17 * u, x0 + 14 * u, y0 + 23 * u], fill=ink)
        d.rectangle([x0 + 20 * u, y0 + 17 * u, x0 + 27 * u, y0 + 23 * u], fill=ink)
    elif name == "quake":
        d.line([P(3, 20), P(11, 20), P(14, 10), P(18, 28), P(21, 14), P(24, 20), P(33, 20)], fill=accent, width=3)
        d.line([P(6, 31), P(30, 31)], fill=ink, width=2)
    elif name == "badge":
        d.ellipse([x0 + 9 * u, y0 + 7 * u, x0 + 27 * u, y0 + 25 * u], outline=ink, width=2)
        d.polygon([P(18, 11), P(20, 16), P(25, 16.5), P(21.5, 20), P(22.5, 25), P(18, 22.5), P(13.5, 25), P(14.5, 20), P(11, 16.5), P(16, 16)], fill=accent)
        d.polygon([P(13, 25), P(17, 25), P(15, 32)], fill=ink)
        d.polygon([P(19, 25), P(23, 25), P(25, 32)], fill=ink)
    elif name == "dove":
        d.arc([x0 + 7 * u, y0 + 10 * u, x0 + 27 * u, y0 + 28 * u], 300, 130, fill=ink, width=3)
        d.polygon([P(22, 8), P(30, 12), P(23, 15)], fill=ink)
        d.line([P(26, 11), P(31, 7)], fill=(64, 145, 108), width=2)
        d.ellipse([x0 + 23 * u, y0 + 10 * u, x0 + 26 * u, y0 + 13 * u], fill=accent)
    elif name == "memo":
        d.rectangle([x0 + 10 * u, y0 + 6 * u, x0 + 26 * u, y0 + 30 * u], outline=ink, width=2)
        for i in range(4):
            d.line([P(13, 12 + i * 4), P(23, 12 + i * 4)], fill=ink, width=1)
        d.line([P(13, 26), P(21, 26)], fill=accent, width=2)
    elif name == "chart":
        d.line([P(6, 30), P(30, 30)], fill=ink, width=2)
        d.line([P(7, 10), P(14, 17), P(19, 14), P(28, 26)], fill=accent, width=3)
        d.polygon([P(28, 26), P(22, 25), P(27, 20)], fill=accent)
    elif name == "handshake":
        d.arc([x0 + 6 * u, y0 + 12 * u, x0 + 20 * u, y0 + 26 * u], 90, 270, fill=ink, width=3)
        d.arc([x0 + 16 * u, y0 + 12 * u, x0 + 30 * u, y0 + 26 * u], 270, 90, fill=ink, width=3)
        d.ellipse([x0 + 15 * u, y0 + 16 * u, x0 + 21 * u, y0 + 22 * u], fill=accent)
    elif name == "coin":
        d.ellipse([x0 + 8 * u, y0 + 8 * u, x0 + 28 * u, y0 + 28 * u], outline=(160, 120, 30), width=3)
        d.text((x0 + 14.5 * u, y0 + 11 * u), "€", fill=(160, 120, 30))
    elif name == "oil":
        d.polygon([P(18, 5), P(26, 18), P(26, 24), P(18, 31), P(10, 24), P(10, 18)], fill=ink)
        d.ellipse([x0 + 14 * u, y0 + 19 * u, x0 + 19 * u, y0 + 25 * u], fill=(240, 200, 90))
    elif name == "gold":
        d.polygon([P(7, 24), P(15, 16), P(23, 16), P(29, 24)], fill=(196, 150, 40))
        d.polygon([P(10, 29), P(16, 22), P(26, 22), P(30, 29)], fill=(160, 120, 30))
    elif name == "leaf":
        d.pieslice([x0 + 8 * u, y0 + 6 * u, x0 + 30 * u, y0 + 28 * u], 90, 360, fill=(64, 145, 108))
        d.line([P(11, 27), P(27, 11)], fill=ink, width=2)
    elif name == "ufo":
        d.ellipse([x0 + 5 * u, y0 + 15 * u, x0 + 31 * u, y0 + 23 * u], fill=ink)
        d.pieslice([x0 + 12 * u, y0 + 8 * u, x0 + 24 * u, y0 + 20 * u], 180, 360, fill=(150, 160, 180))
        for fx in (10, 17, 24):
            d.ellipse([x0 + fx * u, y0 + 18 * u, x0 + (fx + 3) * u, y0 + 21 * u], fill=(250, 210, 90))
        d.polygon([P(13, 24), P(23, 24), P(20, 32), P(16, 32)], fill=(250, 210, 90))
    elif name == "robot":
        d.rounded_rectangle([x0 + 10 * u, y0 + 11 * u, x0 + 26 * u, y0 + 27 * u], 3, outline=ink, width=2)
        d.line([P(18, 11), P(18, 6)], fill=ink, width=2)
        d.ellipse([x0 + 16.5 * u, y0 + 4 * u, x0 + 19.5 * u, y0 + 7 * u], fill=accent)
        d.ellipse([x0 + 13.5 * u, y0 + 16 * u, x0 + 16.5 * u, y0 + 19 * u], fill=accent)
        d.ellipse([x0 + 19.5 * u, y0 + 16 * u, x0 + 22.5 * u, y0 + 19 * u], fill=accent)
        d.line([P(14, 23), P(22, 23)], fill=ink, width=2)
    elif name == "cross":
        d.rectangle([x0 + 15 * u, y0 + 8 * u, x0 + 21 * u, y0 + 28 * u], fill=accent)
        d.rectangle([x0 + 9 * u, y0 + 14 * u, x0 + 27 * u, y0 + 20 * u], fill=accent)
    elif name == "bottle":
        d.rectangle([x0 + 15 * u, y0 + 5 * u, x0 + 21 * u, y0 + 11 * u], fill=ink)
        d.polygon([P(14, 11), P(22, 11), P(24, 18), P(24, 30), P(12, 30), P(12, 18)], fill=(120, 72, 40))
        d.rectangle([x0 + 14 * u, y0 + 19 * u, x0 + 22 * u, y0 + 26 * u], fill=(238, 231, 208))
        d.line([P(16, 24), P(20, 21)], fill=accent, width=2)
        d.line([P(16, 21), P(20, 24)], fill=accent, width=2)
    elif name == "boat":
        d.polygon([P(5, 21), P(31, 21), P(26, 29), P(10, 29)], fill=ink)
        d.line([P(18, 21), P(18, 8)], fill=ink, width=2)
        d.polygon([P(18, 9), P(26, 19), P(18, 19)], fill=accent)
        d.line([P(4, 32), P(12, 30), P(20, 32), P(28, 30), P(32, 32)], fill=(52, 110, 160), width=2)
    elif name == "flame":
        d.polygon([P(18, 4), P(24, 14), P(27, 20), P(24, 29), P(18, 32), P(12, 29), P(9, 20), P(13, 13)], fill=(226, 110, 40))
        d.polygon([P(18, 16), P(22, 22), P(21, 28), P(18, 30), P(15, 28), P(14, 22)], fill=(246, 190, 70))
    elif name == "target":
        d.ellipse([x0 + 7 * u, y0 + 7 * u, x0 + 29 * u, y0 + 29 * u], outline=ink, width=2)
        d.ellipse([x0 + 12 * u, y0 + 12 * u, x0 + 24 * u, y0 + 24 * u], outline=accent, width=2)
        d.ellipse([x0 + 16 * u, y0 + 16 * u, x0 + 20 * u, y0 + 20 * u], fill=accent)
    elif name == "mascot":
        d.ellipse([x0 + 8 * u, y0 + 8 * u, x0 + 28 * u, y0 + 28 * u], fill=(240, 170, 190))
        d.ellipse([x0 + 7 * u, y0 + 4 * u, x0 + 13 * u, y0 + 10 * u], fill=(240, 170, 190))
        d.ellipse([x0 + 23 * u, y0 + 4 * u, x0 + 29 * u, y0 + 10 * u], fill=(240, 170, 190))
        d.ellipse([x0 + 13 * u, y0 + 15 * u, x0 + 16 * u, y0 + 18 * u], fill=ink)
        d.ellipse([x0 + 20 * u, y0 + 15 * u, x0 + 23 * u, y0 + 18 * u], fill=ink)
        d.arc([x0 + 14 * u, y0 + 18 * u, x0 + 22 * u, y0 + 26 * u], 20, 160, fill=ink, width=2)
    elif name == "f1":
        d.polygon([P(4, 22), P(12, 18), P(24, 18), P(32, 22), P(32, 25), P(4, 25)], fill=ink)
        d.rectangle([x0 + 15 * u, y0 + 13 * u, x0 + 22 * u, y0 + 18 * u], fill=accent)
        d.ellipse([x0 + 7 * u, y0 + 23 * u, x0 + 13 * u, y0 + 29 * u], fill=(30, 30, 30))
        d.ellipse([x0 + 23 * u, y0 + 23 * u, x0 + 29 * u, y0 + 29 * u], fill=(30, 30, 30))
    elif name == "tennis":
        d.ellipse([x0 + 8 * u, y0 + 8 * u, x0 + 28 * u, y0 + 28 * u], fill=(168, 198, 60))
        d.arc([x0 + 2 * u, y0 + 8 * u, x0 + 18 * u, y0 + 28 * u], 270, 90, fill=(250, 250, 245), width=2)
        d.arc([x0 + 18 * u, y0 + 8 * u, x0 + 34 * u, y0 + 28 * u], 90, 270, fill=(250, 250, 245), width=2)
    elif name == "rugby":
        d.ellipse([x0 + 7 * u, y0 + 11 * u, x0 + 29 * u, y0 + 25 * u], fill=(140, 84, 44))
        d.line([P(15, 18), P(21, 18)], fill=(250, 250, 245), width=2)
        for i in range(3):
            d.line([P(16.5 + i * 1.8, 16), P(16.5 + i * 1.8, 20)], fill=(250, 250, 245), width=1)
    elif name == "football":
        d.ellipse([x0 + 8 * u, y0 + 8 * u, x0 + 28 * u, y0 + 28 * u], outline=ink, width=2)
        d.polygon([P(18, 13), P(22, 16), P(20.5, 21), P(15.5, 21), P(14, 16)], fill=ink)
        d.line([P(18, 13), P(18, 9)], fill=ink, width=1)
        d.line([P(14, 16), P(10, 14)], fill=ink, width=1)
        d.line([P(22, 16), P(26, 14)], fill=ink, width=1)
    else:
        d.ellipse([x0 + 11 * u, y0 + 11 * u, x0 + 25 * u, y0 + 25 * u], outline=ink, width=2)
        d.ellipse([x0 + 16 * u, y0 + 16 * u, x0 + 20 * u, y0 + 20 * u], fill=accent)
    return d


DRAWN_ICONS = {
    "shield", "radar", "tanker", "ship", "quake", "chart", "coin", "oil",
    "leaf", "ufo", "robot", "bottle", "boat", "flame", "mascot", "f1",
    "tennis", "football",
}
