"""
senha_salva = '12345'
senha_informada = ""
repeticoes = 0

i = 0

while senha_salva != senha_informada:
    senha_informada = input(f'Sua senha ({repeticoes}X): ')
    
    repeticoes += 1
    
print(repeticoes)
print('O laço acima pode ser infinito')
"""

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}' 
    print(letra)
print(novo_texto)