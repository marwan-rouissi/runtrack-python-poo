# job 4

listeValeur = [5, 8, 2, 3, 1, 10, 25, 4]

def valeurMax(listeValeur):

    # si la longueur de la liste est inférieure ou égale à 1, retourner le 1er item de la liste
    if len(listeValeur) <= 1:
        return listeValeur[0]
    
    # sinon
    else:
        # valeur actuelle = entre item 1 et 2 de la liste
        valeurActuelle = max(listeValeur[0], listeValeur[1])
        # liste réduite = valeur précédente + reste de la liste
        listeReduite = [valeurActuelle] + listeValeur[2:]
        # retourner la liste réduite
        return valeurMax(listeReduite)
    
print(f"La valeur max de la liste {listeValeur}\nest: {valeurMax(listeValeur)}")