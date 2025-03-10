cont = 0
positivos = 0
soma = 0
while cont < 6:
    num=float(input())
    if num >= 0:
        positivos += 1
        soma += num
        cont += 1
    elif num < 0:
        cont += 1
print(f'{positivos} valores positivos')

if positivos > 0:
    media = soma / positivos
    print(f'{media:.1f}')
