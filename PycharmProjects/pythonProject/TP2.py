from TP1 import Weapon
class Vessel:

    def __init(self,coordinates,max_hits,weapon):
        self.coordinates =coordinates
        self.max_hits = max_hits
        self.weapon = weapon


    def go_to(self,x,y,z):
