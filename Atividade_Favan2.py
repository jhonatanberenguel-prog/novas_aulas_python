rodando = True
while rodando:
    numero = int(input("Digite o número da tabuada que deseja saber: "))
    print(f"Tabuada do {numero}!")
    for i in range(1, 11):
        tabuada = i * numero
        print (f"{numero} x {i} = {tabuada}")
    
    while True:
        continuar = int(input("Deseja continuar? \n1-Sim \n2-Não \nR:"))

        if continuar == 1:
            break

        elif continuar == 2:
            print ("Finalizando programa!")
            rodando = False
            break

        else:
            print("Por favor digite o número correto.")