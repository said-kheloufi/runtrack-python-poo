class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    def set_longueur(self, nouvelle_valeur):
        self.__longueur = nouvelle_valeur
    
    def get_largeur(self):
        return self.__largeur
    def set_largeur(self, nouvelle_valeur):
        self.__largeur = nouvelle_valeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur
    

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        return self.longueur * self.largeur * self.hauteur
    
objet1 = Rectangle(10, 15)

print(objet1.get_largeur())
print(objet1.get_longueur())
print(objet1.perimetre())
print(objet1.surface())

objet1.set_largeur(25)
objet1.set_longueur(30)

print(objet1.get_largeur())
print(objet1.get_longueur())
print(objet1.perimetre())
print(objet1.surface())