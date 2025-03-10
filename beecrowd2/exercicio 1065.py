cont = 0
pares = 0

while cont < 5:
    num=int(input())
    if num % 2 == 0:
        pares += 1
        cont += 1
    else:
        cont += 1
print(f'{pares} valores pares')