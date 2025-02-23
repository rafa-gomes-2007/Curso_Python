
# Demonstração de loop infinito

nome = 'Rafael Gomes'
inico = 1
fim = 0

while nome:
    inico += 1
    fim += 1
    print(f'{nome[inico:fim:1]}*')