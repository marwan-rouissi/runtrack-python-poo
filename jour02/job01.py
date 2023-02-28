# job 1

class Rectangle:
    # création d'un objet Rectangle

    def __init__(self, longueur, largueur):
        self.__longueur = longueur
        self.__largeur = largueur

    def getParametres(self):
        print("la longueur est de:", self.__longueur)
        print("la largeur est de:", self.__largeur)
    
    def setParametres(self):
        self.__longueur = input("Choisir la longueur: ")
        self.__largeur = input("Choisir la largeur: ")

        
# Instancier le rectangle
rect = Rectangle(10, 5)

# Apeller les méthodes de l'objet Rectangle
# afficher parametres
rect.getParametres()
# modifier parametres
rect.setParametres()
# afficher nouveaux parametres
rect.getParametres()