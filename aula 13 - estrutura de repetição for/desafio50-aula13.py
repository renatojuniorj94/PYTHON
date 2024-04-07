'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidero-o.
'''

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))

#Correto! :D

#Outra maneira mais aprimorada de fazer:

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n

if cont == 0:
    print('Você não digitou nenhum número par')
else:
    print('Você informou {} números pares e a soma foi {}'.format(cont, soma))

#Outra forma de fazer:

soma = 0
cont = 0
tem_par = True

for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
    else:
        tem_par = False

if tem_par:
    print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
else:
    print('Você não digitou nenhum número par')
