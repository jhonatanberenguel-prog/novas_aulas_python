valormin = int(input("Digite um valor minímo que deseja:\n"))
valormax = int(input("Digite um valor máximo que deseja:\n"))

for i in range(valormin,valormax+1):
    if i % 2 == 0:
        print(f"Os números {i} são pares")

    else:
        print(f"Os números {i} são impares")