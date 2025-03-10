A = []
NEG = []
POS = []
contaPOS=0
contaNEG=0
N = 1
cont = 0 


while N > 0:
    N= int(input("Digite numrs entre 0 a 50: "))
    if 0 <= N <= 50 :
        break
    else:
        print("Insira um valor valido: ")

while cont < N:
    X=float(input("Digite numeros reais: "))
    A.append(X)
    cont +=1

    if X > 0:
        POS.append(X)
        contaPOS +=1
    else:
        NEG.append(X)
        contaNEG +=1
print(A)
print(contaPOS)
print(contaNEG)