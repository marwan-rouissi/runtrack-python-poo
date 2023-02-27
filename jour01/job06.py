# job 6

class Animal:
    # création d'un objet Animal

    # création d'un constructeur de l'objet
    def __init__(self):
        self.age = 0
        self.prenom = ""
        # print("L'age de l'animal", self.age, "ans")
    
    # méthode pour vieillir l'âge de l'animal
    def vieillir(self):
        self.age += 1
        return self.age
    
    # méthode pour nommer l'animal
    def nommer(self, prenom):
        self.prenom = prenom

# Instancier l'animal
ani = Animal()

# Imprimer l'âge de l'animal
print("L'age de l'animal", ani.age, "ans")

# Appeler la methode vieillir()
ani.vieillir()

# Imprimer l'âge de l'animal
print("L'age de l'animal", ani.age, "ans")

# Appeler la méthode nommer()
ani.nommer("Luna")

# Imprimer le nom de l'animal
print("L'animal se nomme", ani.prenom)