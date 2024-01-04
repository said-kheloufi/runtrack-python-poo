class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self, taches=[]):
        self.taches = taches

    def ajouterTache(self, nouvelle_tache):
        self.taches.append(nouvelle_tache)

    def supprimerTache(self, tache_remove):
        try:
            self.taches.remove(tache_remove)
            print("Tache supprimer")
        except ValueError:
            print("Tache non trouver dans la liste.")

    def marquerCommeFinie(self, tache_fini):
        for tache in self.taches:
            if tache == tache_fini:
                tache.statut = "fini"
                print("tache : ", tache.titre, "fini")
                return
            print("Tache non trouver dans la liste.")

    def afficherListe(self):
        return [tache.titre for tache in self.taches]

    def filtreListe(self, statut):
        return [tache.titre for tache in self.taches if tache.statut == statut]

tache1 = Tache("menage", "passer l'aspirateur", "en cours")
tache2 = Tache("vaisselle", "faire la vaisselle", "en cours")
tache3 = Tache("cours", "faire les cours", "fini")

liste_taches = ListeDeTaches([tache1, tache2, tache3])

print("Liste initiale des tâches :", liste_taches.afficherListe())

nouvelle_tache = Tache("sport", "aller à la salle de sport", "à faire")
liste_taches.ajouterTache(nouvelle_tache)

print("Liste après ajout d'une tâche :", liste_taches.afficherListe())

liste_taches.supprimerTache(tache2)

print("Liste après suppression d'une tâche :", liste_taches.afficherListe())

liste_taches.marquerCommeFinie(tache1)

print("Liste après modification du statut d'une tâche :", liste_taches.afficherListe())

print("Liste des tâches à faire :", liste_taches.filtreListe("à faire"))
