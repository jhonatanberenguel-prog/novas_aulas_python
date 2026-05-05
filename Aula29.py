import random
while True:
    numero1 = random.randint (1,10)
    numero2 = random.randint (1,10)

    resposta = int(input(f"Quanto é {numero1} X {numero2}?\n"))
    correto = numero1 * numero2

    if resposta == correto:
        print("ACERTOU!")

    else:
        print("ERRADO")

    usuario = int(input("Deseja jogar de novo?\n1-Sim\n2-Não\n"))

    if usuario == 2:
        print("Encerrando programa...")
        break

    elif usuario > 2:
        print("Digite novamente")
