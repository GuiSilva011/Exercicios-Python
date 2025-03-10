#Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. 
# Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
#Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. 
# Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

#ENTRADA
#A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. 
# Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere 
# Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

#SAIDA
#Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, 
# sendo que o percentual deve ser apresentado com dois dígitos após o ponto.



N = int(input())

cont = 0

soma_C = 0
soma_R = 0
soma_S = 0



while cont < N:
    C = 0
    R = 0
    S = 0
    
    C = int(input())
    R = int(input())
    S = int(input())
    
    soma_C += C
    soma_R += R
    soma_S += S
    
    soma = soma_C + soma_R + soma_S
    
    percentual_C = (soma_C /soma )*100
    percentual_R = (soma_R / soma) * 100
    percentual_S = (soma_S / soma) * 100
    cont = cont + 1

print(f'Total: {soma} cobaias')
print(f'Total de coelhos: {soma_C}')
print(f'Total de ratos: {soma_R}')
print(f'Total de sapos: {soma_S}')
print(f'Percentual de coelhos: {percentual_C:.2f}')
print(f'Percentual de ratos: {percentual_R:.2f}')
print(f'Percentual de sapos: {percentual_S:.2f}')