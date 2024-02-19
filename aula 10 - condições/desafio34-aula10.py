'''
Escreva um programa que pergunte o salário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
s = float(input('Digite o seu salário: R$ '))
if s <= 1250:
    print('Seu aumento vai ser de R${}, e o seu novo salário é de R$ {}'.format(s * 15 / 100, s + (s * 15 / 100)))
else:
    print('Seu aumento vai ser de R$ {}, e o seu novo salário é de R$ {}'.format(s * 10 / 100, s + (s * 10 / 100)))

#Correto! :D

#Outra maneira de resolver...

s = float(input('Digite o seu salário: R$ '))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(s, novo))
