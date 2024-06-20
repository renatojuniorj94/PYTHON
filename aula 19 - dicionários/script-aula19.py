#Para especificar uma variável como dicionário:
"""nome = dict()"""
#Ou
"""nome = {}"""
pessoas = {'nome': 'Renato', 'idade': 30}
print(pessoas['nome'])
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos')

#Para adicionar mais um item em dicionário:
pessoas['sexo'] = 'M'
print(pessoas)

#Para remover algum dado utilizamos 'del':
del pessoas['sexo']
print(pessoas)

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

#Para imprimir os valores:
print(filme.values())
#Para imprimir as chaves:
print(filme.keys())
#Para imprimir itens (valor + chave):
print(filme.items())

#Lendo todos os itens do dicionário:
for k, v in filme.items():
    print(f'O {k} é {v}')

#Juntando tuplas, listas e dicionários:
locadora = list()
locadora.append(filme)
print(locadora)
filme = {
    'titulo': 'Avenger',
    'ano': 2012,
    'diretor': 'Joss Whedon'
}
locadora.append(filme)
print(locadora)

filme = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'skdass'
}

locadora.append(filme)
print(locadora)
del locadora[0]
print(locadora)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])

estado = dict()
país = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    #Em dicionário não podemos usar fatiamento [:], temos que usar copy()
    país.append(estado.copy())
print(país)
for e in país:
    print(e)
for e in país:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')