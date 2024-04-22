'''
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos.
'''

termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
pa = termo
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(pa), end='')
        pa += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Você quer exibir mais quantos termos? '))
print('Progressão finalizada com {} termos mostrados'.format(total))

#Correto! :D