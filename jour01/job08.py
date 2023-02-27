# job 8

class Cercle:
    # création d'un objet Cercle

    # création d'un constructeur de l'objet
    def __init__(self, rayon):
        self.rayon = rayon

    # méthode pour chager de rayon
    def changerRayon(self, rayon):
        self.rayon = rayon

    # méthode pour afficher les info du cercle
    def afficherInfo(self):
        print("Cercle de rayon:", self.rayon)
        print("Aire:", self.air)
        print("Circonférence:", self.circ)
        print("Diametre:", self.diam)

    # méthode pour determiner la circonférence du cercle
    def circonférence(self):
        self.circ = self.diam * 3.14
        return self.circ

    # méthode pour déterminer l'aire du cercle
    def aire(self):
        self.air = self.rayon * self.rayon * 3.14
        # return self.air

    # méthode pour déterminer le diametre du cercle
    def diametre(self):
        self.diam = self.rayon * 2
        return self.diam

# Instancier le cercle
c1 = Cercle(4)

# Appeler les méthodes et Imprimer les infos
c1.aire()
c1.diametre()
c1.circonférence()
c1.afficherInfo()
print("")
c1.changerRayon(7)
c1.aire()
c1.diametre()
c1.circonférence()
c1.afficherInfo()