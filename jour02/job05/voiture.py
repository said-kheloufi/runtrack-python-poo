class Voiture :
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_modele(self):
        return self.__modele
    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_annee(self):
        return self.__annee
    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def get_kilometrage(self):
        return self.__kilometrage
    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def get_en_marche(self):
        return self.__en_marche
    def set_en_marche(self, nouvelle_valeur):
        self.__en_marche = nouvelle_valeur
   
    def get_reservoir(self):
        return self.__reservoir
    def set_reservoir(self, nouvelle_valeur):
        self.__reservoir = nouvelle_valeur

    def demarrer(self):
        if self.__verifier_plein():
            self.set_en_marche(True)
            print("La voiture a démarré.")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    def arreter(self):
        self.set_en_marche(False)
        print("la voiture est arreter")

    def __verifier_plein(self):
        return self.__reservoir > 5
    
voiture1 = Voiture("Dodge","challenger SRT HELLCAT",2022,20000)

print(voiture1.get_marque())
print(voiture1.get_modele())
print(voiture1.get_annee())
print(voiture1.get_kilometrage(),"km")
voiture1.set_reservoir(2)
voiture1.demarrer()
voiture1.arreter()


