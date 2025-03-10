A = []

lmin = int(input('Insira o valor minimo: '))
lmax = int(input('Insira um valor maximo: '))
N = int(input('Insira quantos valores a lista deve conter: '))

cont = 0

if lmin > lmax:
    lmin,lmax = lmax, lmin

while cont < N:
    X = int(input('Insira dez valores '))
    if X < lmin or X > lmax:
        cont +=1
    else:
     A.append(X)
     cont +=1
    
print(A)