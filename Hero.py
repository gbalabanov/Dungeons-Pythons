from Spell import Spell
from Weapon import Weapon

class Hero:

    def __init__(self, name, title, health, mana, mana_regen, weapon=None, spell=None):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regen = mana_regen
        self.max_health = health
        self.max_mana = mana
        self._x = 0
        self._y = 0

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health != 0

    def can_cast(self):
        return self.mana > self.spell.mana_cost

    def take_damage(self, dmg_points):
        if dmg_points >= self.get_health():
            self.health = 0
        else:
            self.health -= dmg_points
        return self.health

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        if healing_points + self.health > self.max_health:
            self.health = self.max_health
            return True
        else:
            self.health += healing_points
            return True

    def take_mana(self, mana_amount):
        if mana_amount + self.mana > self.max_mana:
            self.mana = self.max_mana
            return True
        else:
            self.mana += mana_amount
            return True

    def equip(self, weapon):
        if not isinstance(weapon, Weapon):
            return False
        self.weapon = weapon

    def learn(self, spell):
        if not isinstance(spell, Spell):
            return False
        self.spell = spell

    def attack(self, by):
        if by != "magic" or by != "weapon":
            return False
        if self.weapon == None or self.spell == None:
            return 0
        if by == "weapon":
            return self.weapon.power
        if by == "spell" and self.can_cast():
            return self.spell.power









