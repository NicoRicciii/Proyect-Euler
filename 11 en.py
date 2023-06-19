# firstly we can open the txt file in order to read it 

f = open(r"p011_productonagrid.txt")
liststring = f.read()
list = liststring.split()

# we can make a matrix with 20 lists with 20 items each one
matrix = []
for a in range(0, 20):
    matrix.append([list[a*20 + b] for b in range(0, 20)])

# we add all of the possible products in a single list, separating between 
# horizontal, vertical and diagonal products

productos = []

# horizontal products
for a in range(0, 20):
    for b in range(0, 17):
        x = int(matrix[a][b])*int(matrix[a][b+1])*int(matrix[a][b+2])*int(matrix[a][b+3])
        productos.append(x)

# vertical products
for a in range(0, 17):
    for b in range(0, 20):
        x = int(matrix[a][b])*int(matrix[a+1][b])*int(matrix[a+2][b])*int(matrix[a+3][b])
        productos.append(x)

# diagonal products
for a in range(0, 17):
    for b in range(0, 17):
        x = int(matrix[a][b])*int(matrix[a+1][b+1])*int(matrix[a+2][b+2])*int(matrix[a+3][b+3])
        productos.append(x)

for a in range(0, 17):
    for b in range(3, 20):
        x = int(matrix[a][b])*int(matrix[a+1][b-1])*int(matrix[a+2][b-2])*int(matrix[a+3][b-3])
        productos.append(x)

# we print the largest number of this list
print(max(productos))
