def AreaRectangulo (a,b):
    area = a*b
    return area

def PerimetroRectangulo (a,b):
    perimetro = (2*a)+(2*b)
    return perimetro

def Pizza(sabor):
    print(f"Quiero una pizza de {sabor}")

a = input("Introduzca sabor: ")
b= input("Introduzca otro sabor: ")

Pizza(a)
Pizza(b)

rectangulo1 = AreaRectangulo(4,2)

print(rectangulo1)

