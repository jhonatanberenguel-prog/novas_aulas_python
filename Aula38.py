import random
matriz = []

for i in range(3):
    matriz.append([])
    
    for j in range(3):
        matriz[i].append(random.randint(0,50))


print(matriz)

diag1 = (matriz [0][0])
diag2 = (matriz [1][1])
diag3 = (matriz [2][2])

print(diag1)
print(diag2)
print(diag3)

soma = diag1 + diag2 + diag3
print(f"{diag1} + {diag2} + {diag3} = {soma}")

diag4 = (matriz [0][2])
diag5 = (matriz [1][1])
diag6 = (matriz [2][0])

print(diag4)
print(diag5)
print(diag6)

soma2 = diag4 + diag5 + diag6
print(f"{diag4} + {diag5} + {diag6} = {soma2}")

a11 = (matriz [0][0])
a22 = (matriz [1][1])
a33 = (matriz [2][2])

a12 = (matriz [0][1])
a23 = (matriz [1][2])
a31 = (matriz [2][0])

a13 = (matriz [0][2])
a21 = (matriz [1][0])
a32 = (matriz [2][1])

a31 = (matriz [2][0])

determinante = a11 * a22 * a33 + a12 * a23 * a31 + a13 * a21 * a32 - a33 * a21 * a12 - a32 * a23 * a11 - a31 * a22 * a13

print(determinante)







