from Hero import Hero
from Enemy import Enemy
from Weapon import Weapon
from Spell import Spell


class Fight:

    def __init__(self, hero, enemy):
        if not isinstance(hero, Hero) or not isinstance(enemy, Enemy):
            raise AttributeError
        print("A fight started between" + hero + " and " + enemy)
        while hero.get_health() != 0 or enemy.get_health() != 0:
            enemy.health-=hero.weapon.power
            print("{} hits with {} for {} dmg. Enemy health is {}.").format(hero.name, hero.weapon.name, hero.weapon.power, enemy.get_health())
            hero.take_damage(enemy.damage)
            print("Enemy hits {} for {} dmg. {} health is {}").format(hero.name, enemy.damage, hero.name, hero.get_health())
        if hero.get_health() == 0:
            print("Hero is dead ! Game over !")
        if enemy.get_health() == 0:
            print("Enemy is dead !")
