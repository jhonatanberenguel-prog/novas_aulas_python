import random
vetor = [random.randint(1,50) for i in range(10)]

print("Escolha uma opção de exibição:")
print("[1] Ordem normal")
print("[2] Ordem inversa")
opcao = int(input("Escolha a opção 1 ou 2:\n"))

if opcao == 1:
    print(vetor)
    print("Vetor na ordem normal:")
    for i in range(0, 10):
        print(vetor[i], end=" ")
    
elif opcao == 2:
    print(vetor)
    print("Vetor na ordem inversa:")
    for i in range(9, -1, -1):
        print(vetor[i], end=" ")

else:
    print("Opção invalida")
