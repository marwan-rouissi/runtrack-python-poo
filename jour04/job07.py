# job 7

import random

class Carte:
    # création d'un objet Carte

    def __init__(self) -> None:
        self.valeur = {"AS": 11, "figure": 10}
        self.couleur = ["coeur", "pique", "trefle", "carreau"]


class Jeu(Carte):
    # création d'un objet Jeu (fille de Carte)

    def __init__(self) -> None:
        super().__init__()
        self.paquet = []
        self.jeu = []

        for carte in range(1, 14):
            if carte == 11:
                carte = "valet"
            if carte == 12:
                carte = "dame"
            if carte == 13:
                carte = "roi"
            for couleur in self.couleur:
                self.paquet.append({"valeur": carte, "couleur": couleur})
        # print(self.paquet)
        
    
    # méthode pour recevoir une (ou plusieurs) carte(s) supplémentaires
    def prendre(self, nombre_de_cartes=1):
        self.nombre_de_cartes = nombre_de_cartes
        
        # paquetJeu = self.paquet
        
        jeu = random.choices(self.paquet, k=nombre_de_cartes)
        # if starter not in jeu:
        self.jeu.append(jeu)
        for element in self.paquet:
            if element in jeu:
                self.paquet.remove(element)
                print("élément à supprimer", element)
        # paquet.remove(starter)
        print("--------------------------------------------------------------")
        print("random: ",jeu)
        print("--------------------------------------------------------------")
        print("jeu:", self.jeu)
        print("--------------------------------------------------------------")
        print("paquet", self.paquet)
        print("--------------------------------------------------------------")

    # méthode pour laisser le tour au croupier
    def passer(self):
        pass

    def commencerJeu(self):
        paquetJeu = self.paquet
        

class Joueur(Jeu):
    # création d'un objet Joueur (fille de Jeu)

    def __init__(self) -> None:
        super().__init__()


jeu = Jeu()

croupier = Joueur()
joueur_1 = Joueur()

joueur_1.prendre()

croupier.prendre()