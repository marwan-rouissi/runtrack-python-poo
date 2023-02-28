# job 5

class Voiture:
     # création d'un objet Voiture

    def __init__(self, marque, modèle, année, kilométrage):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.en_marche = False
        self.__reservoir = 50
    
### méthodes pour afficher les attributs demandés
    def getMarque(self):
        return self.__marque
    def getModèle(self):
        return self.__modèle
    def getAnnée(self):
        return self.__année
    def getKilomètrage(self):
        return self. __kilométrage
    
### méthodes pour modifier les attibuts demandés 
    def setMarque(self, marque):
        self.__marque = marque 
    def setModèle(self, modèle):
        self.__modèle = modèle
    def setAnnée(self, année):
        self.__année = année
    def setKilomètrage(self, kilomètrage):
        self.__kilométrage = kilomètrage

    # méthode pour démarrer la voiture
    def demarrer(self):
        self.__verifier_plein()
        if self.__verifier_plein() > 5:
            self.en_marche = True
            print("la voiture a démarré")
        else:
            print("vérifier le reservoir")
    
    # méthode pour arrêter la voiture
    def arreter(self):
        self.en_marche = False

    # méthode pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir

# Instancier la voiture
voiture = Voiture("Chevrolet", "Impala", 1967, 50000)

# Imprimer les infos de la voiture / démarrage et arrêt
print("La marque:", voiture.getMarque())
print("Le modèle:", voiture.getModèle())
print("L'année:", voiture.getAnnée())
print("Le kilomètrage:", voiture.getKilomètrage(), "km")
print("")
print("démarrage de la voiture")
voiture.demarrer()
print("l'état en marche est", voiture.en_marche)
print("Arrêt de la voiture")
voiture.arreter()
print("l'état en marche est", voiture.en_marche)
print("")