#8.Escreva um algoritmo que solicite o valor de N e calcule o fatorial de N.
numero = int(input("Informe um número: "))

fatorial = 1          #acumuladora
while numero >= 1:
    fatorial *= numero
    numero -= 1

print(f"Fatotial: {fatorial}")

