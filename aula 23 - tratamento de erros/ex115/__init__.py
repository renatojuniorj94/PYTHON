def menu():
    print('—' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('—' * 40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('—' * 40)
    opção = int(input('Sua opção: '))


def pessoasCadastradas():
    pessoas = [
        {'nome': 'Ana Paula Vieira', 'idade': 32},
        {'nome': 'Claudio Mendonça', 'idade': 18},
        {'nome': 'Gustavo Guanabara', 'idade': 41},
        {'nome': 'Maria Clara Peixoto', 'idade': 65},
        {'nome': 'Mauricio Souza', 'idade': 19},
        {'nome': 'Nilce Pedrosa', 'idade': 43},
        {'nome': 'Pedro Gonçalves', 'idade': 18},
        {'nome': 'Rafael Albuquerque', 'idade': 38},
        {'nome': 'Renata Soares', 'idade': 13},
    ]
    print('—' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('—' * 40)
    for p in pessoas:
        print(f'{p['nome']:<25}  \t  {p['idade']} anos')


pessoasCadastradas()