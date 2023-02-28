# job 6 

class Commande:
    # création de l'objet Commande

    def __init__(self):
        self.__numCommande = 0
        self.__listePlats = []
        self.__statutCommande = ""

    def ajouterPlat(self, plat, prix):
        self.__statutCommande = "en cours"
        commande = {"plat" : plat, "prix" : prix, "statut": self.__statutCommande}
        self.__listePlats.append(commande)

    def annulerCommande(self):
        self.__statutCommande = "annulée"

    def __calculerTotal(self):
        pass

    def afficherTotal(self):
        self.__statutCommande = "terminée"
        self.__numCommande += 1
        print("Commande numéro:", self.__numCommande)
        
        for i in self.__listePlats:
            i = 0
            print("le plat commandé(s):", self.__listePlats[i]["plat"])
            print("Montant à payer", self.__listePlats[i]["prix"], "€")


    def calculerTVA(self):
        pass

# Instancier un objet commande 
commande = Commande()

# Ajouter une 1ere commande
commande.ajouterPlat("Lasagne", 12)
# Ajouter une 2e commande
commande.ajouterPlat("Pizza", 10)
# commande.ajouterPlat("Lasagne", 12)

# Afficher le total (test)
commande.afficherTotal()