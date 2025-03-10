n1 = float(input())
n2 = float(input())

while n1 > 10 or n2 > 10:
    print('nota inválida')
    n1 = float(input())
    n2 = float(input())

media = (n1 + n2) / 2

print(f'média={media:.2f}')