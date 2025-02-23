# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# n = 2
# n1 = 3
# n2 = 4

# def duplicar(result):
#     result *=2
#     return result 

# def triplo(result2):
#     result2 *=3
#     return result2 
# def quadruplo(result3):
#     result3 *=4
#     return result3

# dobro = duplicar(5)
# triplo = triplo(5)
# quadruplo = quadruplo(5)

# print(dobro, triplo, quadruplo)

def criar_multiplicador(multilpicador):
    def multiplicar(numero):
        return numero * multilpicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(5))
print(quadruplicar(10))