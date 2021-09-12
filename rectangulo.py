class Rectangulo():
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def perimetro(self):
        perimetro = 2*self.largo + 2*self.ancho
        return perimetro

    def area(self):
        area = self.largo * self.ancho
        return area
