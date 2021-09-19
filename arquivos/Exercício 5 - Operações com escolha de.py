# Exercício 5 - Operações com escolha de sinal

from math import sin

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
sinal = input("Digite o operador: ")

if sinal == "+":
    print("A soma dos valores é: ",num1+num2)
elif sinal == "-":
    print(("A subtração dos valores é: ",num1-num2))
elif sinal == "*":
    print(("A multiplicação dos valores é: ",num1*num2))
elif sinal == "/":
    print(("A divisão dos valores é: ",num1/num2))
elif sinal == "**":
    print(("A exponenciação dos valores é: ",num1**num2))
elif sinal == "%":
    print(("O resto da divisão dos valores é: ",num1%num2))
else:
    print("Sinal não encontrado!")                