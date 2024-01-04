class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def get_nom_ville(self):
        return self.__nom
    
    def get_habitants(self):
        return self.__habitants
    def set_habitants(self, nouvelle_valeur):
        self.__habitants = nouvelle_valeur

        
class Personne:
    def __init__(self, nom, age, Ville):
        self.__nom = nom
        self.__age = age
        self.__Ville = Ville

    def get_nom_pesonne(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__Ville

    def ajouterPopulation(self):
        ville_personne = self.__Ville
        nombre_habitant = ville_personne.get_habitants()
        ville_personne.set_habitants(nombre_habitant + 1)
        return ville_personne.get_habitants()

objet1 = Ville("Paris", 1000000)
objet2 = Ville("Marseille", 861635)

personne1 = Personne("john", 45, objet1)
personne2 = Personne("Myrtille", 4, objet1)
personne3 = Personne("Chloe", 18, objet2)

print("population de la ville de ", objet1.get_nom_ville(), "est de ", objet1.get_habitants(), "habitants")
print("population de la ville de ", objet2.get_nom_ville(), "est de ", objet2.get_habitants(), "habitants")

print("Mise a jour de population de la ville de ", personne1.get_ville().get_nom_ville(), "est de ", personne1.ajouterPopulation(), "habitants")
print("Mise a jour de population de la ville de ", personne2.get_ville().get_nom_ville(), "est de ", personne2.ajouterPopulation(), "habitants")
print("Mise a jour de population de la ville de ", personne3.get_ville().get_nom_ville(), "est de ", personne3.ajouterPopulation(), "habitants")
