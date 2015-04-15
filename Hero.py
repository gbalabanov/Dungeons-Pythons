class Hero:

    def __init__(self, name, title, health, mana, mana_regen, weapon = None, spell = None):
        self.name = name
        self.title = title
        self.health = health
        self.mana_regen = mana_regen
        self.max_health = health
        self.max_mana = mana

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health
