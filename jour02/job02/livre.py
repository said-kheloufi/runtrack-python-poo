class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

    def get_titre(self):
        return self.__titre
    def set_titre(self, nouvelle_valeur):
        self.__titre = nouvelle_valeur

    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, nouvelle_valeur):
        self.__auteur = nouvelle_valeur

    def get_pages(self):
        return self.__pages
    def set_pages(self, nouvelle_valeur):
        if isinstance(nouvelle_valeur, int) and nouvelle_valeur > 0:
            self.__pages = nouvelle_valeur
        else :
            print("le nombre doit être un nombre entier positif")


livre1 = Livre("one piece", "eichiro oda", 193)

print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_pages())

livre1.set_titre("naruto")
livre1.set_auteur("Masashi Kishimoto")
livre1.set_pages(2.5)

print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_pages())