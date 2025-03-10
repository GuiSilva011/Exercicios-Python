from random import randint

Lista = []
N = int(input('Quantos numeros vão conter a lista?: '))
cont = 0


    
while cont < N:
    X = randint(0,1000)
    Lista.append(X)
    cont +=1

print(Lista)