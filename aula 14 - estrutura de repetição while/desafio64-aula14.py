'''
Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
'''

'''num = int(input('Digite um número(999 para parar): '))
contador = 0
soma = 0
while num != 999:
    #contador fica responsável por continuar o loop, enquanto o usuário não digita 999
    contador += 1
    #soma fica responsável por somar os números digitados
    soma += num
    #jogamos a variável 'num' por último para não incluir 999 na 'variável' soma
    num = int(input('Digite um número(999 para parar): '))
print('Você digitou {} números e a soma entre eles foi {}'.format(contador, soma))'''

#Correto! :D
#Outra maneira de fazer

'''num = 0
cont = 0
soma = 0'''
#Simplificando as variáveis acima.
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número(999 para parar): '))
    soma += num
    cont += 1
#Abaixo é uma gambiarra
#Para corrigir, colocamos a variável 'num' como input antes da repetição while, e dentro de while, na última linha
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, soma - 999))

