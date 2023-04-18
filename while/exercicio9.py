num = int(input("Informe a quantidade de números: "))

cont = 1 
somapar = 0 
somaimpar = 0 
contapar = 0 
contaimpar = 0 

while cont <= num:
    numero = int(input("Número: "))
    if numero % 2 == 0:
        somapar += numero       #somatorio dos pares 
        contapar += 1           #conta a quantidade de pares 
    else:
        somaimpar += numero     #somatorio dos impares
        contapar += 1           #conta a quantidade de impares
    cont += 1

if contapar > 0:
    mediapar = somapar / contapar
    print(f"A media dos pares {mediapar}")
else:
    print("Não há números pares")

if contapar > 0:
    mediaimpar = somaimpar / contaimpar
    print(f"A media dos pares {mediaimpar}")
else:
    print("Não há números impares")



