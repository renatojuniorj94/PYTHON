'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7 por cada km acima do limite.
'''
vel = int(input('Digite a velocidade do veiculo: '))
if vel <= 80:
    print('Sua velocidade é {}Km/h, Dirija com segurança e boa viagem!'.format(vel))
else:

    print('VOCÊ FOI MULTADO! Sua velocidade é de {}Km/h, é o valor da sua multa é de R$ {}'.format(vel, vel > 1 * 7))