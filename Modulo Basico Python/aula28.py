string = 'Valor Qualquer'

i = 0
while i< len(string):
    letra = string[i] #Ele esta acessando um indice/ uma letra da string
    
    print(letra)
    i += 1
else:
    print('Não encontrei espaços na string')
print('Fora do while')