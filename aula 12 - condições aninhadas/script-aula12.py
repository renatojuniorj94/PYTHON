nome = str(input('Digite seu nome: ')).lower()
if nome == 'renato':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ana cláudia jéssica juliana mariza':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um  bom dia, {}!'.format(nome.capitalize()))