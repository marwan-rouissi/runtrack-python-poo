# job 3

mot = "j'entends"

def lenword(mot):
    # condition de break
    if mot == "":
        return 0
    # retourne la somme des éléments de ma chaine de caractère (en ométtant l'index 0) + 1
    else:
        return 1+lenword(mot[1:])
    
print(f"Dans le mot: {mot}")
print(f"Il y a {lenword(mot)} caractère(s)" )