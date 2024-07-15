#Para ver todas as bibliotecas, colocamos "import" e apertamos ctrl + espaço
#import math > Nós importamos toda a biblioteca math
#from math import sqrt > Importamos somente sqrt da biblioteca de matematica
#from math import sqrt, ceil > Importando duas funcionalidades da biblioteca math

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))

import random
print(random.randint(1, 60), random.randint(1, 60), random.randint(1, 60),
      random.randint(1, 60), random.randint(1, 60), random.randint(1, 60))

#https://www.webfx.com/tools/emoji-cheat-sheet/
#https://pypi.org/project/emoji/
import emoji
print(emoji.emojize('Olá mundo :smiling_face_with_sunglasses:'))
print(emoji.emojize('Python is :winking_face:'))  # O nome do código do emoji é shortcode.
