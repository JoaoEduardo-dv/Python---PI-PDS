temperatura = int(input("Digite a temperatura da cadeira em ºC: "))
if temperatura < 100:
    print("Temperatura baixa.")
elif temperatura >= 100 and temperatura <= 150:
    print("Temperatura Normal.")
else:
    print("Alerta: Temperatura alta.")