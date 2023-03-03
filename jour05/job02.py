# job 2

def calc(x, n):
    # condtion de break 
    if n < 1:
        return 1
    
    # retourne le produit de x par la fonction (calculer puissance) avec exposant décrémenté de 1 
    else:
        return x*calc(x, n-1)

# demander à l'utilisatieur d'entrer un entier
print("Entrer un nombre entier:")
x = int(input())

# demander à l'utilisatieur d'entrer un exposant
print("Entrer un exposant:")
n = int(input())

# Imprimer le résultat
print("Le résultat est:", calc(x, n))