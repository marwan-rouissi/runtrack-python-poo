# Job 3

class Operation:
    # création d'un objet Operation

    # création du constructeur de l'objet
    def __init__(self):
        self.nombre1 = 5
        self.nombre2 = 10

        # imprimer les attributs défi
        print("Le nombre1 est", self.nombre1)
        print("Le nombre2 est", self.nombre2)
    
    # méthode pour additionner "nombre1" et "nombre2"
    def addition(self):
        result = self.nombre1 + self.nombre2

        # imprimer le resultat
        print("la somme des deux est:", result)

# instancier la classe 
Op = Operation()

# appel de la méthode 
Op.addition()