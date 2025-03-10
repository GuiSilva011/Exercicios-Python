

cont = 0
valores = []


while cont < 3:
    value = int(input())
    valores.append(value)
    cont +=1

maior = max(valores)
pos = valores.index(maior) + 1

print(maior)
print(pos)
