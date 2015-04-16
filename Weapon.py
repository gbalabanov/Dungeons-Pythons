class Weapon:

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __eq__(self, other):
        return self.power == other.power

    def __ge__(self, other):
        return self.power > other.power
