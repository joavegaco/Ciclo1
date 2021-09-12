import numpy

a = numpy.zeros((4,4))

print(a)

a = int(input("Introduzca el primer nùmero "))
b = int(input("Introduzca el segundo nùmero "))
c = int(input("Introduzca el tercer nùmero "))

if (a+b) == c:
    print(f"La suma de {a}+{b} es {c}")
elif (b+c) == a:
    print(f"La suma de {b}+{c} es {a}")
elif (c+a) == b:
    print(f"La suma de {c}+{a} es {b}")
else:
    print(f"Los elementos no se pueden sumar")