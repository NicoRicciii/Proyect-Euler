# podemos simplemente abrir el archivo txt

f = open(r"p013_largesum.txt")
string = f.read()

# sumar todos los números en el archivo, y ver cuáles son 
# los primeros 10 números en la suma

lista = string.split()
suma = 0
for i in range(0, len(lista)):
    suma += int(lista[i])  

print(suma)
