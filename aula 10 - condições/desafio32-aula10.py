'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
'''
Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias,
 um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos 
 (exceto anos múltiplos de 100 que não são múltiplos de 400).
'''
from datetime import date
ano = int(input('Digite o ano. Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
