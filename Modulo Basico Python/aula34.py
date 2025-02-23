"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
import os 
os.system('cls')

# lista = [10,20,30,40]
# lista.append(50)
# lista.append(60)
# lista.append(70)
# lista.pop()
# lista.insert(0, 8)
# print(lista)


lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c, 'Lista_C')
lista_a.extend(lista_b)
print(lista_a, 'Lista_A')