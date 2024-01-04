class Joueur:
    def __init__(self, nom, numero, position, buts_marques=0 , passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = buts_marques
        self.passes_decisives = passes_decisives
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges


    def marquer_un_but(self):
        self.buts_marques += 1

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        print("Statistiques de ", self.nom, ("Numéro", self.numero, "Position", self.position))
        print("Buts marqués : ", self.buts_marques)
        print("Passes décisives effectuées : ", self.passes_decisives)
        print("Cartons jaunes reçus : ",self.cartons_jaunes)
        print("Cartons rouges reçus : ",self.cartons_rouges)

class Equipe:
    def __init__(self, nom, list_joueur=[]):
        self.nom = nom
        self.list_joueur = list_joueur

    def ajouterJoueur(self,joueur):
        self.list_joueur.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.list_joueur:
            joueur.afficher_statistiques()
        
    def mettreAJourStatistiquesJoueur(self, num_joueur, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.list_joueur:
            if joueur.numero == num_joueur:
                joueur.marquer_un_but(buts)
                joueur.effectuer_une_passe_decisive(passes)
                joueur.recevoir_un_carton_jaune(jaunes)
                joueur.recevoir_un_carton_rouge(rouges)
                return
        print("Joueur non trouvé dans l'équipe.")

joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar", 11, "Milieu")

equipe1 = Equipe("Barça", [joueur1, joueur3])
equipe2 = Equipe("Real Madrid", [joueur2])

print("Statistiques initiales des joueurs :")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

print("Simuler un match...")
joueur1.marquer_un_but()
joueur2.recevoir_un_carton_jaune()
joueur3.effectuer_une_passe_decisive()

print("Statistiques après le match :")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()