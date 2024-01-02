class Operation:
    def __init__(self, nombre1=0,nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation_instance = Operation(12, 3)

resultat = "le nombre1 est {} le nombre2 est {}".format(operation_instance.nombre1, operation_instance.nombre2)

print(resultat)