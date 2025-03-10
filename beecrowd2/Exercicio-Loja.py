while True:
    cod, qtde, preco = input().split() 
    qtde = float(qtde)
    preco = float(preco)
    
    infantil, feminina, masculina = 0,0,0
    invalidos = []
    
    linha = int(cod[:3])  
    
    if 100 <= linha <= 399:
        infantil += qtde * preco
    elif 400 <= linha <= 799:
        feminina += qtde * preco
    else:
        masculina += qtde * preco

    if len(cod) != 7:
        invalidos.append(cod)
    
    if cod == "0":  
        break

total = infantil + feminina + masculina

print("Subtotais")
print("Linha Infantil = {:.2f}".format(infantil))
print("Linha Feminina = {:.2f}".format(feminina))
print("Linha Masculina = {:.2f}\n\n".format(masculina))
print("Total Geral = {:.2f}\n\n".format(total))
print("Inconsistencias\n")

if len(invalidos) == 0:
    print("Não há inconsistências")
else:
    print("Código inválido: {}".format(invalidos))