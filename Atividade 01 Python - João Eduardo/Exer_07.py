salario = float(input("Digite o seu salário: "))
tempo = float(input("Digite seu tempo de empresa em anos: "))

aumento = None
reajuste = None
porcentagem = None

if tempo < 2:
    aumento = salario * 0.05
    porcentagem = 5
elif tempo >= 2 and tempo <= 5:
    aumento = salario * 0.1
    porcentagem = 10
else:
    aumento = salario * 0.15
    porcentagem = 15

reajuste = salario + aumento

print(f"Você que recebia {salario} R$, e tem {tempo} anos de empresa, teve um aumento no seu salário de {porcentagem}%, no valor de {aumento} R$, e agora o seu salário é de {reajuste} R$.")