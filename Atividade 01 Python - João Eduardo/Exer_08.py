peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Seu peso está normal.")
else:
    print("Você está acima do peso")