password = 2002
senha = int(input('DIgite a senha'))

while senha !=2002:
    print('Acesso negado')
    senha = int(input('Digite a senha'))
    
    if senha == 2002:
        print('Acesso concedido')
