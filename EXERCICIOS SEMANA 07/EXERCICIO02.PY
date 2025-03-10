lista = []

p = 1

while p > 0:
    X = int(input('Insira numeros postivios maiores que zero: '))

    if X <= 0:
        print(lista)
        
        for i in range(len(lista)):
            print(f'Elemento {i + 1}: {lista[i]} ')
        p -= 1
    else:
        lista.append(X)
    
        
        