N = int(input())

i = 0

for i in range(N):
    x,y = map(int,input().split())
    X = int(x)
    Y = int(y)
    if Y == 0 :
        print('divisao impossivel')
    else:
        divi = X / Y
        print(divi)
        i +=1