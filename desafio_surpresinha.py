#versão 1.0
import random
quant_num = 0
modalidade = ''
loteria = int(input('Qual loteria deseja apostar?\n'
                        'Mega-sena [1]\n'
                        'Quina [2]\n'
                        'Lotofacil [3]\n'))
while True:
    if loteria <= 0 or loteria > 3:
        print('Opção inválida!')
        loteria = int(input('Qual loteria deseja apostar?\n'
                            'Mega-sena [1]\n'
                            'Quina [2]\n'
                            'Lotofacil [3]\n'))
    if loteria == 1:
        print('Você escolheu Mega-sena')
        quant_num = int(input('Quantos números deseja escolher? [6 a 15] '))
        num_unicos = random.sample(range(1, 61), quant_num)
        break
    if loteria == 2:
        print('Você escolheu Quina')
        quant_num = int(input('Quantos números deseja escolher? [5 a 15] '))
        num_unicos = random.sample(range(1, 81), quant_num)
        break
    if loteria == 3:
        print('Você escolheu Lotofacil')
        quant_num = int(input('Quantos números deseja escolher? [15 a 20] '))
        num_unicos = random.sample(range(1, 26), quant_num)
        break
#Ordenando os números em ordem crescente
num_unicos.sort()
print(num_unicos)