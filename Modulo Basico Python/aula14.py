numero_1 = input("Digite o primeiro numero: ")
numero_2 = input("Digite o segundo numero: ")

if numero_1 > numero_2:
    print(f'O primeiro numero  ({numero_1})  é maior que o segundo ({numero_2}) ')
elif numero_2 > numero_1:
    print(f'O segundo numero  ({numero_2})  é maior que o primeiro ({numero_1}) ')
else:
    print('Os numeros são iguais')