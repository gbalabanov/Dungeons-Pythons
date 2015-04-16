import os
from Hero import Hero
from Enemy import Enemy
from Weapon import Weapon
from Spell import Spell


class Dungeon:

    def __init__(self, map_file):
        if os.path.isfile(map_file) == False:
            raise AttributeError("No such file!")
        with open(map_file, "r") as f:
            matrix = []
            for line in f.readlines():
                matrix.append(list(line.strip("\n")))
        self._map = matrix
        self._hero = None

    def print_map(self):
        output = (["".join(x) for x in self._map])
        for x in output:
            print(x, end="\n")

    def spawn(self, myhero):
        if not isinstance(myhero, Hero):
            raise ValueError
        x = 0
        y = 0
        found = False
        for row in self._map:
            for col in row:
                if col == "S":
                    found = True
                    self._map[x][y] = "H"
                    myhero._x = x
                    myhero._y = y
                    self._hero = myhero
                    return True
                x += 1
            x = 0
            y += 1

    def move_hero(self, direction):
        if direction not in ["up", "down", "left", "right"]:
            raise ValueError
        if direction == "right":
            if self._hero._x == len(self._map[0]) - 1:
                return False
            if self._map[self._hero._y][self._hero._x + 1] == "#":
                return False
            self._map[self._hero._y][self._hero._x] = "."
            self._hero._x += 1
            self._map[self._hero._y][self._hero._x] = "H"
            return True
        if direction == "left":
            if self._hero._x == 0:
                return False
            if self._map[self._hero._y][self._hero._ - 1] == "#":
                return False
            self._map[self._hero._y][self._hero._x] = "."
            self._hero._x -= 1
            self._map[self._hero._y][self._hero._x] = "H"
            return True
        if direction == "up":
            if self._hero._y == 0:
                return False
            if self._map[self._hero._y - 1][self._hero._x] == "#":
                return False
            self._map[self._hero._y][self._hero._x] = "."
            self._hero._y -= 1
            self._map[self._hero._y][self._hero._x] = "H"
            return True
        if direction == "down":
            if self._hero._y == len(self._map) - 1:
                return False
            if self._map[self._hero._y + 1][self._hero._x] == "#":
                return False
            self._map[self._hero._y][self._hero._x] = "."
            self._hero._y += 1
            self._map[self._hero._y][self._hero._x] = "H"
            return True


def main():

    d = Dungeon("level1.txt")
    hero = Hero("batman", "the dark knight", 100, 100, 2)
    print(d.spawn(hero))
    print(d.move_hero("down"))
    d.print_map()

if __name__ == '__main__':
    main()
