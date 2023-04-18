#solicitar 5 números e calcular a quatidade de números pares

quantidade = 0
for n in range(5):
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        quantidade += 1
print(f"Quantidade de números pares: {quantidade}")
