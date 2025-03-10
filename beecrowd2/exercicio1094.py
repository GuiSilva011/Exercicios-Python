N = int(input())

S = 0 
C = 0
R = 0
Total = 0

for i in range(N):
    qtd, tipo = input().split()
    
    qtd = int(qtd)
    
    Total = Total + qtd
    
    if (tipo == 'R' or tipo == 'r'):
        R = R + qtd
        
    elif (tipo == 'C' or tipo == 'c'):
        C = C + qtd
    elif (tipo =='S' or tipo == 's'):
        S = S + qtd
        
percentual_R = (R / Total) * 100
percentual_C = (C / Total) * 100
percentual_S = (S / Total) * 100       

print(f'Total: {Total} cobaias')
print(f'Total de coelhos: {C}')
print(f'Total de ratos: {R}')
print(f'Total de sapos: {S}')
print(f'Percentual de coelhos: {percentual_C:.2f}%')
print(f'Percentual de ratos: {percentual_R:.2f}%')
print(f'Percentual de sapos: {percentual_S:.2f}%')