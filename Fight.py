from Hero import Hero
from Enemy import Enemy
from Weapon import Weapon
from Spell import Spell


class Fight:

    def __init__(self, hero, enemy):
        if not isinstance(hero, Hero) or not isinstance(enemy, Enemy):
            raise AttributeError
        print("A fight started between " + repr(hero) + " and " + repr(enemy))
        self.hero = hero
        self.enemy = enemy


    def start_battle(self, hero, enemy):
            dist = self.get_distance()
            while True:
                for x in range(0, dist):
                    if self.hero.can_cast():
                        self.hero.mana-=self.hero.spell.mana_cost
                        self.enemy.take_damage(self.hero.spell.power)
                        print("Hero casts a {} ({} mana left), hits enemy for {} dmg. Enemy health is {}".format(self.hero.spell.name,self.hero.mana ,self.hero.spell.power, self.enemy.health))
                    else:
                        print("Hero can not cast a spell.")
                    print("Enemy moves one block closer to Hero. This is his move.")
                    dist-=1
                self.enemy.take_damage(self.hero.weapon.power)
                print("{} hits with {} for {} dmg. Enemy health is {}.".format(self.hero.name, self.hero.weapon.name, self.hero.weapon.power, self.enemy.get_health()))
                if not self.enemy.is_alive():
                    print("Enemy is dead !")
                    return True
                self.hero.take_damage(self.enemy.damage)
                print("Enemy hits {} for {} dmg. {} health is {}".format(self.hero.name, self.enemy.damage, self.hero.name, self.hero.get_health()))
                if not self.hero.is_alive():
                    print("Hero is dead ! \n ===Game over ====")
                    return False

    def get_distance(self):
        if self.hero._x == self.enemy._x:
            return abs(self.hero._y - self.enemy._y)
        return abs(self.hero._x - self.enemy._y)


