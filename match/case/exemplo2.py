letra = input("Informe uma letra: ")

match letra:
    case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
        print("Vogal")
    case _ :
        print("Consoante")
