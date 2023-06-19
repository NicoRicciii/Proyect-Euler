#abro un archivo con los 400 números, y los hago una lista de 400 objetos

f = open(r"p011_productonagrid.txt")
liststring = f.read()
list = liststring.split()

#hago una matriz, con 20 listas de 20 items c/u
matriz = []
for a in range(0, 20):
    matriz.append([list[a*20 + b] for b in range(0, 20)])

#agrego en una lista todos los posibles productos, separando en casos: horizontales, verticales, diagonales

productos = []

#horizontales
for a in range(0, 20):
    for b in range(0, 17):
        x = int(matriz[a][b])*int(matriz[a][b+1])*int(matriz[a][b+2])*int(matriz[a][b+3])
        productos.append(x)

#verticales
for a in range(0, 17):
    for b in range(0, 20):
        x = int(matriz[a][b])*int(matriz[a+1][b])*int(matriz[a+2][b])*int(matriz[a+3][b])
        productos.append(x)

#diagonales1
for a in range(0, 17):
    for b in range(0, 17):
        x = int(matriz[a][b])*int(matriz[a+1][b+1])*int(matriz[a+2][b+2])*int(matriz[a+3][b+3])
        productos.append(x)

#diagonales2
for a in range(0, 17):
    for b in range(3, 20):
        x = int(matriz[a][b])*int(matriz[a+1][b-1])*int(matriz[a+2][b-2])*int(matriz[a+3][b-3])
        productos.append(x)

print(max(productos))
