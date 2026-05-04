nome = input("Digite seu nome: ")
vezes = int(input("Digite quantas vezes deseja repetir seu nome: "))

for i in range(vezes):
    print(f"{i+1}. {nome}")