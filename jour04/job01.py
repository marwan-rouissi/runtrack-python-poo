# job 1

class Personne:
    # création d'un objet Personne

    def __init__(self, age=14):
        self.age = age
    
    # méthode pour afficher l'age
    def afficherAge(self):
        print(f"Age: {self.age} ans")

    # méthode pour dire bonjour
    def bonjour(self):
        print("Hello")
    
    # méthode pour modifier l'age
    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    # création d'un objet Eleve (fille de Personne)

    def __init__(self):
        super().__init__()
    
    # méthode aller en cours
    def allerEnCours(self):
        print("Je vais en cours")
    
    # méthode pour afficher l'age
    def AffichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur:
    # création d'un objet Porfesseur

    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée
    
    # méthode enseigner
    def enseigner(self):
        print("Le cours va commencer.")

# Instancier un objet personne et un objet eleve
personne = Personne()
eleve = Eleve()

# Afficher l'age

eleve.afficherAge()
eleve.AffichageAge()