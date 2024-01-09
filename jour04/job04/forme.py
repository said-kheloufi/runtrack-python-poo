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
    
forme1 = Rectangle(15,41)

print(forme1.aire())