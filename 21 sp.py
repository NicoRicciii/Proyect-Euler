from math import floor

# en la lista sumadiv, vamos a guardar el d() de 
# cada número, sumando cada divisor i a cada múltiplo de i 

sumadiv = [0 for k in range(0, 10000)]
for i in range(1, 10000):
    for j in range(2, floor(9999/i)+1):
        sumadiv[j*i] += i

# para cada k, verificamos si k es un número amicable
# para eso tiene que pasar que: 
# d(k) no sea igual a k, pero d(d(k)) = k, para que
# haya efectivamente una pareja de números distintos entre sí
# pero además, esa pareja debería ser de números <= 10000

sumaamicable = 0
for k in range(1, 10000):
    if sumadiv[k] != k and sumadiv[k] <= len(sumadiv):
        if sumadiv[sumadiv[k]] == k:
            sumaamicable += k

print(sumaamicable)

