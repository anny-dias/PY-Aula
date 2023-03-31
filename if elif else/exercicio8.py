a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a < b and a < c:
    print(f"Menor número é {a}")
elif b < a and b < c:
    print(f"Menor número é {b}")
elif c < a and c < b:
    print(f"Menor número é {c}")
elif a == b and b == c:
    print("Três numeros iguais")
else:
    print("Dois numeros iguais")