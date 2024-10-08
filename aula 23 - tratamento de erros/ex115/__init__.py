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
        try:
            print('—' * 40)
            print('MENU PRINCIPAL'.center(40))
            print('—' * 40)
            print('\033[1;32m1 -\033[m \033[1;34mVer pessoas cadastradas\033[m')
            print('\033[1;32m2 -\033[m \033[1;34mCadastrar nova pessoa\033[m')
            print('\033[1;32m3 -\033[m \033[1;34mSair do sistema\033[m')
            print('—' * 40)
            opção = int(input('\033[1;32mSua opção:\033[m '))
            if opção == 1:
                pessoasCadastradas()
                sleep(1.5)
            elif opção == 2:
                novoCadastro()
                sleep(1.5)
            elif opção < 1 or opção > 3:
                print('\033[31mOpção inválida!\033[m')
                sleep(1.5)
            elif opção == 3:
                print('\033[1;34;43m<<< Volte sempre! >>>\033[m')
                break
        except ValueError:
            print('\033[31mERRO: Por favor, digite um número válido.\033[m')
            sleep(1.5)


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