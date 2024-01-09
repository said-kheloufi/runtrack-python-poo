class Vehicule:
    def __init__(self, marque, modèle, année, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    def informationVehicule(self):
        print("Marque = ",self.marque)
        print("Model = ",self.modèle)
        print("année = ",self.année) 
        print("prix = ", self.prix)

    def demarrer(self):
        print("attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modèle, année, prix, portes=4):
        super().__init__(marque, modèle, année, prix)
        self.portes = portes 

    def informationVehicule(self):
        return super().informationVehicule(), print("nombre de portes = ", self.portes)
         
    def demarrer(self):
        return super().demarrer()
    
class Moto(Vehicule):
    def __init__(self, marque, modèle, année, prix, roue=2):
        super().__init__(marque, modèle, année, prix)
        self.roue = roue 

    def informationVehicule(self):
        return super().informationVehicule(), print("nombre de roue = ", self.roue)
    
    def demarrer(self):
        return super().demarrer()


voiture1 = Voiture("Mercedes", "classe A", 2020, 18500, 4)
moto1 = Moto("yamaha", "1200 Vmax", 1987, 4500)

voiture1.informationVehicule()
voiture1.demarrer()
moto1.informationVehicule()
moto1.demarrer()