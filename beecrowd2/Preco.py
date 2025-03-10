
N,Q = map(int,input().split())

preco = 0


if N == 1:
    preco = Q * 4
if N == 2:
  preco =  Q * 4.50
if N == 3:
   preco = Q * 5
if N == 4:
   preco = Q * 2
if N == 5:
   preco = Q * 1.50

print(preco)
    

