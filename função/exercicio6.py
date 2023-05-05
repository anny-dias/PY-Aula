#Implementar uma função que recebe como parâmetro a altura em metros (exemplo: 1.70) 
# e o sexo ('M' para masculino e 'F' para feminino) de uma pessoa e retorne o seu peso ideal, 
# sendo que:
# Peso Ideal (para homens) = (72.7 * altura) -58 
# Peso Ideal (para mulheres) = (62.1 * altura) -44.7

def peso_ideal(sexo):
    if sexo == "F":
        p = (62.1 * altura) -44.7
        print(f"O peso ideal, para mulher, é: {p} ")
    elif sexo == "M":
        p = (72.7 * altura) -58 
        print(f"O peso ideal, para homem, é: {p} ")
    else:
        print("Opção Inválido")
    return p 


altura = float(input("Infome a sua altura: "))
sexo = input("Informe o seu sexo (M = Masculino e F = Feminino): ")
p = peso_ideal(sexo)




