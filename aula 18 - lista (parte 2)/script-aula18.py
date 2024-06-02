pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[1])
#['Maria', 19]

print(pessoas[0][0])
#Pedro

for p in pessoas:
    print(p[0])
#Imprindo somente os nomes

teste = list()
teste.append('Renato')
teste.append(30)
galera = list()
galera.append(teste[:]) # Criando cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
