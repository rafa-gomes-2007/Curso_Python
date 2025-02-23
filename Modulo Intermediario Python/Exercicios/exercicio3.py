# Jogo de perguntas e respostas

import os 

cont_c = 0
cont_e = 0

perguntas = {

    
        'Pergunta1' : 'Em que ano foi fundado o Sport Club Corinthians Paulista? ',
        'Opçoes1' : ['1542' , '1597 ', '1910', '1240'],
        'Resposta1' : '2',
    
    
    
        'Pergunta2' : 'Quantos episodios tem o anime One Piece? ',
        'Opçoes2' : ['1122', '1000', '1500' , '1800 '],
        'Resposta2' : '0',
   
    
      
        'Pergunta3' : 'Quantos mundiais tem o Sport Club Corinthians Paulista? ',
        'Opçoes3' : ['5','4','2','3 '],
        'Resposta3' : '2',
      
}

os.system('cls')
if True:
    
    print(f'Pergunta 1:',perguntas['Pergunta1'])
    for cont , respostas in enumerate(perguntas['Opçoes1']):
        print(cont,')', respostas)
    r_1 = input('Digite uma resposta: ')
    if r_1 == perguntas['Resposta1']:
        print('Voce Acertou')
        cont_c +=1
    else:
        print(' Voce Errou')  
        cont_e +=1 
        
    os.system('cls')  
    
    print(f'Pergunta 2:',perguntas['Pergunta2'])
    for cont , respostas in enumerate(perguntas['Opçoes2']):
        print(cont,')', respostas)
    r_1 = input('Digite uma resposta: ')
    if r_1 == perguntas['Resposta2']:
        print('Voce Acertou')
        cont_c +=1
    else:
        print(' Voce Errou')
        cont_e +=1 
        
    os.system('cls')
    
    print(f'Pergunta 3:',perguntas['Pergunta3'])
    for cont , respostas in enumerate(perguntas['Opçoes3']):
        print(cont,')', respostas)
    r_1 = input('Digite uma resposta: ')
    if r_1 == perguntas['Resposta3']:
        print('Voce Acertou')
        cont_c +=1
    else:
        print(' Voce Errou')
        cont_e +=1 
    
    os.system('cls')
    
    print(f'Parabéns você acertou {cont_c} e errou {cont_e}')