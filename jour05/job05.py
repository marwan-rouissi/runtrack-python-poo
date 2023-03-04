# job 5

n = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

termeSuivant = 10

def fibonacci(n):
    # condition de break
    # les 2 premiers termes de la suite valent 1 chacun
    if n <= 2:
        return 1
    
    else:
        # retourner la somme de l'index précédent et de celui qui le précéde
        return (fibonacci(n-1) + fibonacci(n-2))

print(f"Les 9 premiers termes de la suite de Fibonacci sont:\n{n}")
print(f"Le {termeSuivant}e terme sera: {fibonacci(termeSuivant)}")