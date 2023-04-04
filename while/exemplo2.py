#exibir números inteiros de 1 até 20

from calendar import prcal


cont = 1 
while cont <= 20:
    print(cont)
    cont += 1
print('FIM')

#so mostra números multilplos de 3 ate 20 

cont = 1 
while cont <= 20:
    if cont % 3 == 0:
        print(cont)
    cont += 1
print('FIM')

#solicitar 10 números e informar quantos dos mesmos são pares

cont = 1 
contapar = 0 
while cont <= 10:
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        contapar += 1   #contador dos pares 
    cont += 1           #contador das reptições
print(f"Quantidade de par: {contapar}")



