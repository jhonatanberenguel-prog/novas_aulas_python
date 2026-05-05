somapar = 0
for i in range(0,101,2):
    somapar = i + somapar

somaimpar = 0
for i in range(1,101,2):
    somaimpar = i + somaimpar

resultado = somapar + somaimpar
print(f"O resultado da soma dos números pares e ímpares são: {resultado}")