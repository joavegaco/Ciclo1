import random

m = int(input("filas "))
n = int(input("columnas "))

mat =[]*(m)
for i in range (m+1):
    a = [0]*(n+1)
    mat.append(a)

for i in range(m+1):
    for j in range(1,n+1):
        mat[i][j] = random.randint(1,9)



def sumarFilas(m,n):
    for i in range(m + 1):
        s = 0
        for j in range(1, n + 1):
            s = s + mat[i][j]
    print("El total de la fila ", i,"  es: ", s)

def sumarColumnas(m,n):
    for i in range(n + 1):
        s = 0
        for j in range(1, m + 1):
            s = s + mat[j][i]
    print("El total de la columna ", i,"  es: ", s)

sumarFilas(m,n)
sumarColumnas(m,n)

print(mat)
