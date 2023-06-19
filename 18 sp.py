# para cada número x, el camino máximo para llegar a x, 
# es el máximo de los dos posibles caminos anteriores a él (que llegan
# hasta los dos números encima de x), más x

# primero creamos "mtr" (matriz triangular) que va a tener
# los números dados en el enunciado

# y podemos crear una nueva matriz "mcm" (matriz caminos máximos), 
# que vaya fila por fila haciendo este algoritmo

f = open(r"p018.maximumpathsum.txt")
liststring = f.read()
list = liststring.split()

mtr = [[0 for i in range(0, 15)] for j in range(0, 15)]
mcm = []

# agregamos varias listas con 0s en mcm, 
# hacemos que mcm[0][0] sea igual a mtr[0][0] 
# ya que el primer camino ese número solamente,
# y en mtr agregamos los números dados en el enunciado
for i in range(1, 16):
    mcm.append([0 for a in range(0, 15)])

    for b in range(0, i):
        mtr[i-1][b] = list[0]
        list.remove(list[0])
mcm[0][0] = mtr[0][0]

# hacemos el algoritmo explicado anteriormente
for m in range(1, 15):

    mcm[m][0] = int(mcm[m-1][0]) + int(mtr[m][0])
    for n in range(1, m+1):
        mcm[m][n] = max(int(mcm[m-1][n]), int(mcm[m-1][n-1])) + int(mtr[m][n])

print(max(mcm[14]))