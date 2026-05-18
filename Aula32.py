import random

vetor = [random.randint(1, 50) for i in range(10)]

pares = 0
impares = 0

for numero in vetor:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1


print(f"Vetor gerado: {vetor}\n")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")