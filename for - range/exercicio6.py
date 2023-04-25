#6.Criar um algoritmo que leia dez números inteiros e informe o maior e o menor número.

numero = int(input("Informe o numero: "))
menor = numero
maior = numero

for n in range(9):
    numero = int(input("Informe o numero: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"Maior: {maior}")
print(f"Menor: {menor}")
       