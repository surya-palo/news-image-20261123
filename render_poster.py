#!/usr/bin/env python3
"""Render the news-image-20261123 poster (1024x1024) with PIL.

Build-time tool only: it draws entry.png from the verified story list
below. The graded entrypoint (main.py) merely copies entry.png.
Run:  python3 render_poster.py   -> writes entry.png next to this file.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)      # warm newsprint
INK = (26, 26, 26)
RED = (176, 42, 32)
NAVY = (31, 58, 95)
GREY = (90, 86, 78)
RULE = (26, 26, 26)
CARD_BG = (255, 253, 247)
GOLD = (176, 132, 32)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centered(draw, text, y, fnt, fill, cx=W // 2):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def spaced_text(draw, text, y, fnt, fill, tracking=4):
    """Draw uppercase text with letter tracking, centred."""
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = (W - total) / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + tracking
    return y + fnt.size


# ---------------------------------------------------------------- icons
def icon_globe(d, x, y, s, col):
    d.ellipse([x, y, x + s, y + s], outline=col, width=3)
    d.arc([x + s * 0.28, y, x + s * 0.72, y + s], 270, 90, fill=col, width=2)
    d.arc([x + s * 0.28, y, x + s * 0.72, y + s], 90, 270, fill=col, width=2)
    d.line([x, y + s * 0.5, x + s, y + s * 0.5], fill=col, width=2)


def icon_chart(d, x, y, s, col):
    d.line([x, y + s, x + s, y + s], fill=col, width=3)
    d.line([x, y + s, x, y], fill=col, width=3)
    d.line([x + 4, y + s * 0.55, x + s * 0.35, y + s * 0.35,
            x + s * 0.6, y + s * 0.62, x + s - 4, y + s * 0.18],
           fill=RED, width=4)


def icon_factory(d, x, y, s, col):
    d.rectangle([x, y + s * 0.45, x + s * 0.62, y + s], fill=col)
    d.rectangle([x + s * 0.62, y + s * 0.62, x + s, y + s], fill=col)
    d.rectangle([x + s * 0.12, y + s * 0.12, x + s * 0.26, y + s * 0.5],
                fill=col)
    for wx in (0.08, 0.30, 0.52):
        d.rectangle([x + s * wx, y + s * 0.58, x + s * (wx + 0.10),
                     y + s * 0.72], fill=PAPER)


def icon_ball(d, x, y, s, col):
    d.ellipse([x, y, x + s, y + s], outline=col, width=3)
    d.arc([x + s * 0.15, y + s * 0.15, x + s * 0.85, y + s * 0.85],
          200, 340, fill=RED, width=3)


def icon_building(d, x, y, s, col):
    d.rectangle([x + s * 0.2, y, x + s * 0.8, y + s], outline=col, width=3)
    for i in range(3):
        for j in range(3):
            d.rectangle([x + s * (0.3 + j * 0.18), y + s * (0.15 + i * 0.28),
                         x + s * (0.42 + j * 0.18), y + s * (0.27 + i * 0.28)],
                        fill=col)


def icon_flags(d, x, y, s, col):
    # Two small waving flags on poles (abstract: India + Nepal colours).
    d.line([x + s * 0.2, y, x + s * 0.2, y + s], fill=col, width=3)
    d.line([x + s * 0.72, y, x + s * 0.72, y + s], fill=col, width=3)
    d.polygon([(x + s * 0.2, y + 2), (x + s * 0.58, y + 10),
               (x + s * 0.2, y + 18)], fill=(255, 153, 51))
    d.polygon([(x + s * 0.72, y + 2), (x + s * 0.34, y + 10),
               (x + s * 0.72, y + 18)], fill=(220, 20, 60))


# ---------------------------------------------------------------- poster
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    d.rectangle([0, 0, W, 10], fill=RED)
    f_title = font(SERIF_B, 62)
    centered(d, "THE WORLD IN ONE DAY", 26, f_title, INK)
    f_date = font(SANS_B, 30)
    spaced_text(d, "MONDAY  23 NOVEMBER 2026", 100, f_date, RED, tracking=5)
    d.line([28, 146, W - 28, 146], fill=RULE, width=3)
    d.line([28, 151, W - 28, 151], fill=RULE, width=1)

    # ---- lead story ----------------------------------------------------
    lx, ly, lw, lh = 28, 166, W - 56, 236
    d.rectangle([lx, ly, lx + lw, ly + lh], outline=RULE, width=2,
                fill=CARD_BG)
    f_kick = font(SANS_B, 17)
    d.text((lx + 18, ly + 12), "LEAD  \u00b7  MARKETS", font=f_kick, fill=RED)
    f_lead = font(SERIF_B, 40)
    lead_head = ["WALL STREET BRACES", "AFTER AI SELL-OFF"]
    y = ly + 38
    for line in lead_head:
        d.text((lx + 18, y), line, font=f_lead, fill=INK)
        y += 48
    f_body = font(SANS, 20)
    body = ("Stocks steadied on Monday after Friday's rout - the S&P 500 "
            "fell 3.7% and the Nasdaq 5.3% - as investors questioned the "
            "payoff from vast AI spending. US futures pointed higher.")
    lines = wrap(d, body, f_body, 620)
    assert len(lines) <= 3, lines
    draw_lines(d, lines, lx + 18, y + 4, f_body, INK, 25)

    # mini falling-market chart, right side of the lead box
    cx0, cy0, cw, chh = 700, ly + 44, 260, 158
    d.rectangle([cx0, cy0, cx0 + cw, cy0 + chh], outline=GREY, width=1)
    d.line([cx0 + 14, cy0 + chh - 34, cx0 + cw - 14, cy0 + chh - 34],
           fill=GREY, width=1)
    pts = [(cx0 + 16 + i * 34, cy0 + 26 + i * 15 + (0 if i < 3 else 8))
           for i in range(7)]
    d.line(pts, fill=RED, width=4)
    for px, py in pts:
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=RED)
    f_lab = font(SANS_B, 15)
    for txt, yy in (("S&P 500  -3.7%", cy0 + 6), ("Nasdaq  -5.3%", cy0 + 26)):
        tw = d.textlength(txt, font=f_lab)
        d.text((cx0 + cw - 10 - tw, yy), txt, font=f_lab, fill=RED)
    f_cap = font(SANS, 13)
    d.text((cx0 + 14, cy0 + chh - 26), "FRIDAY'S ROUT", font=f_cap, fill=GREY)

    # ---- story cards ---------------------------------------------------
    cards = [
        ("DIPLOMACY", "Nepal's PM meets Modi in Delhi",
         "Balendra Shah, on his first trip abroad since taking office in "
         "March, holds talks with Narendra Modi on energy, trade and "
         "connectivity.",
         icon_flags),
        ("CLIMATE", "COP31 fallout: 'worst ever'",
         "A day after climate talks in Antalya ended with no deal, "
         "governments and campaigners trade blame - the first COP to "
         "fail outright since 2009.",
         icon_globe),
        ("DISASTER", "Search resumes at torched factory",
         "Rescuers return at dawn to the ruined Java candy factory, "
         "where dozens are still missing after Saturday's blaze; at "
         "least three are dead.",
         icon_factory),
        ("SPORT", "India hunt eight wickets on final day",
         "New Zealand resume on 119 for 2, still 233 behind after "
         "India's record 720 for 9 - the highest Test total ever made "
         "in New Zealand.",
         icon_ball),
        ("BUSINESS", "Home Depot's new chief takes over",
         "Richard McPhail becomes chief executive today, stepping up "
         "from finance chief as the retailer lifts its full-year "
         "outlook.",
         icon_building),
    ]
    gx, gy = 28, 418
    cw2, ch2, gut = 474, 168, 20
    f_ck = font(SANS_B, 16)
    f_ch = font(SERIF_B, 25)
    f_cb = font(SANS, 17)
    for i, (kick, head, body, icon) in enumerate(cards):
        x = gx + (i % 2) * (cw2 + gut)
        y = gy + (i // 2) * (ch2 + 16)
        d.rectangle([x, y, x + cw2, y + ch2], outline=RULE, width=2,
                    fill=CARD_BG)
        d.text((x + 16, y + 12), kick, font=f_ck, fill=RED)
        icon(d, x + cw2 - 64, y + 8, 48, NAVY)
        hl = wrap(d, head, f_ch, cw2 - 32 - 62)
        assert len(hl) <= 2, hl
        yy = draw_lines(d, hl, x + 16, y + 36, f_ch, INK, 30)
        bl = wrap(d, body, f_cb, cw2 - 32)
        assert len(bl) <= 3, bl
        draw_lines(d, bl, x + 16, yy + 4, f_cb, INK, 22)

    # ---- numbers box (6th cell) ----------------------------------------
    x = gx + (cw2 + gut)
    y = gy + 2 * (ch2 + 16)
    d.rectangle([x, y, x + cw2, y + ch2], outline=RULE, width=2, fill=NAVY)
    d.text((x + 16, y + 12), "THE DAY IN NUMBERS", font=f_ck, fill=(255, 210, 120))
    nums = [("-3.7%", "S&P 500 on Friday"),
            ("-5.3%", "Nasdaq on Friday"),
            ("720/9", "India's record Test total"),
            ("~50", "workers missing in Java")]
    f_num = font(SANS_B, 24)
    f_nlab = font(SANS, 17)
    yy = y + 42
    for val, lab in nums:
        d.text((x + 16, yy), val, font=f_num, fill=(255, 255, 255))
        d.text((x + 130, yy + 4), lab, font=f_nlab, fill=(220, 225, 235))
        yy += 30

    # ---- footer ---------------------------------------------------------
    d.line([28, 972, W - 28, 972], fill=RULE, width=1)
    f_foot = font(SANS, 15)
    centered(d, "All stories happened or were first reported on Monday 23 November 2026",
             980, f_foot, GREY)
    f_src = font(SANS, 13)
    centered(d, "Sources: Reuters  \u00b7  AP  \u00b7  IANS  \u00b7  The Hindu",
             1002, f_src, GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
