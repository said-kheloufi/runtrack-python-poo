class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def __calculer_total(self):
        total = 0
        for plat, details in self.__plats_commandes.items():
            total += details["prix"]
        return total

    def ajouter_plat(self, nom_plat, prix_plat):
        if self.__statut_commande == "en cours":
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"Plat ajouté : {nom_plat}, Prix : {prix_plat}€")
        else:
            print("Impossible d'ajouter un plat à une commande terminée ou annulée.")

    def annuler_commande(self):
        if self.__statut_commande == "en cours":
            self.__statut_commande = "annulée"
            print("Commande annulée.")
        else:
            print("Impossible d'annuler une commande terminée ou déjà annulée.")

    def afficher_commande(self):
        total_commande = self.__calculer_total()
        print(f"Commande #{self.__numero_commande}")
        print("Plats commandés:")
        for plat, details in self.__plats_commandes.items():
            print(f"{plat} - Prix : {details['prix']}€ - Statut : {details['statut']}")
        print(f"Total à payer : {total_commande}€")

    def calculer_tva(self, taux_tva):
        total_commande = self.__calculer_total()
        tva = total_commande * (taux_tva / 100)
        return tva


commande1 = Commande(1)

commande1.ajouter_plat("Pizza Margherita", 10)
commande1.ajouter_plat("Pâtes Carbonara", 15)

commande1.afficher_commande()

tva_calculée = commande1.calculer_tva(10)
print(f"TVA calculée : {tva_calculée}€")

commande1.annuler_commande()
commande1.afficher_commande()
