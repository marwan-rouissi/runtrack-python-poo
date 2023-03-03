# job 1

# fonction pour calculer la factorielle
def fact(n):
    # condition de break
    if n < 1:
        return 1
    # retourne le produit de n par n décrémenté de 1
    else:
        return n * fact(n-1)
        
# demander à l'utilisatieur d'entrer un entier
print("Entrer un nombre entier:")
n = int(input())

# Imprimer le résultat
print("La factorielle est:", fact(n))