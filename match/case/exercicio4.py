print ("1 - Linux")
print ("2 - Banco de Dados")
print ("3 - Windows Server")
print ("4 - Lógica de Programação")

opcao = int(input("Informe a opção desejada: "))

match opcao:
    case 1:
        print("Auitório 1")
    case 2:
        print("Auditório 2")
    case 3:
        print("Auditório 3")
    case 4:
        print("Auditório Principal")
    case _:
        print("Opção Inválida")
    
    
