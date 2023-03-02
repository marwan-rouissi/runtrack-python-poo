# job 3 

class Tache:
    # création d'un objet Tache

    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

    def getStatut(self):
        return self.statut

    def setStatut(self, statut):
        self.statut = statut

class ListeDeTaches:
    # création d'un objet Liste de Taches

    def __init__(self):

        self.taches = []

    # méthode pour ajouter une tache à la liste
    def ajouterTache(self, tache):
        tache = {"Titre":tache.titre, "Description": tache.description,"Statut": tache.statut}
        self.taches.append(tache)

    # méthode pour supprimer une tache de la liste
    def supprimerTache(self, tache):
        tache = {"Titre":tache.titre, "Description": tache.description,"Statut": tache.statut}
        self.taches.remove(tache)

    # méthode pour changer l'état de la tache
    def marquerCommeFinie(self, tache):
        tache = {"Titre":tache.titre, "Description": tache.description,"Statut": tache.statut}
        for i in self.taches:
            if tache == i:
                tache["Statut"] = "terminée"

                i.update(tache)

        

    # méthode pour afficher la liste de taches
    def afficherListe(self):

        for tache in self.taches:
            print("tache:", tache["Titre"], ", description:", tache["Description"], ", statut:", tache["Statut"])
            # print(f"Tâche: {self.taches [0]["Titre"]}")

    # méthode à revoir
    def filtrerListe(self, statut):

        for tache in self.taches:
            if tache["Statut"] == statut:
                print("tache:", tache["Titre"], ", description:", tache["Description"], ", statut:", tache["Statut"])
            else:
                pass

# Instancier des taches

tache_1 = Tache("Réviser", "cours de maths", "à faire")
tache_2 = Tache("Sport", "Aller à la salle", "à faire")
tache_3 = Tache("Manger", "Aller manger", "à faire")

# Instancier une liste de tache

listTache = ListeDeTaches()

# Imprimer et vérifier le bon fonctionnement des méthodes

print("-----------------------------------------------------------------")
print("Ajouter 3 taches")
print("-----------------------------------------------------------------")

listTache.ajouterTache(tache_1)
listTache.ajouterTache(tache_2)
listTache.ajouterTache(tache_3)
listTache.afficherListe()
print("-----------------------------------------------------------------")
print("Supprimer tache 1")
print("-----------------------------------------------------------------")
listTache.supprimerTache(tache_1)
listTache.afficherListe()
print("-----------------------------------------------------------------")
print("Marquer tache 3 comme terminée")
print("-----------------------------------------------------------------")
listTache.marquerCommeFinie(tache_3)
listTache.afficherListe()
print("-----------------------------------------------------------------")
print("Filter taches à faire")
print("-----------------------------------------------------------------")
listTache.filtrerListe("à faire")
print("-----------------------------------------------------------------")
print("Filter taches terminée")
print("-----------------------------------------------------------------")
listTache.filtrerListe("terminée")
print("-----------------------------------------------------------------")