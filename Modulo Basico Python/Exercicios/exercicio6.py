'''Calculadora com While'''

entrar = 'sim'
print('Seja bem-vindo a calculadora: ')

while entrar == 'sim':
    num_1 = 0
    num_2 = 0
    
    numeros_validos = None
    n_1 = input('Digite o primerio numero: ')
    n_2 = input('Digite o segundo numero: ')
    try:
        num_1 = float(n_1)
        num_2 = float(n_2)
        numeros_validos = True
    
    except:
      numeros_validos = None
    
    if numeros_validos == None:
        print('Digite um numero valido')
        continue
    
    operacao = input('Escolha uma das opções [A] - Adição [S] - Subtração [M] - Multiplicação [D] - Divisão ').lower()  
    operadores_validos = 'asmd'
    
    if operacao not in  operadores_validos:
        print('Digite um operador valido')
        continue
    
    if len(operacao) > 1:
        print('Digite apenas um operador')
        continue
    
    if operacao == 'a':
        resultado = num_1 + num_2
        print(f'O resultado é {resultado:.1f}')
    elif operacao == 's':
        resultado = num_1 - num_2
        print(f'O resultado é {resultado:.1f}')
    elif operacao == 'm':
        resultado = num_1 * num_2
        print(f'O resultado é {resultado:.1f}')
    elif operacao == 'd':
        resultado = num_1 / num_2
        print(f'O resultado é {resultado:.1f}')    
             
    entrar = input('Quer continuar a Cauculadora ? ').lower()
    if entrar == 'não':
        print('Obrigado por utilizar a calculadora')
        