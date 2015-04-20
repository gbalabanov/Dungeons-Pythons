from Hero import Hero
from Enemy import Enemy
from Weapon import Weapon
from Spell import Spell


class Fight:

    def __init__(self, hero, enemy):
        if not isinstance(hero, Hero) or not isinstance(enemy, Enemy):
            raise AttributeError
        print("A fight started between " + repr(hero) + " and " + repr(enemy))
        while True:
            enemy.take_damage(hero.weapon.power)
            print("{} hits with {} for {} dmg. Enemy health is {}.".format(hero.name, hero.weapon.name, hero.weapon.power, enemy.get_health()))
            if not enemy.is_alive():
                print("Enemy is dead !")
                break
            hero.take_damage(enemy.damage)
            print("Enemy hits {} for {} dmg. {} health is {}".format(hero.name, enemy.damage, hero.name, hero.get_health()))
            if not hero.is_alive():
                print("Hero is dead ! \n ===Game over ====")
                break
