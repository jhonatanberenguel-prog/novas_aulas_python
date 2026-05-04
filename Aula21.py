usuario = int(input("Escolha o volume de uma lata de óleo ou de uma caixa de papelão: \n 1- Lata de óleo \n 2- Caixa de papelão \n"))
if usuario == 1:
    raio = int(input("Qual seria o raio da lata?: "))
    altura = float(input("Qual altura da lata?: "))
    volumeO = 3.14159* raio**2 * altura
    print (f"O volume da sua lata é {volumeO}")
else:
    alturaC = float(input("Qual altura da sua caixa?: "))
    largura = int(input("Qual a largura da sua caixa?: "))
    comprimento = int(input("Qual o comprimento da sua caixa?: "))
    volumeC = alturaC * largura * comprimento
    print (f"O volume da sua caixa é {volumeC}")