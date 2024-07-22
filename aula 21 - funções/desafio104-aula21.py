"""
Crie um programa que tenha função leiaInt(), que vai funcionar de forma semelhante
à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt('Digite um n')
"""


def leiaInt(msg):  # Define uma função chamada 'leiaInt' que recebe um argumento 'msg'.
    # Este argumento será a mensagem exibida ao usuário ao solicitar a entrada.

    ok = False  # Inicializa a variável 'ok' com o valor 'False'.
    #Esta variável será usada como uma flag para indicar se a entrada foi validada com sucesso.

    valor = 0  # Inicializa a variável 'valor' com o valor '0'.
    #Esta variável armazenará o número inteiro válido fornecido pelo usuário.

    while True:  # Inicia um loop while True, que continuará executando até que uma entrada válida seja fornecida.

        n = str(input(msg))  # Solicita uma entrada do usuário, exibindo a mensagem 'msg'.
        #A entrada é convertida para uma 'string' e armazenada na variável 'n'.

        if n.isnumeric():  # Verifica se a string 'n' contém apenas dígitos numéricos usando o método isnumeric().
            valor = int(n)  # Se a string contém apenas dígitos, converte a string para um inteiro e armazena em 'valor'
            ok = True  # Define a variável 'ok' como 'True', indicando que a entrada é válida.
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:  # Se a flag 'ok' for 'True', o loop é encerrado usando 'break'.
            break

    return valor  # Retorna o valor inteiro validado.


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

"""
Explicação Final
- Função leiaInt: A função garante que o usuário digite um número inteiro válido, repetindo a solicitação até
que uma entrada correta seja fornecida.

- Inicialização: As variáveis ok e valor são usadas para controlar o fluxo do loop e armazenar o valor validado.

- Loop while True: O loop continua solicitando a entrada do usuário até que uma entrada válida seja fornecida.

- Validação de Entrada: Usa isnumeric() para verificar se a entrada é numérica e, se for, converte para inteiro.

- Mensagem de Erro: Se a entrada não for válida, exibe uma mensagem de erro.

- Saída do Loop: O loop é interrompido quando uma entrada válida é fornecida.

- Retorno: A função retorna o valor inteiro validado.

- Uso no Programa Principal: Chama a função leiaInt para obter um número inteiro do usuário e o exibe na tela.
"""
