#3.Escreva um algoritmo que exiba todos os números ímpares do intervalo fechado de 1 a 100.
for n in range(1,101):
    if n % 2 != 0:
        print(n, end=" - ")

# ou    
#for n in range(1,101,2):
#   print(n, end=" - ")

