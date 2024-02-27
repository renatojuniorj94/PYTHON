"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- Média abaixo de 5:
REPROVADO

- Média entre 5 e 6,99:
RECUPERAÇÃO

- Média 7 ou superior:
APROVADO
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi {} e você foi \033[1;31mREPROVADO\033[m!'.format(media))
#elif media >= 5 and media < 9:
elif 5 <= media <= 6.99:
    print('Sua média foi {} e você está de \033[1;33mRECUPERAÇÃO\033[m!'.format(media))
else:
    print('\033[1;32mParabéns\033[m! Sua média foi {} e você foi \033[1;32mAPROVADO\033[m!'.format(media))


# Correto! :D