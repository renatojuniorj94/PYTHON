'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7 por cada km acima do limite.
'''
vel = float(input('Digite a velocidade do veiculo: '))
if vel <= 80:
    print('Sua velocidade é {}Km/h, Dirija com segurança e boa viagem!'.format(vel))
else:
    print('VOCÊ FOI MULTADO! Sua velocidade é de {}Km/h, é o valor da sua multa é de R$ {}'.format(vel, (vel - 80) * 7))

# Correto! :D

# Outra maneira de fazer usando uma condição simples.

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade >= 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
