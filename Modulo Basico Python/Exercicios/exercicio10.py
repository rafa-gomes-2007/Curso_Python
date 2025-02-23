"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# cpf = 718.307.010-70
# 147.345.110-80

#Calculo Primeirio Digito
import random
import os 


cpf_lista_1 = [1,4,7,3,4,5,1,1,0]
produto_1 = []
resultado_vazio_1 = 0
contador = 10



os.system('cls')

for numero in cpf_lista_1:
    produto_1 = [contador * numero]
    contador -= 1
    
    for resultado in produto_1:
        
        resultado_vazio_1 += resultado
resultado_vazio_1 = resultado_vazio_1 * 10
p_digito = resultado_vazio_1 % 11

if p_digito > 9:
    p_digito = 0
    print(f'O primeiro digito do CPF é {p_digito}')
else:
    print(f'O primeiro digito do CPF é {p_digito}')
    

contador_2 = 11
produto_2 = []
resultado_vazio_2 = 0

cpf_lista_2 = [1,4,7,3,4,5,1,1,0,8]

for numero_2 in cpf_lista_2:
    produto_2 = [contador_2 * numero_2]
    contador_2 -= 1
    
    for resultado_2 in produto_2:
        
        resultado_vazio_2 += resultado_2
resultado_vazio_2 = resultado_vazio_2 * 10
s_digito = resultado_vazio_2 % 11

if s_digito > 9:
    s_digito = 0
    print(f'O segundo digito do CPF é {s_digito}')
else:
    print(f'O segundo digito do CPF é {s_digito}')
    
