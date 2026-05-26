def soma(numero1, numero2):
    return numero1 + numero2
    
def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2
    
def divisao(numero1, numero2):
    return numero1 / numero2

while True:
    print("---Calculadora---\n")
    print("---Menu---")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Sair\n")

    usuario = int(input("R:"))

    if usuario == 1:
        n1 = float(input("Digite o primeiro número escolhido:\n"))
        n2 = float(input("Digite o segundo número escolhido:\n"))
        print(f"Resultado: {soma(n1,n2)}\n")
    
    elif usuario == 2:
        n1 = float(input("Digite o primeiro número escolhido:\n"))
        n2 = float(input("Digite o segundo número escolhido:\n"))
        print(f"Resultado: {subtracao(n1,n2)}\n")

    elif usuario == 3:
        n1 = float(input("Digite o primeiro número escolhido:\n"))
        n2 = float(input("Digite o segundo número escolhido:\n"))
        print(f"Resultado: {multiplicacao(n1,n2)}\n")

    elif usuario == 4:
        n1 = float(input("Digite o primeiro número escolhido:\n"))
        n2 = float(input("Digite o segundo número escolhido:\n"))
        print(f"Resultado: {divisao(n1,n2)}\n")

    elif usuario > 5:
        print("Escolha não encontrada, tente novamente.")

    else:
        print("Encerrando...")
        break   


