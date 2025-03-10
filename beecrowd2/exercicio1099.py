N = int(input())

for i in range(N):
    linha = [int(num) for num in input().split()]
    X = min(linha)
    Y = max(linha)
    
    somar = 0
    
    for num in range(X+1,Y):
        if num % 2!=0:
            somar += num
    
    
    print(somar)
    

        
    
    