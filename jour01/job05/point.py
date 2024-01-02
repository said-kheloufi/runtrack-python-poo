class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoint(self):
        print("coordonnees des sont : ", self.x, ",", self.y  )

    def afficherX(self):
        print("x est ",self.x)

    def afficherY(self):
        print("y est ",self.y)

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

point1 = Point(3, 5)

point1.afficherLesPoint()

point1.afficherX()

point1.afficherY()

point1.changerX(8)

point1.changerY(12)

point1.afficherLesPoint()
