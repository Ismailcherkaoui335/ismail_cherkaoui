import math
class NoAmmunitionError(Exception):
    def __str__(self):
        return "NoAmmunitionError"
class OutOfRangeError(Exception):
    def __str__(self):
        return "OutOfRangeError"

class DestroyedError(Exception):
    def __str__(self):
        return "DetroyedError"

class Weapon:
    def __init__(self, ammunitions, weapon_range):
        self.ammunitions = ammunitions
        self.weapon_range = weapon_range
    def fire_at(self, x, y, z):
        try:
            if self.ammunitions <= 0:
                raise NoAmmunitionError
            if math.sqrt(x**2 + y**2 + z**2) > self.weapon_range:
                self.ammunitions -= 1
                raise OutOfRangeError
        except NoAmmunitionError as e:
            print(e)
        except OutOfRangeError as e:
            print(e)

class Lance_missiles(Weapon):
    def __init__(self):
        super().__init__(50, 100)

class Lance_missiles_antiair(Weapon):
    def __init__(self):
        super().__init__(40, 20)
class Lance_torpilles(Weapon):
    def __init__(self):
        super().__init__(24, 40)

a = Lance_torpilles()
for i in range(a.ammunitions+1):
    print(a.ammunitions)
    a.fire_at(1, 53, 9)
class Vessel:

    def __init__(self,coordinates,max_hits,weapon):
        self.coordinates =coordinates
        self.max_hits = max_hits
        self.weapon = weapon

    def fire_at(self,x,y,z):
        try:
            if self.max_hits == 0:
                raise DestroyedError



class Cruiser(Vessel):

    def __init__(self, coordinates, max_hits, weapon):
        super().__init__(coordinates, max_hits, weapon)
        self.max_hits = 6
        self.weapon = Lance_missiles()

class Submarine(Vessel):

    def __init__(self, coordinates):
        super().__init__(coordinates, 2, Lance_torpilles())



class Fregate(Vessel):

    def __init__(self, coordinates):
        super().__init__(coordinates, 5, Lance_missiles_antiair())

class Destroyer(Vessel):

    def __init__(self, coordinates):
        super().__init__(coordinates, 4, Lance_torpilles())

class Aircraft(Vessel):

    def __init__(self, coordinates):
        super().__init__(coordinates, 1, Lance_torpilles())

