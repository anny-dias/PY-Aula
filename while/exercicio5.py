cont = 1

a = 0

while cont <= 15:

    numero = int(input("Informe um número: "))

    if numero % 2 != 0:

        a +=1    #contador dos impares

    cont += 1   #contador das repetições

print(f'quantidade de impar: {a}')