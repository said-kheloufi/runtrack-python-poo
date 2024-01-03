class Rectangle :
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
        


rectange = Rectangle(10,5)

print(rectange.get_longueur())
print(rectange.get_largeur())

rectange.set_longueur(20)
rectange.set_largeur(10)

print(rectange.get_longueur())
print(rectange.get_largeur())