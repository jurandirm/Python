# Exercício 2 - Média

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1+nota2)/2

if media>=6:
    print("Você foi aprovado!!!" + "\n" + "Sua média foi: ",media)
else:
    print("Você foi reprovado!!!" + "\n" + "Sua média foi: ",media)    