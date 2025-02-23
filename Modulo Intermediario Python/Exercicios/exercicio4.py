# Mostrar numeros primos e soma-los

import os
os.system('cls')


    
print('Seja Bem-vindo ao indicador de numeros primos')
print('Digite um valor inicial e um final para começarmos')

valor_i = input('Digite o  valor inicial: ')
valor_f = input('Digite o  valor final: ')


print()

print('Estes são os numeros primos')

valor_i_int = int(valor_i)
valor_f_int = int(valor_f)

n_p = range(valor_i_int,valor_f_int)

lista_n_p = []

for n in n_p:
    r = n % 2
    r1 = n % 3
    r2 = n % 5
    r3 = n % 7
    r4 = n % 11
    
    if n > 2:
        if r == 0:
            continue
    if n > 3:        
        if r1 == 0:
            continue
    if n > 5:
        if r2 == 0:
            continue
    if n > 7:
        if r3 == 0:
            continue        
    if n > 11:
        if r4 == 0:
            continue
    
    lista_n_p.append(n)
    print(n)

for numeros in lista_n_p:
    print(f'Esta é a soma dos numeros primos {sum(lista_n_p)}')
    break