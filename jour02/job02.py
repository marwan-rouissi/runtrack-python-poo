# job 2 

class Livre:
    # création d'un objet Livre

    def __init__(self, titre, auteur, nombrePages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePages = nombrePages

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

# Instancier un livre
rhinoceros = Livre("Rhinoceros", "Ionesco", 200)

# Appeler les méthodes 
rhinoceros.getInfo()
rhinoceros.setNombrePages(100)
print("")
rhinoceros.getInfo()