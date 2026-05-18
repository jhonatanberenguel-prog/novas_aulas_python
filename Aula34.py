import random

vetor = [random.randint(1, 50) for i in range(20)]
print(vetor)
print("-" * 10)

multiplos = []

for numero in vetor:
    if numero % 5 == 0:
        multiplos.append(numero)
    
if multiplos:
    print(f"Números múltiplos de 5 encontrados:{multiplos}")
    print(f"Total de múltiplos de 5: {len(multiplos)}")

else:
    print("Não há nenhum número múltiplo de 5.")
