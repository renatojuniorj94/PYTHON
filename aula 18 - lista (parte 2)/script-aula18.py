pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[1])  # ['Maria', 19]

print(pessoas[0][0])  # Pedro

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')

teste = list()
teste.append('Renato')
teste.append(30)
galera = list()
galera.append(teste[:])  # Criando cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

turma = list()
dado = []
totMai = totMen = 0
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    turma.append(dado[:])  # Se esquecer de colocar [:], ele vai gerar listas vazias
    dado.clear()
print(turma)

for p in turma:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totMai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totMen += 1
print(f'Ao total temos {totMai} maiores de idade e {totMen} menores de idade.')