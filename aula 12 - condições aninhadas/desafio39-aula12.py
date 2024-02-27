"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostras o tempo que falta ou que passou do prazo.
"""

from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
ano_atual = date.today().year
ano_alistamento = 18 - idade + ano_atual

'''if idade > 0 and idade < 17:'''
#Simplificando o if acima
if 0 < idade < 17:
    print('Faltam {} anos para você se apresentar a junta militar.'.format(18 - idade))
elif idade == 17:
    print('Falta somente 1 ano pra o alistamento militar!')
elif idade == 18:
    print('Você tem 18 anos.'
          ' Esse é o ano para você se apresentar a junta militar mais próxima. \033[1;32mALISTE-SE JÁ\033[m!')
elif idade > 18:
    print('Já se passaram {} anos do seu período para alistamento militar.\n'
          'Se apresente a junta militar mais próxima!'.format(idade - 18))
elif idade <= 0:
    print('Ano inválido!')

print('Seu ano de alistamento foi/será em {}'.format(ano_alistamento))


# Correto! :D