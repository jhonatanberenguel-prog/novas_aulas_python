print ("Calculadora de imposto de renda!") 
salariobruto = float(input("\nInforme seu salário mensal bruto:\n"))
deducaofixa = 607.2
desconto = salariobruto - deducaofixa

if desconto <= 2428.8:
     aliquota = 0
     imposto = 0

elif 2428.8 <= desconto <= 2826.65:
    aliquota = 7.5
    reducao = desconto * 0.075
    imposto_devido = reducao - 182.16

elif 2826.65 <= desconto <= 3751.05:
    aliquota = 15
    reducao = desconto * 0.15
    imposto_devido = reducao - 394.16

elif 3751.05 <= desconto <= 4664.68:
    aliquota = 22.5
    reducao = desconto * 0.225
    imposto_devido = reducao - 675.49

elif desconto > 4664.68:
    aliquota = 27.5
    reducao = desconto * 0.275
    imposto_devido = reducao - 908.73

rdc1 = 312.89
rdc2_base = 0.133145 * salariobruto
rdc2_final = 978.62 - rdc2_base

if desconto <= 5000:
    if imposto_devido > 312.89:
        resultado = rdc1 - imposto_devido
    
    else:
        resultado = imposto_devido
    salarioliquido = salariobruto - resultado
    print(f"Você está isento! \nO seu salário bruto é de {salariobruto:.2f}, a alíquota {aliquota}%, com o desconto de R$ {resultado:.2f}.  salário final será de {salarioliquido:.2f}.")

elif 5000 <= desconto <= 7350:
    resultado = imposto_devido - rdc2_final  
    salarioliquido = salariobruto - resultado
    print(f"Você terá que pagar R${resultado:.2f} de imposto de renda! \nO seu salário bruto é de {salariobruto:.2f}, a alíquota {aliquota}%, com o desconto de R$ {rdc2_final:.2f}. O salário final será de {salarioliquido:.2f}.")

else:
    salarioliquido = salariobruto - imposto_devido
    print(f"Você terá que pagar R$ {imposto_devido:.2f} de imposto de renda! \nO seu salário bruto é de {salariobruto:.2f}, a alíquota {aliquota}%, com o desconto de R$0. O salário final será de {salarioliquido:.2f}.")