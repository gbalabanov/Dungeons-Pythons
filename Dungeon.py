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
        enemy_x=0
        enemy_y=0
        for row in self._map:
            for col in row:
                if col == "E":
                    self._enemies.append(Enemy(100, 100, 30, enemy_x, enemy_y))
                enemy_x+=1
            enemy_x=0
            enemy_y+=1

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

    def hero_atack(self,by):
        if by == "spell":
            top_border = False
            bot_border = False
            left_border = False
            right_border = False
            if self._hero is None or self._hero.spell is None:
                return False
            for rng in range(0, self._hero.spell.cast_range + 1):
                top_border = self._hero._y == 0
                if not top_border:
                    if self._map[self._hero._y - rng][self._hero._x] == "E" and self._hero.can_cast():
                        enemy = self._enemies.pop()
                        f = Fight(self._hero, enemy)
                        if f.start_battle(self._hero, enemy):
                            self._map[enemy._y][enemy._x] = "."
                            return True
                bot_border = self._hero._y == len(self._map)
                if not bot_border:
                    if self._map[self._hero._y + rng][self._hero._x] == "E" and self._hero.can_cast():
                        enemy = self._enemies.pop()
                        f = Fight(self._hero, enemy)
                        print(enemy._x, enemy._y)
                        if f.start_battle(self._hero, enemy):
                            self._map[enemy._y][enemy._x] = "."
                            return True
                left_border = self._hero._x == 0
                if not left_border:
                    if self._map[self._hero._y][self._hero._x - rng] == "E" and self._hero.can_cast():
                        enemy = self._enemies.pop()
                        f = Fight(self._hero, enemy)
                        if f.start_battle(self._hero, enemy):
                            self._map[enemy._y][enemy._x] = "."
                            return True
                right_border = self._hero._x == 0
                if not right_border:
                    if self._map[self._hero._y][self._hero._x + rng] == "E" and self._hero.can_cast():
                        enemy = self._enemies.pop()
                        f = Fight(self._hero, enemy)
                        if f.start_battle(self._hero, enemy):
                            self._map[enemy._y][enemy._x] = "."
                            return True
        return False


def main():

    d = Dungeon("level1.txt")
    hero = Hero("batman", "the dark knight", 100, 100, 3)
    wep = Weapon("Axe", 10)
    hero.equip(wep)
    print(d.spawn(hero))
    d.move_hero("right")
    d.print_map()
    print(hero.get_health())
    spell = Spell("cherna maiq", 10, 20, 3)
    hero.learn(spell)
    print(d.hero_atack(by="spell"))
    d.print_map()

if __name__ == '__main__':
    main()
