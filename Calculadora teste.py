def soma(numero1, numero2):
    return numero1 + numero2
    
def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2
    
def divisao(numero1, numero2):
    return numero1 / numero2

def menu():
    print("---Calculadora---\n")
    print("---Menu---")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[0] Sair\n")
    usuario = int(input("R:"))
    return usuario

while True:
    usuario = menu()
    if usuario == 1:
        n1 = float(input("Digite o primeiro número escolhido:\n"))
        n2 = float(input("Digite o segundo número escolhido:\n"))
        result = soma(n1,n2)
    
    elif usuario == 2:
        n1 = float(input("Digite o primeiro número escolhido:\n"))
        n2 = float(input("Digite o segundo número escolhido:\n"))
        result = subtracao(n1,n2)

    elif usuario == 3:
        n1 = float(input("Digite o primeiro número escolhido:\n"))
        n2 = float(input("Digite o segundo número escolhido:\n"))
        result = multiplicacao(n1,n2)

    elif usuario == 4:
        n1 = float(input("Digite o primeiro número escolhido:\n"))
        n2 = float(input("Digite o segundo número escolhido:\n"))
        result = divisao(n1,n2)

    elif usuario > 5:
        print("Escolha não encontrada, tente novamente.")

    elif usuario == 0:
        print("Encerrando...") 
        break

    print(f"Resultado: {result}")
    
    