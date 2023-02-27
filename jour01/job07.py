# job 7 

class Personnage:
    # création d'un objet Personnage

    # création d'un constructeur de l'objet
    def __init__(self, x, y):
        self.x = x 
        self.y = y

        self.plateau = [[1,2,3],[4,5,6],[7,8,9]]
        self.plateauXY = self.plateau[self.x][self.y]

    # méthode pour déplacer le personnage vers la gauche
    def gauche(self):
        self.y -= 1
        self.plateauXY = self.plateau[self.x][self.y]

    # méthode pour déplacer le personnage vers la droite
    def droite(self):
        self.y += 1
        self.plateauXY = self.plateau[self.x][self.y]

    # méthode pour déplacer le personnage vers le bas
    def bas(self):
        self.x += 1
        self.plateauXY = self.plateau[self.x][self.y]

    # méthode pour déplacer le personnage vers le haut
    def haut(self):
        self.x -= 1
        self.plateauXY = self.plateau[self.x][self.y]

    # méthode pour retourner les coordonnées sous forme d'un tuple
    def position(self):
        pos = (self.x, self.y)
        return pos

# Instancier le personnage
pers = Personnage(2,1)

# Imprimer la position initiale du personnage
print(pers.position())

# Appeler la méthode pour déplacer le personnage vers la gauche
pers.gauche()

# Imprimer la nouvelle position du personnage
print(pers.position())

# Appeler la méthode pour déplacer le personnage vers le haut
pers.haut()

# Imprimer la nouvelle position du personnage
print(pers.position())