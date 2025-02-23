# Algoritmo que calcucla a area de um retangulo com função

def area(largura, comprimento):
    result = comprimento * largura
    return result
print('Bem vindo ao algoritmo')

comp = int(input('Me fale o comprimento: '))
larg = int(input('Me fale a largura: '))

print(f'O reultado é {area(comp,larg)}')