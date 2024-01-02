class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        print("l'age de l'animal", self.age , "ans")
        print("l'age de l'animal", self.age + 1, "ans")

    def nommer(self):
        print("l'animal se nomme ", self.prenom)


animal1 = Animal(1, "luna")

animal1.vieillir()

animal1.nommer()


