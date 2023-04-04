print("1 - Pincanha        R$: 25,00")
print("2 - Lasanha         R$: 20,00")
print("3 - Strogonoff      R$: 20,00")
print("4 - Bife Acebolado  R$: 15,00")
print("5 - Pão com Ovo     R$: 5,00")

opcao = int(input("Esolha o prato desejado: "))

match opcao:
    case 1:
        valor = 25.0
    case 2:
        valor = 20.0  
    case 3:
        valor = 20.0 
    case 4:
        valor = 15.0
    case 5:
        valor = 5.0
    case _:
        print("Opção Inválida")
        valor = 0
    
gorjeta = input("Deseja pagar os 10% (sim/nao): ")

match gorjeta:
    case "sim":
        valor = valor + valor * 10/100
        print(f"Valor Total: {valor}")
    case "nao":
        print(F"Valor total: {valor}")