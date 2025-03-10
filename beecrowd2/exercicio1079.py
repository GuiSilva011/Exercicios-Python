N = int(input())

cont = 0

while cont < N:
    v1,v2,v3 = map(float,input().split())
    media = (v1 *2 + v2 * 3 + v3 * 5 ) / 10
    print(f'{media:.1f}')
    cont += 1