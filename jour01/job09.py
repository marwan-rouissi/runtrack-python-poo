# job 9

class Produit:
    # création d'un objet Produit

    # création d'un constructeur de l'objet
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    # méthode pour calculer le prix TTC
    def CalculerPrixTTC(self):
        self.prixTTC = self.prixHT * (1 + (self.TVA/100))
        return self.prixTTC

    # méthode pour afficher les info sous forme de liste
    def afficher(self):
        all = [self.nom, self.prixHT, self.TVA, self.prixTTC]
        return all

    # méthode pour modifier le nom du produit
    def modifierNomProduit(self, nom):
        self.nom = nom
    
    # méthode pour modifier le prix du produit
    def modifierPrixProduit(self, prix):
        self.prixHT = prix

    # méthode pour récupérer le nom du produit
    def infoNomProduit(self):
        nomProduit = "Nom du produit: " + self.nom
        return nomProduit

    # méthode pour récupérer le prix du produit HT
    def infoPrixProduitHT(self):
        prixHT = "Prix HT: " + str(self.prixHT) + " €"
        return prixHT

    # méthode pour récupérer le prix du produit TTC
    def infoPrixProduitTTC(self):
        prixTTC = "Prix TTC: " + str(self.prixTTC) + " €"
        return prixTTC


# Instancier le produit 
jeu = Produit("Hogwarts Legacy", 60, 20)
meuble = Produit("Table", 50, 20)

# Appeler la méthode pour calculer le prix TTC des produits
jeu.CalculerPrixTTC()
meuble.CalculerPrixTTC()

# Imprimer les infos à afficher
print(jeu.afficher())
print(jeu.infoNomProduit())
print(jeu.infoPrixProduitHT())
print(jeu.infoPrixProduitTTC())

# print d'espacement
print("")

# Imprimer les infos à afficher
print(meuble.afficher())

print(meuble.infoNomProduit())
print(meuble.infoPrixProduitHT())
print(meuble.infoPrixProduitTTC())

# Appeler la méthode pour changer le nom des produits
jeu.modifierNomProduit("Red Dead Redemption 2")
meuble.modifierNomProduit("chaises")
# Appeler la méthode pour changer le prix des produits
jeu.modifierPrixProduit(60)
meuble.modifierPrixProduit(30)
# Appeler la méthode pour calculer le prix TTC du produit
jeu.CalculerPrixTTC()
meuble.CalculerPrixTTC()

# print d'espacement
print("")

# Imprimer les infos à afficher
print(jeu.afficher())

print(jeu.infoNomProduit())
print(jeu.infoPrixProduitHT())
print(jeu.infoPrixProduitTTC())

# print d'espacement
print("")

# Imprimer les infos à afficher
print(meuble.afficher())

print(meuble.infoNomProduit())
print(meuble.infoPrixProduitHT())
print(meuble.infoPrixProduitTTC())