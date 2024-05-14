cont = ('zero', 'hum', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))
while True:
    while num < 0 or num > 20:
        print('Número inválido!')
        num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 or num <= 20:
        print(f'Você digitou o número {cont[num]}')
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar == 'S':
            num = int(input('Digite um número entre 0 e 20: '))
            continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        elif continuar != 'S' or continuar != 'N':
            print('Opção inválida!')
        else:
            break

''' while num < 0 or num > 20:
print('Número inválido!')
num = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {cont[num]}')
continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
if continuar == 'N':
break'''