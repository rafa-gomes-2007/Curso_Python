"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

n_1 = 0.7
n_2 = 0.1
n_3 = n_1 + n_2
print(n_3)
print(round(n_3, 2))