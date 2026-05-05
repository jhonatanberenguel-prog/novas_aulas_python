incio = int(input("Digite um número inicial:\n"))
final = int(input("Digite um número final:\n"))
terceiro = int(input("Digite o divisor:\n"))

for i in range(incio,final + 1):
    if i % terceiro == 0:
        print(f"{i} é divisivel por {terceiro}")
    
    else:
        print("Não foi possível realizar a divisão.")
