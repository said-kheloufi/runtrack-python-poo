class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("hello")

    def modifierAge(self, nouveau_age=0):
        self.age = nouveau_age

class Eleve(Personne):
    def allerEnCours(self):
        print("je vais en cours")

    def afficherAge(self):
        print("j'ai ", self.age, "ans")

class Professeur:
    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("le cours va commencer")

eleve1 = Eleve()

eleve1.afficherAge()