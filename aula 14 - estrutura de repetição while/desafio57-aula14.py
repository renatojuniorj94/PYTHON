'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

#Feito com IA
'''while True:
    #[0] Pega somente a primeira letra
    sexo = input("Digite o sexo (M/F): ").upper().strip()[0]
    if sexo == 'M' or sexo == 'F':
        print('Sexo {} registrado com sucesso!'.format(sexo))
        exit()
    else:
        print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")'''

#Correto! :D

#Outra maneira de fazer
sexo2 = input("Digite de novo o sexo (M/F): ").upper().strip()[0]
while sexo2 not in 'MmFf':
    sexo2 = input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo2))