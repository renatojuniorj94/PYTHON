#Crie um programa que leia quanto dinheiro uma pessoa
#tem na carteira e mostre quantos dólares ela pode comprar.
#Considere > U$ 1,00 = R$ 3,27

d = float(input('Digite quando você tem (R$): '))
print('Com R${} você pode comprar US${:.2f}'.format(d, d/3.27))

#Correto! :D