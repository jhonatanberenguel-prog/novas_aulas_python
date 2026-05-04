capacidade = 500
pessoa1 = int(input("Digite seu peso: "))
pessoa2 = int(input("Digite seu peso: "))
pessoa3 = int(input("Digite seu peso: "))
pessoa4 = int(input("Digite seu peso: "))
pessoa5 = int(input("Digite seu peso: "))

pesototal = pessoa1 + pessoa2 + pessoa3 + pessoa4 + pessoa5
 
if pesototal < capacidade:
    print("O elevador está liberado para subir.")
else:
    if pesototal > capacidade: 
        print("O elevador excedeu a capacidade máxima.")
    