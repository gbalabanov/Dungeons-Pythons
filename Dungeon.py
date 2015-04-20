import os
from Hero import Hero
from Enemy import Enemy
from Weapon import Weapon
from Spell import Spell
from Fight import Fight


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
        self._enemies = []
        for row in self._map:
            for col in row:
                if col == "E":
                    self._enemies.append(Enemy(100, 100, 50))

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
            if self._map[self._hero._y][self._hero._x + 1] == "E":
                f = Fight(self._hero, self._enemies.pop())
                f.start_battle(self._hero, self._enemies.pop())
            self._map[self._hero._y][self._hero._x] = "."
            self._hero._x += 1
            self._map[self._hero._y][self._hero._x] = "H"
            return True
        if direction == "left":
            if self._hero._x == 0:
                return False
            if self._map[self._hero._y][self._hero._ - 1] == "#":
                return False
            if self._map[self._hero._y][self._hero._x - 1] == "E":
                f = Fight(self._hero, self._enemies.pop())
                f.start_battle(self._hero, self._enemies.pop())
            self._map[self._hero._y][self._hero._x] = "."
            self._hero._x -= 1
            self._map[self._hero._y][self._hero._x] = "H"
            return True
        if direction == "up":
            if self._hero._y == 0:
                return False
            if self._map[self._hero._y - 1][self._hero._x] == "#":
                return False
            if self._map[self._hero._y - 1][self._hero._x] == "E":
                f = Fight(self._hero, self._enemies.pop())
                f.start_battle(self._hero, self._enemies.pop())
            self._map[self._hero._y][self._hero._x] = "."
            self._hero._y -= 1
            self._map[self._hero._y][self._hero._x] = "H"
            return True
        if direction == "down":
            if self._hero._y == len(self._map) - 1:
                return False
            if self._map[self._hero._y + 1][self._hero._x] == "#":
                return False
            if self._map[self._hero._y + 1][self._hero._x] == "E":
                f = Fight(self._hero, self._enemies.pop())
                f.start_battle(self._hero, self._enemies.pop())
            self._map[self._hero._y][self._hero._x] = "."
            self._hero._y += 1
            self._map[self._hero._y][self._hero._x] = "H"
            return True

    def hero_atack(self):
        top_border = False
        bot_border = False
        left_border = False
        right_border = False
        if self._hero is None or self._hero.spell is None:
            return False
        for rng in range(0, self._hero.spell.cast_range + 1):
            top_border = self._hero._y == 0
            if not top_border:
                if self._map[self._hero._y - rng][self._hero._x] == "E":
                    f = Fight(self._hero, self._enemies.pop())
                    f.start_battle(self._hero, self._enemies.pop())
            bot_border = self._hero._y == len(self._map)
            if not bot_border:
                if self._map[self._hero._y + rng][self._hero._x] == "E":
                    f = Fight(self._hero, self._enemies.pop())
                    f.start_battle(self._hero, self._enemies.pop())
            left_border = self._hero._x == 0
            if not left_border:
                if self._map[self._hero._y][self._hero._x - rng] == "E":
                    f = Fight(self._hero, self._enemies.pop())
                    f.start_battle(self._hero, self._enemies.pop())
            right_border = self._hero._x == 0
            if not right_border:
                if self._map[self._hero._y][self._hero._x + rng] == "E":
                    f = Fight(self._hero, self._enemies.pop())
                    f.start_battle(self._hero, self._enemies.pop())


def main():

    d = Dungeon("level1.txt")
    hero = Hero("batman", "the dark knight", 100, 100, 2)
    wep = Weapon("Axe", 50)
    hero.equip(wep)
    print(d.spawn(hero))
    d.move_hero("right")
    d.print_map()
    print(hero.get_health())

if __name__ == '__main__':
    main()
