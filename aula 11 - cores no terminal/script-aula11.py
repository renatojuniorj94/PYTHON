print('\033[7;32;43mCampeonato Brasileiro\033[m')
print(
    'Times RJ > \033[1;30;41mFlamengo\033[m, \033[1;31;42mFluminense\033[m, \033[1;30;107mVasco\033[m e \033['
    '1;97;40mBotafogo\033[m')
print(
    'Times SP > \033[1;31;107mS\033[30mã\033[31mo \033[30mP\033[31ma\033[30mu\033[31mlo\033[m, '
    '\033[1;30;107mSantos\033[m, \033[1;97;40mCorinthians\033[m, \033[1;97;42mPalmeiras\033[m')
print('Times MG > \033[1;97;44mCruzeiro\033[m, \033[1;97;40mAtlético-MG\033[m')
print(
    'Times RS > \033[1;97;41mInternacional\033[m, \033[1;97;44mG\033[1;30mr\033[1;97mê\033[1;30mm\033[1;97mi\033['
    '1;30mo\033[m')

#Seperando
nome = 'Renato'
print('')
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;34m', nome, '\033[m'))

estado = 'RJ'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;97m'
}
print('Eu moro no {}{}{}!!!'.format(cores['pretoebranco'], estado, cores['limpa']))
