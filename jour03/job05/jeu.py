class Personnage:
    def __init__(self, nom="", vie=0):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire, points):
        adversaire.vie -= points
        print(self.nom, " attaque ", adversaire.nom, " et lui inflige ", points, "points de dégâts. Vie de", adversaire.nom, ":", adversaire.vie)

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        niveaux_possibles = ["Facile", "Moyen", "Difficile"]

        print("Choisissez le niveau de difficulté:")
        for i, niveau in enumerate(niveaux_possibles, 1):
            print(f"{i}. {niveau}")


        while True:
            try:
                choix = int(input("Entrez le numéro du niveau : "))
                if 1 <= choix <= len(niveaux_possibles):
                    self.niveau = niveaux_possibles[choix - 1]
                    print("Vous avez choisi le niveau : ",self.niveau)
                    break
                else:
                    print("Choix invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                print("Veuillez entrer un numéro.")

    def lancerJeu(self):
        niveaux = {"Facile": 50, "Moyen": 75, "Difficile": 100}

        if self.niveau in niveaux:
            points_vie_joueur = points_vie_ennemi = niveaux[self.niveau]
            joueur = Personnage("Joueur", points_vie_joueur)
            ennemi = Personnage("Ennemi", points_vie_ennemi)

            print(f"Jeu lancé avec un joueur de niveau {self.niveau} ({joueur.vie} points de vie) et un ennemi ({ennemi.vie} points de vie).")

            while joueur.vie > 0 and ennemi.vie > 0:
                joueur.attaquer(ennemi, 20)
                ennemi.attaquer(joueur, 15)

                self.verifierSante(joueur)
                self.verifierSante(ennemi)

            self.determinerGagnant(joueur, ennemi)

    def verifierSante(self, personnage):
        print(f"Points de vie de {personnage.nom}: {personnage.vie}")
        if personnage.vie <= 0:
            print(f"{personnage.nom} a perdu la partie.")

    def determinerGagnant(self, joueur, ennemi):
        if joueur.vie > ennemi.vie:
            print(f"{joueur.nom} a gagné la partie!")
        elif joueur.vie < ennemi.vie:
            print(f"{ennemi.nom} a gagné la partie!")
        else:
            print("La partie est un match nul.")

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()