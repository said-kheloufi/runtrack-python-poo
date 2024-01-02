class Produit:
    def __init__(self, nom="",prixHT=0,TVA=0):
        self.nom =nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def afficher(self):
        print("Informations du produit:")
        print("Nom :", self.nom)
        print("Prix HT :", self.prixHT, "€")
        print("TVA :", self.TVA, "%")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA
    
produit1 = Produit("Produit1", 50, 20)
produit2 = Produit("Produit2", 30, 10)

produit1.afficher()
produit2.afficher()

prix_ttc_produit1 = produit1.CalculerPrixTTC()
prix_ttc_produit2 = produit2.CalculerPrixTTC()


print("Prix TTC du produit 1 :", prix_ttc_produit1, "€")
print("Prix TTC du produit 2 :", prix_ttc_produit2, "€")

produit1.modifierNom("NouveauProduit1")
produit2.modifierPrix(40)

print("Nouveau nom du produit 1 :", produit1.getNom())
print("Nouveau prix HT du produit 2 :", produit2.getPrixHT())