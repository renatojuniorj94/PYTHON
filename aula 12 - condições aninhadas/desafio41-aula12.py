'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Acima: MASTER
'''

from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano

if 0 < idade <= 1:
    print('O atleta tem {} ano e pertence a categoria MIRIM.'.format(idade))
elif 1 < idade == 9:
    print('O atleta tem {} anos e pertence a categoria MIRIM.'.format(idade))
elif 10 <= idade <= 14:
    print('O atleta tem {} anos e pertence a categoria INFANTIL.'.format(idade))
elif 15 <= idade <= 19:
    print('O atleta tem {} anos e pertence a categoria JUNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e pertence a categoria MASTER.'.format(idade))