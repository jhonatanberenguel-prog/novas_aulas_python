salario = float (input("Digite o seu salário mensal:"))
reajuste = int (input("Digite o seu percentual de reajuste:"))

valorReajuste = salario * reajuste / 100
novosalario = salario + valorReajuste

print(f"O seu novo sálario será {novosalario}")