import json

arquivo = open('memoria.txt','r')
conteudo = arquivo.read()
estoque = json.loads(conteudo) 
arquivo.close()
    
i = True

while i:
    print('')
    print('\033[4m\033[95mControle de estoque:\033[0m')
    print('0 - sair')
    print('1 - adicionar item')
    print('2 - remover item')
    print('3 - alterar item')
    print('4 - imprimir estoque')
    
    escolha = input('Faça sua escolha: ')
    
    
    
# Escolha numero 1, adicionar item nao existente 
    
    if escolha == '1':
        
        produto = input('Nome do produto: ')
        nome = produto.lower()
        
        if nome not in estoque:
        
            a = True  
            while a:
                Qinicial = float(input('Quantidade inicial: '))
                
                
                if Qinicial < 0:
                    print('\033[91mA quantidade inicial não pode ser negativa.\033[0m')
                    
                else:
                    a = False
                    
                    
            b = True
            while b:        
                rs = float(input('Valor unitário do produto: '))   
                
                if rs < 0:
                    print('\033[91mO valor do produto não pode ser negativo.\033[0m')
                    
                else:
                    b = False
                    estoque[nome] = {'quantidade' : Qinicial, 'valor' : rs}
        
        else:
            print('\n\033[91mProduto ja cadastrado\033[0m')

        arquivo = open('memoria.txt','w')
        conteudo = json.dumps(estoque, sort_keys=True, indent=4)
        arquivo.write(conteudo)
        arquivo.close()

# Escolha numero 2, remover item  

    elif escolha == '2':
        
        produto = input('Nome do produto: ')
        nome = produto.lower()
        
        if nome not in estoque:
            print('\n\033[91mElemento não encontrado\033[0m')
        
        else:
            del estoque[nome]
            print('Elemento Removido')

        arquivo = open('memoria.txt','w')
        conteudo = json.dumps(estoque, sort_keys=True, indent=4)
        arquivo.write(conteudo)
        arquivo.close()
            
# Escolha numero 3, alterar item   

    elif escolha == '3':
        
        produto = input('Nome do produto: ')
        nome = produto.lower()
        
        if nome in estoque: 
            
            resposta = int(input('Alterar Quantidade ou Valor unitario? (1 ou 2): '))    
            
            if resposta == 1:
                quan = float(input('Alteração na Quantidade: '))
                
                resultado = estoque[nome]['quantidade'] + quan
                
                estoque[nome]['quantidade'] = resultado
                
                print('Novo estoque de {0} : {1}'.format(nome, estoque[nome]['quantidade']))
                
            elif resposta == 2:
                quan = float(input('Alteração no Valor: '))
                
                resultado = estoque[nome]['valor'] + quan
                
                estoque[nome]['valor'] = resultado
                
                print('Novo valor de {0} : {1}'.format(nome, estoque[nome]['valor']))
        
        else:
            print('\n\033[91mElemento não encontrado\033[0m')

        arquivo = open('memoria.txt','w')
        conteudo = json.dumps(estoque, sort_keys=True, indent=4)
        arquivo.write(conteudo)
        arquivo.close()

# Escolha numero 4, printar estoque    

    elif escolha == '4':
        
        soma = 0
        
        print('')
        print('\033[95mEstoques:\033[0m')
        for k in estoque:
            if estoque[k]['quantidade'] >= 0:
                print(' - {0} : {1}'.format(k, estoque[k]['quantidade']))
         
        print('')
        print('\033[95mEstoques negativos:\033[0m')
        for k in estoque:
            if estoque[k]['quantidade'] < 0:
                print(' - {0} : {1} '.format(k, estoque[k]['quantidade']))
        
        for l in estoque:
            soma += estoque[l]['valor'] * estoque[l]['quantidade']
        
        print('')
        print(f'\033[94mValor monetario:\033[0m R${round(soma, 2)}')
                

# Escolha numero 0, Interromper programa

    elif escolha == '0':
        i = False
    
    else:
        print('\n\033[91mEscolha inválida\033[0m')
    
    
arquivo = open('memoria.txt','w')
conteudo = json.dumps(estoque, sort_keys=True, indent=4)
arquivo.write(conteudo)
arquivo.close()

print('\n\033[1m\033[94mAté mais!\033[0m\n')