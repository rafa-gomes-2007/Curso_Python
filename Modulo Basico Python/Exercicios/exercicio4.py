""" ENUNCIADO 1
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


#----------------------------------------------------------------------------------------------------------------------------------- 


'''''EXERCICIO 1
numero = input('Digite um numero: ')

if numero.isdigit():   
    
    resto_p = int(numero) % 2
    resto_i = int(numero) % 2 
    
    if resto_p == 1:
        print('Este numero é impar')
    elif resto_i == 0:
        print('Este numero é par')  
        
else:
    print('Digite um numero inteiro')
'''
    
    
    
#----------------------------------------------------------------------------------------------------------------------------------- 
    
    
    
    
    
""" ENUNCIADO 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#----------------------------------------------------------------------------------------------------------------------------------- 

''' Exercicio 2
horas = float(input('Fala Chefe, que horas são ? '))

if horas > 0  and  horas <= 11:
    print('Bom dia, Chefe')
elif horas >= 12  and  horas <= 17:
    print('Bom tarde, Chefe')
elif horas >= 18  and  horas <= 23:
    print('Bom noite, Chefe')
'''
 
 
#-----------------------------------------------------------------------------------------------------------------------------------  
 
""" ENUNCIADO 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


#----------------------------------------------------------------------------------------------------------------------------------- 

''' Exercicio 3
    nome = input('Fala Chef, Qual o seu nome mesmo ? ')

if len(nome) <= 4:
    print('Seu nome é curto Chef !')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal Chef !')
elif len(nome) > 6:
    print('Seu nome é grande Chef !')  
'''
