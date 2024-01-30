#Faça um algoritmo que leia o salário de um funcionário
#e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite seu salario atual: R$ '))
print('Seu novo salario com aumento de 15% é R$ {:.2f}'.format((s/100) * 115))

#Correto, mas a maneira ideal de fazer é esta:

aumento = s + (s * 15 / 100)
print(aumento)