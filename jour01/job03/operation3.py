class Operation:
    def __init__(self, nombre1=0,nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("le resultat de l'addition est ", resultat)

operation_instance = Operation(12, 3)

operation_instance.addition()