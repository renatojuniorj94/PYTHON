#Quando nós sabemos o limite da repetição, podemos usar tanto 'for' quanto 'while'
#Quando não sabemos o limite da repetição, usamos 'while'

#Enquanto não pega maçã =
'''
while not maçã:
    passo
pega
'''

#Simulação do jogo:

'''
Enquanto não maçã:
    se (tiver)chão:
        passo
    se (tiver)buraco:
        passo
    se (tiver)moeda:
        pega
pega (maçã)
'''

#Comparando for e while:

'''for c in range(1, 10):
    print(c)
print('Fim')'''

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

#Criando um programa para encerrar ao digitar '0':

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

#Outro exemplo:

r = 's'
while r == 's':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).lower()
print('Fim')

#Outro exemplo:
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))