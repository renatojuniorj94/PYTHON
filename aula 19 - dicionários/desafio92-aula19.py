"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente
de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
"""from datetime import datetime
ctps = dict()
ctps['nome'] = str(input('Nome: '))
ctps['ano_nascimento'] = int(input('Ano de nascimento: '))
ctps['numero'] = int(input('Carteira de trabalho (0 não tem): '))
ctps['idade'] = datetime.now().year - ctps['ano_nascimento']
if ctps['numero'] == 0:
    print('-=' * 30)
    print(f'Nome: {ctps['nome']}')
    print(f'Idade: {datetime.now().year - ctps['ano_nascimento']}')
    print(f'CTPS tem o valor {ctps['numero']}')

else:
    ctps['contratação'] = int(input('Ano de contratação: '))
    ctps['salário'] = float(input('Salário: R$ '))
    print('-=' * 30)
    print(f'Nome: {ctps['nome']}')
    print(f'Idade: {datetime.now().year - ctps['ano_nascimento']}')
    print(f'Nº CTPS: {ctps['numero']}')
    print(f'Ano de contratação: {ctps['contratação']}')
    print(f'Salário: R$ {ctps['salário']}')
    print(f'A aposentadoria será com {ctps['idade'] + (ctps['contratação'] + 35) - datetime.now().year} anos de idade.')
print(ctps)
"""
#Correto! :D
#Outra maneira de fazer...

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'    — {k} tem o valor {v}')