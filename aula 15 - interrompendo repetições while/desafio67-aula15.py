'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
print('=' * 30)
print(f'{'Desafio Tabuada':^30}')
print('=' * 30)

while True:
    num = int(input('Digite um número para a tabuada: '))
    print('—' * 30)
    if num < 0:
        break
    tab = 1
    while tab < 11:
        print(f'{num} x {tab} = {num * tab}')
        tab += 1
    print('—' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

#Correto! :D
#Outra maneira de fazer:
#No laço de repetição acima 'while tab < 11:', podemos substituir por um laço de repetição for
'''for tab in range(1, 11):
    print(f'{num} x {tab} = {num * tab}')
print('—' * 30)'''