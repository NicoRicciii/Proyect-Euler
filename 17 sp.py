from num2words import num2words

# podemos, usando la librería "num2words", contar
# la cantidad total de letras en la variable "cantidad"

cantidad = 0
for i in range(1, 1001):

    s = num2words(i)
    for m in range(0, len(s)):

        if not(s[m] == " " or s[m] == "-"):
            cantidad += 1

print(cantidad)