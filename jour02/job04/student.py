class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__student_eval()

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            self.__level = self.__student_eval()
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    def get_total_credits(self):
        return self.__credits

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print("Nom =", self.__nom)
        print("Prénom =", self.__prenom)
        print("Id =", self.__numero_etudiant)
        print("Niveau =", self.__level)

john_doe = Student("John", "Doe", 145)

john_doe.add_credits(10)
john_doe.add_credits(15)
john_doe.add_credits(5)

john_doe.student_info()
