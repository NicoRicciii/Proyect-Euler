# we can simply open the txt file

f = open(r"p013_largesum.txt")
string = f.read()

# sum all of the numbers
# and check the first 10 numbers in the sum

lista = string.split()
suma = 0
for i in range(0, len(lista)):
    suma += int(lista[i])  

print(suma)
