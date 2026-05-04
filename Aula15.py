precodagasolina = float(input("Digite o preço da gasolina:"))
desempenho = float(input("Digite qual é o consumo do seu carro KM/L:"))
distancia = int(input("Digite a distância do ponto de partida até o destino final:"))

litros = distancia / desempenho
preco = litros * precodagasolina

print(f"Você gastou {litros}L e pagará R${preco}")