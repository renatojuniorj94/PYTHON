"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
-Á vista dinheiro/cheque: 10% de desconto
-Á vista no cartão: 5% de desconto
-Em até 2x no cartão: Preço normal
-3x ou mais no cartão: 20% de juros
"""

preco = float(input('Digite o valor do produto: R$ '))
form_pag = int(input('Digite a forma de pagamento: \n'
                     '1 - Á vista dinheiro/pix/cheque (10% de desconto)\n'
                     '2 - Á vista no cartão de crédito ou débito (5% de desconto)\n'
                     '3 - Em até 2x no cartão de crédito\n'
                     '4 - 3x ou mais no cartão de crédito (20% de juros): '))
vista = preco / 100 * 90
vista_cartao = preco / 100 * 95
cartao_tres = preco / 100 * 120

if form_pag == 1:
    print('O valor do produto para pagamento á vista irá custar R$ {:.2f}'.format(vista))
elif form_pag == 2:
    print('O valor do produto para pagamento no cartão de crédito ou débito irá custar R$ {:.2f}'.format(vista_cartao))
elif form_pag == 3:
    print('O valor do produto para pagamento em até 2x no cartão de crédito irá custar R$ {:.2f}'.format(preco))
elif form_pag == 4:
    print('O valor do produto para pagamento em até 2x no cartão de crédito irá custar R$ {:.2f}'.format(cartao_tres))
else:
    print('\033[1;31mOpção inválida!')

# Correto! :D