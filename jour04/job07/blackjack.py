from random import shuffle

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        return paquet

    def melanger_paquet(self):
        shuffle(self.paquet)

    def tirer_carte(self):
        if self.paquet:
            return self.paquet.pop()
        else:
            print("Le paquet est vide.")

class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.mains_joueur = []
        self.main_croupier = []

    def distribuer_cartes(self):
        for _ in range(2):
            self.mains_joueur.append(self.jeu.tirer_carte())
            self.main_croupier.append(self.jeu.tirer_carte())

    def calculer_total(self, main):
        total = 0
        as_count = 0

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                as_count += 1
            else:
                total += int(carte.valeur)

        for _ in range(as_count):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1

        return total

    def afficher_mains(self):
        print("Main du joueur:")
        for carte in self.mains_joueur:
            print(carte)
        print("Total:", self.calculer_total(self.mains_joueur))

        print("\nMain du croupier:")
        for carte in self.main_croupier:
            print(carte)
        print("Total:", self.calculer_total(self.main_croupier))

    def joueur_gagne(self):
        total_joueur = self.calculer_total(self.mains_joueur)
        total_croupier = self.calculer_total(self.main_croupier)

        return total_joueur <= 21 and (total_joueur > total_croupier or total_croupier > 21)

    def joueur_perd(self):
        return self.calculer_total(self.mains_joueur) > 21

    def croupier_doit_tirer(self):
        return self.calculer_total(self.main_croupier) < 17

    def jouer(self):
        self.jeu.melanger_paquet()
        self.distribuer_cartes()
        self.afficher_mains()

        while not self.joueur_perd():
            action = input("Voulez-vous tirer une carte ? (Oui/Non): ").lower()

            if action == 'oui':
                self.mains_joueur.append(self.jeu.tirer_carte())
                self.afficher_mains()

                if self.joueur_perd():
                    print("Dommage, vous avez dépassé 21. Vous avez perdu.")
                    return 

            elif action == 'non':
                break
            else:
                print("Réponse invalide. Veuillez répondre 'Oui' ou 'Non'.")

        while self.croupier_doit_tirer():
            self.main_croupier.append(self.jeu.tirer_carte())

        self.afficher_mains()

        if self.joueur_gagne():
            print("Félicitations, vous avez gagné!")
        else:
            print("Dommage, vous avez perdu.")

if __name__ == "__main__":
    partie_blackjack = Blackjack()
    partie_blackjack.jouer()
