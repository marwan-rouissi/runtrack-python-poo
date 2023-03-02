# job 4

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

# Instancier un rectangle
rectangle = Rectangle(30, 15)
print("-----------------------------------------------------")
print(f"Pour un rectangle de largeur {rectangle.largeur} et de hauteur {rectangle.hauteur}")
# Imprimer l'aire
print(f" l'aire est de {rectangle.aire()}")
print("-----------------------------------------------------")