letra = input("Informe uma letra: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Vogal")
elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("Vogal") # ou letra = letra.lower() -> tranforma a letra maiuscula em minuscula / letra.upper() -> tranforma a letra minuscula em maiscula #
else:
    print("Consoante")

# ou 
#vogais = "aiouAEIOU" 
# if letra in (inserida na) vogais:
    #print("Vogal")
#else:
    #print("Consoante")