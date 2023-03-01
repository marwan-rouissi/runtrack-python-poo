# job 2

class CompteBancaire:
    # création d'un objet Compte Bancaire

    def __init__(self, numCompte, nom, prénom, solde):
        self.__numCompte = numCompte
        self.__nom = nom
        self.__prénom = prénom
        self.__solde = solde
        self.découvert = True
    
    # méthode pour afficher les détails du compte
    def afficher(self):
        print(f"Num Compte: {self.__numCompte}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prénom}")
        print(f"Solde: {self.__solde}", "€")

    # méthode pour afficher le solde du compte
    def afficherSolde(self):
        return self.__solde

    # méthode pour verser un montant spécifique au compte
    def versement(self, montant):
        self.__solde += montant

    # méthode pour retirer un montant spécifique du compte
    def retrait(self, montant_à_retirer):
        if montant_à_retirer < self.__solde and self.découvert:
                self.__solde -= montant_à_retirer
                self.__solde -= self.agios()
                print("Solde actuel:", self.afficherSolde(), "€")
        else:
            self.__solde = self.__solde
            print("solde insufisant.")
    
    # méthode pour déduire les agios
    def agios(self):
    
        # res = montant * nombre de jours écoulé en étant à découvert
        # res = res * taux d'intêret (en %)
        # res = res / nombre de jours dans l'année (365)

        res = self.__solde * 10 # nombre de jours passé à découvert
        res = res * (20/100) # taux à 20 %
        res = res / 365 # nombre de jours dans l'année
        # print(res, "€")
        return res

    # méthode pour virer de l'argent d'un compte à un autre
    def virement(self, compteCréditeur, compteCrédité, montant):
        if compteCréditeur.__solde > montant or compteCréditeur.découvert:
            compteCréditeur.__solde -= montant
            compteCrédité.__solde += montant
            print("Virement effectué.")
        else:
            print("Virement impossible, solde insufisant.")


# Instancier un premier compte
compte_1 = CompteBancaire(124578, "Doe", "John", 1300)

# Imprimer et vérifier le bon fonctionnement des méthodes
compte_1.afficher()
print("")
print("Retrait de 500 €")
compte_1.retrait(500)
print("")
print("Retrait de 1000 €")
compte_1.retrait(1000)
print("")

# Instancier un deuxième compte
compte_2 = CompteBancaire(784512, "Smith", "Joe", 2600)

# Imprimer et vérifier le bon fonctionnement des méthodes
compte_2.virement(compte_2, compte_1, 500)

compte_1.afficher()
print("")
compte_2.afficher()