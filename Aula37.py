import random

M = [[1,2,3],[4,5,6]]
print(M)
M1 = [0] * 3
print(M[1][1]) #primeira linha e primeiro elemento

for i in range(3):
    M1[i] = [0] * 3
print(M1)

M2 = [10,20,30],[40,50,60]
for i in range(2): #LINHA
    for j in range(3): #coluna
        M2[i][j] = random.randint(0,50)
print(M2)

M3= []
for i in range(3):
    M3.append([])
    for j in range(3):
        M3[i].append(random.randint(0,50))
print(M3)