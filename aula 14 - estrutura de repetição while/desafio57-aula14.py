'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

'''s = 'M', 'm', 'F', 'f'
teste = str(input('Digite o sexo [M/F]: '))
while teste == s:
    print(teste)
'''

#Feito com IA
while True:
    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo == 'M' or sexo == 'F':
        print(sexo)
    else:
        print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
