"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante      '
lista_palavras = frase.split(',')

for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()

print(lista_palavras)