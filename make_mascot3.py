#!/usr/bin/env python3
"""Mascot extension pose for AiProve aiprove-mascot: 'Pose 4 — At the Velvet
Rope'. Composites the original Clerk-Bot pose-1 crop from the character sheet
(mascot.png) onto a new cream card, adds a PIL-drawn velvet rope with gold
stanchions in the foreground and a golden 'ADMIT ONE — 100,000 $PROVE'
ticket by his stamp hand."""
import math
from PIL import Image, ImageDraw, ImageFont

SHEET = "/home/hatch/workspace/aiprove/art/mascot.png"
FONT = "/home/hatch/workspace/makefun/fonts/PatrickHand-Regular.ttf"
W, H = 1600, 1150

img = Image.new("RGB", (W, H), (246, 239, 222))
d = ImageDraw.Draw(img, "RGBA")

# crop Clerk-Bot pose 1 (waving, stamp in hand) from the sheet
sheet = Image.open(SHEET).convert("RGB")
bot = sheet.crop((58, 258, 648, 1008))  # 590 x 750
img.paste(bot, (90, 210))
d = ImageDraw.Draw(img, "RGBA")

# title
fT = ImageFont.truetype(FONT, 64)
fS = ImageFont.truetype(FONT, 36)
d.text((W // 2, 78), "CLERK-BOT — POSE 4: AT THE VELVET ROPE", font=fT, fill=(30, 60, 40), anchor="mm")
d.line([(90, 140), (W - 90, 140)], fill=(30, 60, 40), width=4)

# golden ticket layer, rotated, placed by the stamp hand (right side)
tick = Image.new("RGBA", (560, 250), (0, 0, 0, 0))
td = ImageDraw.Draw(tick)
td.rounded_rectangle([6, 6, 554, 244], radius=22, fill=(238, 200, 105, 255), outline=(120, 84, 20, 255), width=6)
td.line([(70, 20), (70, 230)], fill=(120, 84, 20, 255), width=3)
fA = ImageFont.truetype(FONT, 52)
fB = ImageFont.truetype(FONT, 62)
fC = ImageFont.truetype(FONT, 34)
td.text((312, 62), "ADMIT ONE", font=fA, fill=(74, 50, 8), anchor="mm")
td.text((312, 132), "100,000 $PROVE", font=fB, fill=(74, 50, 8), anchor="mm")
td.text((312, 198), "SEASON 1 — HOLD TO PLAY", font=fC, fill=(74, 50, 8), anchor="mm")
tick = tick.rotate(7, expand=True, resample=Image.BICUBIC)
img.paste(tick, (860, 330), tick)
d = ImageDraw.Draw(img, "RGBA")

# speech line from Clerk-Bot
fQ = ImageFont.truetype(FONT, 40)
d.rounded_rectangle([880, 640, 1520, 760], radius=20, fill=(255, 255, 255), outline=(30, 60, 40), width=4)
d.text((1200, 682), '"Ticket, please. The stamp', font=fQ, fill=(30, 40, 34), anchor="mm")
d.text((1200, 726), 'is ready when you are."', font=fQ, fill=(30, 40, 34), anchor="mm")

# velvet rope across the foreground
GOLD = (196, 152, 52)
GOLD_D = (130, 96, 26)
RED = (170, 28, 44)
RED_D = (104, 14, 26)
def stanchion(x, top=872, base=1052):
    d.ellipse([x - 46, base - 12, x + 46, base + 14], fill=GOLD_D)
    d.rectangle([x - 8, top + 22, x + 8, base - 4], fill=GOLD)
    d.ellipse([x - 21, top, x + 21, top + 42], fill=GOLD)
stanchion(140)
stanchion(1460)
pts = []
for i in range(121):
    t = i / 120
    x = 140 + t * 1320
    y = 912 + 74 * math.sin(math.pi * t) ** 1.3
    pts.append((x, y))
d.line(pts, fill=RED_D, width=24)
d.line([(x, y - 5) for x, y in pts], fill=RED, width=15)

# footer in sheet style
fF = ImageFont.truetype(FONT, 34)
d.text((W // 2, 1108), "MODEL: CLERK-BOT • FUNCTION: STAMP • CERTIFY • QUEUE POLITELY • EXTENSION POSE, AIPROVE MASCOT SHEET",
       font=fF, fill=(52, 56, 52), anchor="mm")

img.save("/home/hatch/workspace/aiprove/round5/clerkbot-velvet-rope.png")
print("saved mascot pose 4")
