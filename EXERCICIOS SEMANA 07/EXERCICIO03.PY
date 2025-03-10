lista = []

cont = 0

while cont < 10:
    X = int(input('Preencha a lista com dez valores: '))
    
    lista.append(X)
    cont +=1
    
lista.reverse()
print(lista) 