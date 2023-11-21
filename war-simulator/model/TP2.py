from TP1 import Weapon
from TP1 import Lance_missiles
from TP1 import
class Vessel:

    def __init__(self,coordinates,max_hits,weapon):
        self.coordinates =coordinates
        self.max_hits = max_hits
        self.weapon = weapon

 class Cruiser(Vessel):

    def __init__(self, coordinates, max_hits, weapon):
        super().__init__(coordinates, max_hits, weapon)
        self.max_hits = 6
        self.weapon = Lance_missiles()

 class Submarine(Vessel):

    def __init__(self, coordinates, max_hits, weapon):
        super().__init__(coordinates, max_hits, weapon)
        self.max_hits = 2
        self.weapon = Lance_torpilles()



    def go_to(self,x,y,z):

        self.coordinates = a,b,c

    def fire_at(self,x,y,z):
        if max_hits == 0:
            raise Exception("DestroyedError")




class DestroyedError(Exception):
    def __str__(self):
        return "DetroyedError"







