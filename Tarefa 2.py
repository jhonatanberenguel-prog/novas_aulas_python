import random


def tamanhomatriz():
    n = random.randint(2, 10)  
    return n

n = tamanhomatriz()
print(f"Tamanho da matriz = {n}x{n}")

matriz = []
for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(random.randint(0, 50))

for linha in matriz:
    print(linha)
print("--------------\n")

diagonal = []
soma = 0

for i in range(n):
    coluna = n - 1 - i 
    numeros = matriz[i][coluna]
    diagonal.append(numeros)
    soma += numeros

print(f"Os números da diagonal secundária: {diagonal}")

