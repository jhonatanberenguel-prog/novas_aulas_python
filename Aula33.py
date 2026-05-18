import random

vetor = [random.randint(1, 50) for i in range(20)]
print(vetor)
print("-" * 10)

soma = 0
quantidade = 0

for numero in vetor:
    if numero % 2 == 0:
        soma += numero
        quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"O total de números pares foi: {quantidade}")
    print(f"A média total dos números pares foi de: {media}")

else:
    print("Nenhum número par foi encontrado.")