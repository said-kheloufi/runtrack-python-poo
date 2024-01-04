class CompteBancaire:
    def __init__(self, compte, nom, prenom, solde, decouvert=False):
        self.__compte = compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def get_compte(self):
        return self.__compte
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
    
    def get_decouvert(self):
        return self.__decouvert
    
    def afficher_solde(self):
        print("Solde actuel :", self.__solde)

    def afficher(self):
            print("Numéro de compte :", self.__compte)
            print("Nom :", self.__nom)
            print("Prénom :", self.__prenom)
            print("Solde actuel :", self.__solde)

    def versement(self, montant):
            self.__solde += montant
            print("Versement de", montant, "effectué.")
        
    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print("Retrait de ", montant, "effectué. Nouveau solde : ", self.__solde)
        else:
            print("Opération non autorisée. Solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            montant_agios = abs(self.__solde) * taux_agios / 100
            self.__solde -= montant_agios
            print("Des agios de ",montant_agios, "ont été appliqués. Nouveau solde : ", self.__solde)

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement de ", montant, "effectué vers le compte ", compte_destinataire.get_compte())
        else:
            print("Opération non autorisée. Solde insuffisant.")

compte1 = CompteBancaire("123456789", "Doe", "John", 1000.0, decouvert=True)
compte2 = CompteBancaire("987654321", "Smith", "Alice", -500.0, decouvert=True)

compte1.afficher()
compte2.afficher()

compte1.virement(compte2, 700.0)

compte1.afficher()
compte2.afficher()