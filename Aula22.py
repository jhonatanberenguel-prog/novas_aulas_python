opcao = int(input("Você deseja calcular: \n 1- Área do retângulo \n 2-Área do triângulo \n "))
if opcao == 1:
    baseR = float(input("Qual é o comprimento da base do retângulo?: "))
    alturaR = float(input("Qual é a altura do retângulo?: "))
    areaR = baseR * alturaR
    print (f"A base do retângulo é {areaR}")
else:
    baseT = float(input("Qual é o comprimento da base do triângulo?: "))
    alturaT = float(input("Qual é a altura do triângulo?: "))
    areaT = (baseT * alturaT) / 2
    print (f"A base do triângulo é {areaT}")