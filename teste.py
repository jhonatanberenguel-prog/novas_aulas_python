usuario = float(input("Informe o valor do seu imposto de renda: "))
fontederenda = int(input("Quantas fontes de renda você possui? \n1-Uma \n2-Mais de uma \n"))

if usuario < 5000 and fontederenda == 1:
    print("Você está isento de pagar impostos!")

elif usuario < 5000 and fontederenda == 2:
    print("Você precisará pagar impostos!")

input("\nPressione ENTER para sair...")