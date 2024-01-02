class Personne:
    def __init__(self, prenom="", nom=""):
        self.prenom = prenom
        self.nom = nom

    def SePresenter(self):
        print("je suis",self.prenom,self.nom)

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupond")
personne3 = Personne("Edward", "Kenway")

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()
