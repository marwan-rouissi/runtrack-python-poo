# job 1

class Ville:
    # création d'un objet Ville

    def __init__(self, nom, nombreHabitants):
        self.__nom = nom
        self.__nombreHabitants = nombreHabitants
    
    # méthode pour récupérer le nom de la ville
    def getNom(self):
        return self.__nom

    # méthode pour récupérer le nombre d'habitants
    def getNombreHabitants(self):
        return self.__nombreHabitants

    # méthode pour changer le nom de la ville
    def setNom(self, nom):
        self.__nom = nom

    # méthode pour changer le nombre d'habitants
    def setNombreHabitants(self, nombreHabitants):
        self.__nombreHabitants = nombreHabitants
    
class Personne:
    # création d'un objet Personne

    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    # méthode pour modifier le nombre d'habitants
    def ajouterPopulation(self, ville):
        add = ville.getNombreHabitants() + 1
        # print(add)
        ville.setNombreHabitants(add)

# Instancier un objet Paris
Paris = Ville("Paris", 1000000)

# Imprimer le nombre d'habitnant de Paris
print(f"Population de la ville de {Paris.getNom()}: {Paris.getNombreHabitants()} habitants" )

# Instancier un objet Marseille
Marseille = Ville("Marseille", 861635)

# Imprimer le nombre d'habitnant de Marseille
print(f"Population de la ville de {Marseille.getNom()}: {Marseille.getNombreHabitants()} habitants" )

# Instancier les 3 objets demandés

John = Personne("John", 45, Paris)
John.ajouterPopulation(Paris)
Myrtille = Personne("Mystille", 4, Paris)
Myrtille.ajouterPopulation(Paris)
Chloé = Personne("Chloé", 18, Marseille)
Chloé.ajouterPopulation(Marseille)

# MAJ Imprimer le nombre d'habitnant de Paris
print(f"Mise a jour de la population de la ville de {Paris.getNom()}: {Paris.getNombreHabitants()} habitants" )
# MAJ Imprimer le nombre d'habitnant de Marseille
print(f"Mise a jour de la population de la ville de {Marseille.getNom()}: {Marseille.getNombreHabitants()} habitants" )