nome = str(input("Informe seu nome: "))
nasc = int(input("Informe ano de nascimento: "))
hoje = int(input("Informe o ano atual: "))
idade = hoje - nasc
print(f"Olá, {nome}")
print(f"Você possui em torno de {idade} anos de idade")