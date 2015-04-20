import os
from Hero import Hero
from Enemy import Enemy
from Weapon import Weapon
from Spell import Spell
from Dungeon import Dungeon
import unittest


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.map = Dungeon('level1.txt')

    def test_init(self):
        with self.assertRaises(AttributeError):
            dg = Dungeon('blabla')
        self.assertTrue()
if __name__ == '__main__':
    unittest.main()
