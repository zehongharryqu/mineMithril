"""stores the coords in px of bz items"""


class BzcoordTree:
    """Navigates the bazaar window"""

    def __init__(self, name, coords, sub):
        self.name = name
        self.coords = coords
        self.sub = sub

    def find(self, key):
        if self.name == key:  # leaf and match
            return [self.coords]
        else:
            if self.sub:  # node
                for node in self.sub:
                    result = node.find(key)
                    if result:  # found in sub
                        return [self.coords] + result
                return []  # couldn't find in any sub
            else:  # leaf and not match
                return []


# anchors
CELL = 36
FARMING = (575, 280)
DONE = (720, 485)

BUY = (FARMING[0] + 6 * CELL, FARMING[1] + 2 * CELL)
AMOUNT = (FARMING[0] + 7 * CELL, FARMING[1] + 2 * CELL)
CONFIRM = (FARMING[0] + 4 * CELL, FARMING[1] + 2 * CELL)

COORDS = BzcoordTree("root", (0, 0), [
    BzcoordTree("farming", FARMING, [
        BzcoordTree("wheats", (FARMING[0]+2*CELL, FARMING[1]+1*CELL), [
            BzcoordTree("wheat", (FARMING[0]+2*CELL, FARMING[1]+2*CELL), []),
            BzcoordTree("ebread", (FARMING[0]+3*CELL, FARMING[1]+2*CELL), []),
            BzcoordTree("hay", (FARMING[0] + 4 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("ehay", (FARMING[0] + 5 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("tthay", (FARMING[0] + 6 * CELL, FARMING[1] + 2 * CELL), [])
        ]),
        BzcoordTree("carrots", (FARMING[0] + 3 * CELL, FARMING[1] + 1 * CELL), [
            BzcoordTree("carrot", (FARMING[0] + 1 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("ecarrot", (FARMING[0] + 3 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("ecarrotstick", (FARMING[0] + 5 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("egcarrot", (FARMING[0] + 7 * CELL, FARMING[1] + 2 * CELL), [])
        ]),
        BzcoordTree("potatoes", (FARMING[0] + 4 * CELL, FARMING[1] + 1 * CELL), [
            BzcoordTree("potato", (FARMING[0] + 2 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("epotato", (FARMING[0] + 4 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("ebpotato", (FARMING[0] + 6 * CELL, FARMING[1] + 2 * CELL), [])
        ]),
        BzcoordTree("pumpkins", (FARMING[0] + 5 * CELL, FARMING[1] + 1 * CELL), [
            BzcoordTree("pumpkin", (FARMING[0] + 2 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("epumpkin", (FARMING[0] + 4 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("ppumpkin", (FARMING[0] + 6 * CELL, FARMING[1] + 2 * CELL), [])
        ]),
        BzcoordTree("melons", (FARMING[0] + 6 * CELL, FARMING[1] + 1 * CELL), [
            BzcoordTree("melon", (FARMING[0] + 2 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("emelon", (FARMING[0] + 3 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("egmelon", (FARMING[0] + 4 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("melonblock", (FARMING[0] + 5 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("emelonblock", (FARMING[0] + 6 * CELL, FARMING[1] + 2 * CELL), [])
        ]),
        BzcoordTree("mushrooms", (FARMING[0] + 7 * CELL, FARMING[1] + 1 * CELL), []),
        BzcoordTree("cocoabeans", (FARMING[0] + 2 * CELL, FARMING[1] + 2 * CELL), []),
        BzcoordTree("cacti", (FARMING[0] + 3 * CELL, FARMING[1] + 2 * CELL), []),
        BzcoordTree("canes", (FARMING[0] + 4 * CELL, FARMING[1] + 2 * CELL), [
            BzcoordTree("cane", (FARMING[0] + 1 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("sugar", (FARMING[0] + 3 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("epaper", (FARMING[0] + 5 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("ecane", (FARMING[0] + 7 * CELL, FARMING[1] + 2 * CELL), [])
        ]),
        BzcoordTree("leathers", (FARMING[0] + 5 * CELL, FARMING[1] + 2 * CELL), [
            BzcoordTree("leather", (FARMING[0] + 1 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("eleather", (FARMING[0] + 3 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("beef", (FARMING[0] + 5 * CELL, FARMING[1] + 2 * CELL), []),
            BzcoordTree("ebeef", (FARMING[0] + 7 * CELL, FARMING[1] + 2 * CELL), [])
        ])
    ]),
    BzcoordTree("mining", (FARMING[0], FARMING[1] + 1 * CELL), [
        BzcoordTree("gemstones", (FARMING[0] + 2 * CELL, FARMING[1] + 2 * CELL), [
            BzcoordTree("jade", (FARMING[0] + 1 * CELL, FARMING[1]), []),
            BzcoordTree("amber", (FARMING[0] + 2 * CELL, FARMING[1]), []),
            BzcoordTree("topaz", (FARMING[0] + 3 * CELL, FARMING[1]), []),
            BzcoordTree("sapphire", (FARMING[0] + 4 * CELL, FARMING[1]), []),
            BzcoordTree("amethyst", (FARMING[0] + 5 * CELL, FARMING[1]), []),
            BzcoordTree("jasper", (FARMING[0] + 6 * CELL, FARMING[1]), []),
            BzcoordTree("ruby", (FARMING[0] + 7 * CELL, FARMING[1]), []),
            BzcoordTree("opal", (FARMING[0] + 8 * CELL, FARMING[1]), [])
        ])
    ])
])
