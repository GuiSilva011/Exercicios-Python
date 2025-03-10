A = []


cont = 0


while True:
    N = int(input("Entre com um numero entre 0 e 50: "))
    if  0 <= N <= 50:
     print("ERRO: VALOR INVÁLIDO")
     break
    else:
        print("Numero inválido")
        
   
while cont < N:
    X = float(input(("Insira numeros reais na lista A: ")))
    A.append(X)
    cont +=1

    
print(A)
    