pessoas = [
    {'nome': 'Ana Paula Vieira', 'idade': 32},
    {'nome': 'Claudio Mendonça', 'idade': 18},
    {'nome': 'Gustavo Guanabara', 'idade': 41},
    {'nome': 'Maria Clara Peixoto', 'idade': 65},
    {'nome': 'Mauricio Souza', 'idade': 19},
    {'nome': 'Nilce Pedrosa', 'idade': 43},
    {'nome': 'Pedro Gonçalves', 'idade': 18},
    {'nome': 'Rafael Albuquerque', 'idade': 38},
    {'nome': 'Renata Soares', 'idade': 13}
    ]


def menu():
    from time import sleep
    while True:
        print('—' * 40)
        print('MENU PRINCIPAL'.center(40))
        print('—' * 40)
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova pessoa')
        print('3 - Sair do sistema')
        print('—' * 40)
        opção = int(input('Sua opção: '))
        if opção == 1:
            pessoasCadastradas()
            sleep(3)
        elif opção == 2:
            novoCadastro()
            sleep(3)
        else:
            break


def pessoasCadastradas():
    from time import sleep
    print('—' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('—' * 40)
    for p in pessoas:
        print(f'{p['nome']:<25}{p['idade']} anos')


def novoCadastro():
    print('—' * 40)
    print('NOVO CADASTRO'.center(40))
    print('—' * 40)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    pessoas.append({'nome': nome, 'idade': idade})
    print(f'Registro de {nome} adicionado')