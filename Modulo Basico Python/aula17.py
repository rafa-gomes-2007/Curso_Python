# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
#nome = 'Rafael'
#print(nome[5])
#print('Rafa' in nome)
#print('Rafa' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em nome')
else:
    print(f'{encontrar} não esta em {nome}')