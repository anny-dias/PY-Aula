horas = int(input("Informe as horas: "))
minutos = int(input("Informe os minutos: "))

if horas >= 0 and horas <= 23 and minutos >= 0 and minutos <= 59:
    print("Horas e minutos válios")
else:
    print("Horas e minutos inválidos")

#ou
#if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
#   print(Inválido)
#else:
#   print(Válido)
