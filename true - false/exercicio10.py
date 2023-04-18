'''
numero = int(input("Digite um número com 3 dígitos: "))
numeroInvertido = int(str(numero)[::-1])
print(f"Número invertido: {numeroInvertido}")
'''
numero = int(input("Digite um número com 3 dígitos: "))
a = numero // 100
resto = numero % 100
b = resto // 10
c = resto % 10
print(f"Número invertido: {c}{b}{a}")