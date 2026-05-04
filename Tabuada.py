while True:
    num = int(input("Digite um valor para tabuada\n"))
    if num ==0:
        print("Encerrando...")
        break
    Nmin = int(input("Digite o valor mínimo para a tabuada\n"))
    Nmax = int(input("Digite o valor máximo para a tabuada\n"))
    print(f"Tabuada do {num} de {Nmin} até {Nmax}\n")
    i = Nmin
    while i <= Nmax:
        res = num * i
        print(f"{num} x {i} = {res}")
        i += 1
    print("Fim da tabuada")