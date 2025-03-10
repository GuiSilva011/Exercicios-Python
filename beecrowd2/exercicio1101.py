soma = 0
a = 0
while a !=1:
    m,n = map(int,input().split())
    soma = 0
    if m > n:
        aux = m
        m = n
        n = aux
        
    if m < 1 or n < 1:
        a = 1
    else:
        for i in range(m,n+1):
            print(f"{i} ",end ="")
            soma +=i
            
            if i == n:
                print(f"Sum = {soma}")