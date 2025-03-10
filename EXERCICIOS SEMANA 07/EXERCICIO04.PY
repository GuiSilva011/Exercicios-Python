lista1 = []
lista2 = []

cont = 0

for i in range(10):
    X = int(input('Preencha a primeira lista com dez numeros: '))
    lista1.append(X)
    print(f'Primeira lista preenchida com os numeros: {lista1}')
    
for i in range(10):
    P = int(input('Preencha a segunda lista com dez numeros'))
    lista2.append(P)
    print(f'Segunda lista preenchida com os numeros: {lista2}')
    
junta_lista = lista1 + lista2

print(f'As duas listas juntas: {junta_lista}')
    