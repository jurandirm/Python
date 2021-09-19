# Exercício 3 - Equação de Segundo Grau Completa

a = int(input("Digite o valor de a: ")) # 1 ou 2
b = int(input("Digite o valor de b: ")) # -1 ou 8
c = int(input("Digite o valor de c: ")) # -12 ou -10

print (" ")

delta = (b**2)-4*a*c # formula do delta
raizdelta = float(delta) ** 0.5 # raiz quadrada

x1 = (-b + raizdelta)/(2*a)
x2 = (-b - raizdelta)/(2*a)

print("O valor do delta é: ",delta,"\n")
print("A raiz do delta é: ",raizdelta,"\n")
print("O valor de x1 é: ",x1)
print("O valor de x2 é: ",x2,"\n")

print("O resultado da equação de segundo grau é: ",x1," e ",x2)