#solicitar  números p/ usuario e somar os números

soma = 0 
a = int(input("Valor inicial: "))
b = int(input("Valor final: "))

for n in range (a,b):
    numero = int(input("Informe um número: "))
    soma += numero
print(f"Somatório dos números: {soma}")

