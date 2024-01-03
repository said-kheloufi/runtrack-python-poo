class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

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
        else:
            raise ValueError("Le nombre de pages doit être un nombre entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():  
            print("Emprunt du livre en cours.")
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.verification():  
            print("Le livre a été rendu.")
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté.")

livre1 = Livre("One Piece", "Eiichiro Oda", 193)

print("Avant emprunt :")
print("Disponibilité :", livre1.verification())
livre1.emprunter()

print("\nAprès emprunt :")
print("Disponibilité :", livre1.verification())
livre1.emprunter()
livre1.rendre()

print("\nAprès rendu :")
print("Disponibilité :", livre1.verification())
