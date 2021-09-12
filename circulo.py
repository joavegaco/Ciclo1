class Circulo():
    def __init__(self,radio):
        self.radio = radio
        self.pi = 3.14

    def area_circulo(self):
        area_circulo = self.pi * self.radio ** 2
        return area_circulo

    def perimetro_circulo(self):
        perimetro_circulo = 2 * self.pi * self.radio
        return perimetro_circulo