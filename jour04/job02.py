# job 2

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

    def __init__(self, age=14):
        super().__init__(age)
    
    # méthode aller en cours
    def allerEnCours(self):
        print("Je vais en cours")
    
    # méthode pour afficher l'age
    def AffichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    # création d'un objet Porfesseur

    def __init__(self, age, matiereEnseignée):
        super().__init__(age)
        self.__matiereEnseignée = matiereEnseignée
    
    # méthode enseigner
    def enseigner(self):
        print("Le cours va commencer.")

# Instancier un objet professeur
professeur = Professeur(40, "Maths")
# Instancier un objet eleve
eleve = Eleve()

# Imprimer et vérifier le bon fonctionnement des méthodes
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
professeur.bonjour()
professeur.enseigner()