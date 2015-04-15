class Spell:

    def __init__(self, name, power, mana_cost, cast_range):
        self.name = name
        self.power = power
        self.mana_cost = mana_cost
        self.cast_range = cast_range

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

    def atack(self, by):
        if by != "magic" or by != "weapon":
            return False
        if self.weapon == None or self.spell == None:
            return 0
        if by == "weapon":
            return self.weapon.power
        if by == "spell" and self.can_cast():
            return self.spell.power


