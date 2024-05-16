cont = ('zero', 'hum', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        print('Número inválido!')
        num = int(input('Digite um número entre 0 e 20: '))

    print(f'Você digitou o número {cont[num]}')

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    while continuar not in ('S', 'N'):
        print('Opção inválida!')
        continuar = input('Deseja continuar? [S/N] ').strip().upper()

    if continuar == 'N':
        break
