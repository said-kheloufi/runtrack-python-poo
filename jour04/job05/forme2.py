import math

class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur) :
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
class Cercle(Forme):
    def __init__(self, radius) :
        super().__init__()
        self.radius = radius

    def aire(self):
        return math.pi * self.radius ** 2
    
forme1 = Rectangle(15,41)
forme2 = Cercle(20)

print(forme1.aire())
print(forme2.aire())