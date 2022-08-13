"""stores the coords in px of bz items"""

# anchors
NEXT_SLOT = 36
MINING = (575, 335)
JADE = (610, 280)
DONE = (715, 490)

COORDS = {
  # main bz screen
  "mining": MINING,
  "jade": JADE,
  "done": DONE,
  # mining screen
  "gems": (MINING[0] + 8 * NEXT_SLOT, MINING[1]),
  "ices": (MINING[0] + 2 * NEXT_SLOT, MINING[1] + 2 * NEXT_SLOT),
  # gems screen
  "topaz": (JADE[0] + 2 * NEXT_SLOT, JADE[1]),
  # ices screen
  "ice": (JADE[0], JADE[1] + 2 * NEXT_SLOT),
  # individual item screen
  "buy": (JADE[0] + 5 * NEXT_SLOT, JADE[1] + 2 * NEXT_SLOT),
  "amount": (JADE[0] + 6 * NEXT_SLOT, JADE[1] + 2 * NEXT_SLOT),
  "confirm": (JADE[0] + 3 * NEXT_SLOT, JADE[1] + 2 * NEXT_SLOT)
}
