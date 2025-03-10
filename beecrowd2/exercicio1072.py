N = int(input())

dentro = 0
out = 0

for lista in range(N):
    X = int(input())
    if X >= 10 and X <= 20:
        dentro +=1
    else:
        out +=1
        
print(f'{dentro} dentro')
print(f'{out} out')

