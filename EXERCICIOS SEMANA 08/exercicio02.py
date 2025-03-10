L = []

cont = 10

while cont > 0:
    X = int(input("Insira 10 valores na lista: "))
   
    L.append(X)
   
    cont -=1
    
L.reverse()
print(L)