nota1 = int(input("Digite sua primeira nota: ")) #Considerando a nota do IF: 0 à 100
nota2 = int(input("Digite sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 70:
    print("Aprovado")
elif media >= 50 and media <= 69:
    print("Recuperação")
else:
    print("Reprovado")