lista = ['MARIA','JOÃO','PEDRO']
lista.append('CARLOS')


# lista_numerada = enumerate(lista)
# print(next(lista_numerada))

for item in enumerate(lista):
    indice , nome = item
    print(indice , nome)
    

# for item in lista_numerada:
#     print(item)