# job 5

class Forme:
    # création d'un objet Forme

    def __init__(self) -> None:
        pass

    def aire(self):
        return 0

class Rectangle(Forme):
    # création d'un objet Rectangle

    def __init__(self, largeur, hauteur) -> None:
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur
    
    # méthode pour calculer et retourner l'aire
    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    # création d'un objet Cercle (fille de Forme)

    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def aire(self):
        return 3.14 * (self.radius*self.radius)

# Instancier des objet rectangle et cercle
rectangle = Rectangle(20, 10)
cercle = Cercle(15)

print("-----------------------------------------------------")
print(f"Pour un rectangle de largeur {rectangle.largeur} et de hauteur {rectangle.hauteur}")
# Imprimer l'aire
print(f" l'aire est de {rectangle.aire()}")
print("-----------------------------------------------------")
print(f"Pour un cercle de rayon {cercle.radius}")
# Imprimer l'aire
print(f" l'aire est de {cercle.aire()}")
print("-----------------------------------------------------")