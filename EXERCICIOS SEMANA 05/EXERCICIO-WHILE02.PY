#Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor
#mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o
#mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário.

num_min = int(input('Insira um número minimo: '))
num_max = int(input('Insira um número maximo: '))

if num_max > num_min:
    print(f'Os valores divisiveis por 5 entre {num_min} e {num_max} são: ')

    num = num_min

    while num <= num_max:
        if num % 5 == 0:
         print(num)
        num +=1
else:
    print('O valor máximo é menor que o valor minimo')


