import math
class Weapon:
    def __int__(self,ammunitions,range):
        self.ammunitions = ammunitions
        self.range = range

    def fire_at(self,x,y,z):
        if self.ammunitions == 0:
            raise Exception("NoAmmunitionError")

        if  (math.sqrt(x**2+y**2) > self.range):

            self.ammunitions -= 1
            raise Exception("OutOfRangeError")

missile_antisurface = Weapon(50,100)
missile_anti-air = Weapon(20,40)
missile_antisurface = Weapon(40,24)





