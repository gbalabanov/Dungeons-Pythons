import os
from Hero import Hero
from Enemy import Enemy
from Weapon import Weapon
from Spell import Spell


class Dungeon:

    def __init__(self, map_file):
        if os.path.isfile(map_file) == False:
            raise AttributeError("No such directory !")
        with open(map_file, "r") as f:
            matrix = []
            for line in f.readlines():
                matrix.append(list(line.strip("\n")))
        self._map = matrix

    def print_map(self):
        output = (["".join(x) for x in self._map])
        for x in output:
            print(x, end="\n")

    def spawn(self,myhero):
        if not isinstance(myhero, Hero):
            raise ValueError
        x = 0
        y = 0
        found = False
        for row in self._map:
            for col in row:
                if col == "S":
                    print(x, y)
                    found = True
                    return True
                y += 1
            y = 0
            x += 1


d = Dungeon("level1.txt")
print(d.spawn())
