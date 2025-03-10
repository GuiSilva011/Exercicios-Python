A = []

lmin = int(input('Insira o valor minimo: '))
lmax = int(input('Insira um valor maximo: '))


cont = 0

if lmin > lmax:
    lmin,lmax = lmax, lmin

while cont < 10:
    X = int(input('Insira dez valores '))
    if X < lmin or X > lmax:
        cont +=1
    else:
     A.append(X)
     cont +=1
    
print(A)

