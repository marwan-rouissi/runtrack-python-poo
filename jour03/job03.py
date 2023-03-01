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
        tache = [tache.titre, tache.description, tache.statut]
        self.taches.append(tache)

    # méthode pour supprimer une tache de la liste
    def supprimerTache(self, tache):
        tache = [tache.titre, tache.description, tache.statut]
        self.taches.remove(tache)

    # méthode pour changer l'état de la tache
    def marquerCommeFinie(self, tache):
        tache.description = "terminer"

        tache.setStatut(tache.description)
        # print(tache.description)
        

    # méthode pour afficher la liste de taches
    def afficherListe(self):

        for i in range(len(self.taches)):
                print(f"Tâche: {self.taches[i][0]}. Description: {self.taches[i][1]}")

    # méthode à revoir
    def filtrerListe(self, statut):
        tache_encours = []
        tache_faites = []

        
        for i in range(len(self.taches)):
            
                # print(i)
                print(f"Tâche: {self.taches[i][0]}. Description: {self.taches[i][1]}, état: {self.taches[i][2]}")
                print('liste en cours', tache_encours)
                print('liste terminer', tache_faites)
        
# Instancier des taches

tache_1 = Tache("Réviser", "cours de maths", "à faire")
tache_2 = Tache("Sport", "Aller à la salle", "à faire")
tache_3 = Tache("Manger", "Aller manger", "à faire")

listTache = ListeDeTaches()

print("-----------------------------------------------------")
print("Ajouter 3 taches")
print("-----------------------------------------------------")

listTache.ajouterTache(tache_1)
listTache.ajouterTache(tache_2)
listTache.ajouterTache(tache_3)
listTache.afficherListe()
print("-----------------------------------------------------")
print("Supprimer tache 1")
print("-----------------------------------------------------")
listTache.supprimerTache(tache_1)
listTache.marquerCommeFinie(tache_3)

# listTache.filtrerListe("en cours")

listTache.afficherListe()