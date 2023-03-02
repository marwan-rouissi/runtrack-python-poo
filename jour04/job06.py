# job 6

class Vehicule:
    # création d'un objet Vehicule

    def __init__(self, marque, modèle, année, prix) -> None:
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    # méthode pour afficher les infos générales du véhicule
    def informationsVehicule(self):
        print(f"marque: {self.marque}")
        print(f"modèle: {self.modèle}")
        print(f"année: {self.marque}")
        print(f"prix: {self.prix} €")
        
    # méthode pour démarre le véhicule
    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    #création d'un objet Voiture (fille de Vehicule)

    def __init__(self, marque, modèle, année, prix, portes=4) -> None:
        super().__init__(marque, modèle, année, prix)
        self.portes = portes
    
    # méthode info surchargée pour Voiture
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"portes: {self.portes}")
    
    # méthode demmarer surchagée et personnalisée pour la classe Voiture
    def demarrer(self):
        super().demarrer()
        print("Attachez votre ceinture.")

# Instancier un objet voiture
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
# Imprimer les infos
print("-----------------------------------------------------")
voiture.informationsVehicule()
voiture.demarrer()

class Moto(Vehicule):
    # création d'un objet Moto (fille de Vehicule)

    def __init__(self, marque, modèle, année, prix, roue=2) -> None:
        super().__init__(marque, modèle, année, prix)
        self.roue = roue

    # méthode info surchargée pour Moto
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"roues: {self.roue}")

    # méthode demmarer surchagée et personnalisée pour la classe Moto
    def demarrer(self):
        super().demarrer()
        print("Mettez votre casque.")

# Instancier un objet moto
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)

# Imprimer les infos
print("-----------------------------------------------------")
moto.informationsVehicule()
moto.demarrer()
print("-----------------------------------------------------")