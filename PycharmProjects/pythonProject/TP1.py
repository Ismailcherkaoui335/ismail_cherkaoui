import math

class Weapon:
    def __init__(self, ammunitions, weapon_range):
        self.ammunitions = ammunitions
        self.weapon_range = weapon_range

    def fire_at(self, x, y, z):
        if z == 0:
            if math.sqrt(x**2 + y**2) > self.weapon_range:
                self.ammunitions -= 1
                raise Exception("OutOfRangeError")
        if z > 0:
            if math.sqrt(x**2 + y**2) > self.weapon_range:
                self.ammunitions -= 1
                raise Exception("OutOfRangeError")
        if z < 0:
            if math.sqrt(x**2 + y**2) > self.weapon_range:
                self.ammunitions -= 1
                raise Exception("OutOfRangeError")

class Lance_missiles(Weapon):
    def __init__(self, ammunitions, weapon_range, z):
        super().__init__(ammunitions, weapon_range)
        self.z = z

class Lance_missiles_antiair(Weapon):
    def __init__(self, ammunitions, weapon_range, z):
        super().__init__(ammunitions, weapon_range)
        self.z = z

class Lance_torpilles(Weapon):
    def __init__(self, ammunitions, weapon_range, z):
        super().__init__(ammunitions, weapon_range)
        self.z = z

a = Lance_torpilles(50, 35, 2)
a.fire_at(3, 5, 2)
