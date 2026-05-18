import random

vetor = [random.randint(1, 50) for i in range(20)]
print(vetor)
print("-" * 10)

usuario = int(input("Digite um número de 1 a 50:\n"))

multiplos = []

for numero in vetor:
    if numero % usuario == 0:
        multiplos.append(numero)

if multiplos:
    print(f"Os números que são múltiplos de {usuario} são: {multiplos}")

else:
    print("Não há nenhum número multiplo")