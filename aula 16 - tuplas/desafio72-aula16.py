'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e amostrá-lo por extenso.
'''
'''tupla = ('zero', 'hum', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    print('Opção \033[1;33mÍNVALIDA!\033[m Tente novamente...')
    num = int(input('Digite um número entre 0 e 20: '))
for pos in enumerate(tupla):
    print(f'Você digitou o número {tupla[num]}')
    break'''

#Correto! :D
#Outra maneira de fazer:

cont = ('zero', 'hum', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {cont[núm]}')
