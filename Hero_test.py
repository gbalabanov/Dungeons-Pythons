from Hero import Hero
import unittest


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero(name="Bron", title="Dragonslayer",
                         health=100, mana=100, mana_regen=2)

    def test_init(self):
        self.assertTrue(isinstance(self.hero, Hero))

    def test_known_as(self):
        needed_result = "{} the {}".format(self.hero.name, self.hero.title)
        self.assertEqual(needed_result, Hero.known_as(self.hero))

    def test_get_health(self):
        self.assertEqual(Hero.get_health(self.hero), self.hero.health)

if __name__ == '__main__':
    unittest.main()
