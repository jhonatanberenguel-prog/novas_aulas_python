dia = int(input("Digite a quantidade de dias:"))
hora = int(input("Digite quantas horas:"))
minutos = int(input("Digite quantos minutos:"))
segundos = int(input("Digite quantos segundos:"))

dia = dia * 24 * 60 * 60
hora = hora * 60 * 60
minutos = minutos * 60

Total = dia + hora + minutos + segundos

print(f"O total de segundos foi {Total}")