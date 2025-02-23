# Algoritmo que monta uma lista de valores onde se pode apagar, excluir e adicionar 

import os 

lista = []
while True:
    print('Selecione uma opcão')
    resposta = input('[I]nserir [A]pagar [L]istar: ').upper()
    
    if resposta == 'I':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        
    elif resposta == 'A':
        indice = input('Digite a posição que você deseja excluir: ')
        
        try:     
            indice_2 = int(indice)
            del(lista[indice_2])    
            for indice, nomes in enumerate(lista):
                print(f'A posição é -> {indice} e o item é -> {nomes}')
            if lista == []:
                print('Lista Vazia')
        except ValueError:
            print('Digite um numero inteiro')
        except IndexError:
            print('Este indice não existe na lista')
        except Exception:
            print('Erro desconhecido')     
                    
    elif resposta == 'L':
        if lista == []:
            print('Lista Vazia')
        for indice, nomes in enumerate(lista):
            print(f'A posição é -> {indice} e o item é -> {nomes}')
            
    else:
        print('Escolha uma opção válida')