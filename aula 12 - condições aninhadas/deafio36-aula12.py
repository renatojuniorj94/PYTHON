'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado.
'''

casa = float(input('Qual o valor do imóvel? '))
salário = float(input('Digite o seu salário '))
anos = int(input('Em quanto anos você vai pagar o imóvel? '))

mensalidade = casa / (anos * 12)
trinta_porcento = salário / 100 * 30

if mensalidade > trinta_porcento:
    print('O valor da parcela ficou em R$ \033[31m{:.2f}\033[m em {} meses, e \033[31minfelizmente\033[m não será possível seguir com o financiamento.'.format(mensalidade, anos * 12))
else:
    print('\033[32mParabéns!\033[m Sua renda foi aprovada e podemos seguir com a negociação.'
          ' O valor da parcela será de R$ \033[32m{:.2f}\033[m em \033[32m{}\033[m meses.'.format(mensalidade, anos * 12))
