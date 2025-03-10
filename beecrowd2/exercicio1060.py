cont = 0
numeros = 0
while cont < 6:
    num=float(input())
    if num >= 0:
        numeros += 1
        cont += 1
    elif num < 0:
        cont += 1
print(f'{numeros} valores positivos')


   