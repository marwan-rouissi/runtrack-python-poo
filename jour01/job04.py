# job 4

class Personne:
    # création d'un objet Personne

    # création du constructeur de l'objet
    def __init__(self, nom, prenom):

        self.nom = nom
        self.prenom = prenom

    # méthode pour se Presenter
    def SePresenter(self):

        print("Je suis" , self.prenom , self.nom)

# Instancier les personnes
Personne1 = Personne("Doe", "John")
Personne2 = Personne("Dupond", "Jean")

# Appeler la méthode SePresenter
Personne1.SePresenter()
Personne2.SePresenter()