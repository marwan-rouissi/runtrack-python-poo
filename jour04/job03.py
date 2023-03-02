# job 3

class Rectange:
    # création d'un objet Rectangle

    def __init__(self, longueur, largeur):
        self.__longueur = longueur 
        self.__largeur = largeur

    # méthode pour calculer le périmètre du rectangle 
    def périmètre(self):
        res = (self.__longueur + self.__largeur) * 2
        return res
    
    # méthode pour calculer la surface du rectangle
    def surface(self):
        res = self.__longueur * self.__largeur
        return res
    
    # getter
    def getLongueur(self):
        return self.__longueur
    def getLargeur(self):
        return self.__largeur
    # setter
    def setLongueur(self, longueur):
        self.__longueur = longueur
    def setLargeur(self, largeur):
        self.__largeur = largeur
    
class Parallélépipède(Rectange):
    # création d"un objet Parallélépipède (fille de Rectangle)

    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    # méthode pour calculer le volume du parallélépipède
    def volume(self):
        self.__longueur = self.getLongueur()
        self.__largeur = self.getLargeur()
        res = self.__longueur * self.__largeur * self.hauteur
        return res
    
    def getHauteur(self):
        return self.hauteur

# instancier un objet rectangle

rectangle = Rectange(30, 10)
print(f"Pour un rectangle de longueur {rectangle.getLongueur()} et de largeur {rectangle.getLargeur()}")
print(f"le périmètre: {rectangle.périmètre()}")
print(f"la surface: {rectangle.surface()}")
print("-----------------------------------------------------------")
parallélépipède = Parallélépipède(60, 20, 15)
print(f"Pour un parallélépipède de longueur {parallélépipède.getLongueur()}, de largeur {parallélépipède.getLargeur()} et de hauteur {parallélépipède.getHauteur()}")
print(f"le périmètre: {parallélépipède.périmètre()}")
print(f"la surface: {parallélépipède.surface()}")
print(f"le volume: {parallélépipède.volume()}")