from Hero import Hero
from Spell import Spell
#from Weapon import Weapon

import unittest


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero(name="Bron", title="Dragonslayer",
                         health=100, mana=100, mana_regen=2)
        self.spell = Spell("Fireball", 30, 50, 2)

    def test_init(self):
        self.assertTrue(isinstance(self.hero, Hero))

    def test_known_as(self):
        needed_result = "{} the {}".format(self.hero.name, self.hero.title)
        self.assertEqual(needed_result, Hero.known_as(self.hero))

    def test_get_health(self):
        self.assertEqual(Hero.get_health(self.hero), self.hero.health)

    def test_get_mana(self):
        self.assertEqual(Hero.get_mana(self.hero), self.hero.mana)

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive() != 0)

    def test_can_cast(self):
        self.hero.learn(self.spell)
        self.assertTrue(self.hero.can_cast())

    def test_take_damage(self):
        self.assertEqual(self.hero.take_damage(101), 0)

    def test_healing(self):
        self.hero.health = 0
        self.assertFalse(self.hero.take_healing(50))
        self.hero.health = 100
        self.assertTrue(self.hero.take_healing(50))

    def test_take_mana(self):
        self.hero.take_mana(202)
        self.assertEqual(self.hero.mana, 100)

    def test_equip(self):
        false_instance = 6
        self.assertFalse(self.hero.equip(false_instance))

    def test_learn(self):
        false_instance = 6
        self.assertFalse(self.hero.learn(false_instance))

    def test_attack(self):
        self.assertFalse(self.hero.attack("something"))
        self.hero.weapon = None
        self.hero.spell = None
        self.assertEqual(self.hero.attack("something"), 0)
        other = Hero(name="Bron", title="Dragonslayer",
                     health=100, mana=100, mana_regen=2,weapon=None, spell=None)
        self.assertEqual(other.attack("weapon"), other.weapon.power)

if __name__ == '__main__':
    unittest.main()
