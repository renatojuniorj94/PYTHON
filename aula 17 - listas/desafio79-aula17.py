"""
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

num = [int(input('Digite um número: '))]
print('Valor adicionado com sucesso...')
while True:
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'S':
        num = [int(input('Digite um número: '))]
    elif continuar not in 'SN':
        print('Opção inválida!')
    else:
        break