'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$1
'''
valor = int(input('Qual valor você deseja sacar? '))
valor_total = valor
nota = 50
total_nota = 0
while True:
    if valor_total >= nota:
        valor_total -= nota
        total_nota += 1
    else:
        if total_nota > 0:
            print(f'Total de {total_nota} cédulas de R$ {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        total_nota = 0
        if valor_total == 0:
            break
print('fim')

#Correto! :D