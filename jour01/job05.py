# job 5

class Point:
    # création d'un objet Point

    # création du constructeur de l'objet
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # méthode pour afficher les coordonnées 
    def afficherLesPoints(self):
        print("les coordonnées sont: " + str(self.x) + ":" + str(self.y))

    # méthode pour afficher le x
    def afficherX(self):
        print("x: "+ str(self.x))

    # méthode pour afficher le y
    def afficherY(self):
        print("y: "+ str(self.y))

    # méthode pour changer le x
    def changerX(self, x):
        self.x = x

    # méthode pour changer le y
    def changerY(self, y):
        self.y = y

# Instancier le point
Pt = Point(5, 10)

# Appel des méthodes
Pt.afficherLesPoints()
Pt.afficherX()
Pt.afficherY()
Pt.changerX(10)
Pt.changerY(20)
Pt.afficherLesPoints()