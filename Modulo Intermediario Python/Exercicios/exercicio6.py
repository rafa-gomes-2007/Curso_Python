import os 
os.system('cls')

def contador(cont1, cont2):
    

    print('Segue a primeira contagem')
    while cont1 < 10:
        cont1 +=1
        print(cont1)
    
    print()
    
    print('Segue a segunda contagem')    
    while cont2 > -1:
        print(cont2)
        cont2 -= 2
        

contador(0,10)