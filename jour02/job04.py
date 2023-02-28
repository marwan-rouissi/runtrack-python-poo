# job 4

class Student:
    # création d'un objet Student

    def __init__(self, nom, prénom, id):
        self.nom = nom
        self.prénom = prénom
        self.id = id
        self.nombre_crédits = 0
        self.__level = self.__studentEval()
    
    # méthode pour ajouter un nombre de crédits
    def add_credits(self, crédits):
        if crédits > 0:
            self.nombre_crédits += crédits
            self.__level = self.__studentEval()
    
    # méthode pour évaluer l'élève
    def __studentEval(self):
        if self.nombre_crédits >= 90:
            return "Excellent."
        if self.nombre_crédits >= 80:
            return "Tès bien."
        if self.nombre_crédits >= 70:
            return "Bien."
        if self.nombre_crédits >= 60:
            return "Passable."
        else:
            return "Insuffisant."
        
    # méthode pour imprimer les infos demandées
    def studentInfo(self):
        print("Nom =", self.nom)
        print("Prénom =", self.prénom)
        print("id =", self.id)
        print("Niveau =", self.__level)

# Instancier un objet étudiant John Doe (numEtudiant: 145)
student = Student("Doe", "John", 145)

# Appeler la méthode add_credits
student.add_credits(30)
# Imprimer le résultat attendu
print("Le nombre de credits de", student.prénom, student.nom, "est de", student.nombre_crédits, "points")
student.studentInfo()
print("")
# Appeler la méthode add_credits
student.add_credits(55)
# Imprimer le résultat attendu
print("Le nombre de credits de", student.prénom, student.nom, "est de", student.nombre_crédits, "points")
student.studentInfo()
print("")
# Appeler la méthode add_credits
student.add_credits(90)
# Imprimer le résultat attendu
print("Le nombre de credits de", student.prénom, student.nom, "est de", student.nombre_crédits, "points")
student.studentInfo()