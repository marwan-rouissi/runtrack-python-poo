# job 3

class Livre:
    # création d'un objet Livre

    def __init__(self, titre, auteur, nombrePages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePages = nombrePages
        
        self.__disponible = True

    # méthode pour afficher les attributs
    def getInfo(self):
        print("Le titre du livre:", self.__titre)
        print("L'auteur du livre:", self.__auteur)
        print("Le nombre de pages:", self.__nombrePages)

    # méthode pour modifier le titre
    def setTitre(self, titre):
        self.__titre = titre
    
    # méthode pour modifier l'auteur
    def setAuteur(self, auteur):
        self.__auteur = auteur
    
    # méthode pour modifier le nombre de pages
    def setNombrePages(self, nombrePages):
        if type(nombrePages) == int:
            if nombrePages > 0:
                self.__nombrePages = nombrePages
    
    # méthode pour vérifier si la disponibilité du livre
    def vérification(self):
        if self.__disponible == True:
            return True
        else:
            return False
    
    # méthode pour emprunter le livre
    def emprunter(self):
        if self.vérification():
            self.__disponible = False
            return True
        else:
            return False
        
    # méthode pour rendre le livre
    def rendre(self):
        if self.vérification() == False:
            self.__disponible = True
            return True
        else:
            return False

# Instancier un livre
rhinoceros = Livre("Rhinoceros", "Ionesco", 200)

# Imprimer les méthodes 

print("dispo:", rhinoceros.vérification())
print("emprunter:", rhinoceros.emprunter())
print("dispo:", rhinoceros.vérification())
print("rendre:", rhinoceros.rendre())
print("dispo:", rhinoceros.vérification())