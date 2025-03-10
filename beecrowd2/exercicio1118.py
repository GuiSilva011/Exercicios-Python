novo_calc = 1
while novo_calc == 1:
    nota_valida = 0
    media = 0
    
    while nota_valida != 2:
        notas = float(input())
        if 0 <= notas <= 10:
            media += notas / 2
            nota_valida += 1
        else:
            print('nota invalida')
    
    print(f'media = {media:.2f}')
    
    continua = 0  
    
    while continua != 1 and continua != 2:
        continua = int(input('novo calculo (1-sim 2-nao)\n'))
        if continua == 1:
            novo_calc = 1
        elif continua == 2:
            novo_calc = 2
        


    
    
