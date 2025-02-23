for i in range(10):
    if i == 3:
        print('I é 3 estou pulando...')
        continue
    if i == 5:
        print('I é 5, seu else não executará')
        break
    
    for j in range(1,5):
        print(i , j)
else:
    print('For completo com sucesso')
    
#Projetinho legal d+