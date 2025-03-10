import math

a, b, c = map(float, input().split())


eq1 = (b**2) - (4*a*c)
if eq1 < 0 or a == 0:
 print('Impossivel calcular')
 
else:
    bhaskara = math.sqrt(eq1)
    
    R1 = (-b + bhaskara) / (2 * a)
    R2 = (-b - bhaskara) / (2 * a)

    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
    