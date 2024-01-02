import math

class Cercle:
    def __init__(self, rayon=0):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfo(self):
        print("un cercle qui a un rayon de ", self.rayon)

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)
    
    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfo()
cercle2.afficherInfo()

print("Cercle 1 - Circonférence:", cercle1.circonference())
print("Cercle 1 - Diamètre:", cercle1.diametre())
print("Cercle 1 - Aire:", cercle1.aire())

print("Cercle 2 - Circonférence:", cercle2.circonference())
print("Cercle 2 - Diamètre:", cercle2.diametre())
print("Cercle 2 - Aire:", cercle2.aire())


cercle1.changerRayon(12)
cercle2.changerRayon(20)

print("Cercle 1 - Circonférence:", cercle1.circonference())
print("Cercle 1 - Diamètre:", cercle1.diametre())
print("Cercle 1 - Aire:", cercle1.aire())

print("Cercle 2 - Circonférence:", cercle2.circonference())
print("Cercle 2 - Diamètre:", cercle2.diametre())
print("Cercle 2 - Aire:", cercle2.aire())

cercle1.afficherInfo()
cercle2.afficherInfo()