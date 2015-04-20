from Spell import Spell
import unittest


class TestSpell(unittest.TestCase):

    def setUp(self):
        self.test_spell = Spell(
            name="Fireball", power=30, mana_cost=50, cast_range=2)

    def test_init(self):
        self.assertTrue(isinstance(self.test_spell, Spell))

if __name__ == '__main__':
    unittest.main()
