import math
class Weapon:
    def __int__(self,ammunitions,range):
        self.ammunitions = ammunitions
        self.range = range

    def fire_at(self,x,y,z):
        if z == 0:
            if math.sqrt(x**2+y**2) > range:
                ammunitions -=1
                raise Exception("OutOfRangeError")
        if z > 0:
            if math.sqrt(x ** 2 + y ** 2) > range:

                ammunitions -=1
                raise Exception("OutOfRangeError")

        if z < 0:


            if math.sqrt(x ** 2 + y ** 2) > range:



                ammunitions -= 1
                raise Exception("OutOfRangeError")

class Lance_missiles(Weapon):
    def __init__(self,ammunitions,range,z):
        super().__init__(ammunitions,range)
        ammunitions = 50
        range = 100
        self.z = z

class Lance_missiles_antiair(Weapon):
    def __init__(self,ammunitions,range,z):
        super().__init__(ammunitions,range)
        ammunitions = 40
        range = 20
        self.z = z

class Lance_torpilles(Weapon):
    def __init__(self,ammunitions,range,z):
        super().__init__(ammunitions,range)
        self.z = z
        ammunitions = 24
        range = 40

a = Lance_torpilles(50,35,2)
a.fire_at(3,5,2
          )







