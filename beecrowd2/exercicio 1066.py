cont = 0
impares = 0
pares = 0
negativos = 0
positivos = 0


while cont < 9:
    num = int(input())
    if num < 0:
        negativos +=1
        cont +=1  
    if num >= 0:
         positivos +=1
         cont +=1 
    if num % 2 == 0:
         pares +=1
         cont +=1 
    if num % 2 != 0:
         impares +=1
         cont +=1 

print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')