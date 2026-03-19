n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))
base = int(input("Ingrese el número base: "))

matriz = []
contador = 1

for i in range(n):
    fila = []
    for j in range(m):
        fila.append(base * contador)
        contador += 1
    matriz.append(fila)

for fila in matriz:
    print(fila)
    