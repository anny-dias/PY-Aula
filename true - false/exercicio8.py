nome = input("Nome do vendedor: ")
qc = int(input("Quantidade de carros vendidos: "))
vv = float(input("Valor total das vendas: "))
s = 2500.00 + (200 * qc) + (vv * 0.02)
print(f'O vendedor {nome} receberá um salário de R$ {s}')
