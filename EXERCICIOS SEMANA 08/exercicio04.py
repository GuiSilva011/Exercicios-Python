from random import randint

A = []
cont = 0

while True:
    N = int(input("Entre com um numero entre 0 e 50: "))
    if  0 <= N <= 50:
     break
    else:
        print('Valor invalido')
    
while cont < N:
    X = randint(0,1000)
    A.append(X)
    cont +=1

print(A)
    