import json

negativo = []

with open ('memoria.txt','r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo) 
    
i = 0 

while i == 0:
    print('')
    print('Controle de estoque')
    print('0 - sair')
    print('1 - adicionar item')
    print('2 - remover item')
    print('3 - alterar item')
    print('4 - imprimir estoque')
    
    escolha = input('Faça sua escolha: ')
    
    
    
# Escolha numero 1, adicionar item nao existente ************   FEITO   *******
    
    if escolha == '1':
        
        produto = input('Nome do produto: ')
        nome = produto.lower()
        
        if nome not in estoque:
        
            a = True  
            while a:
                Qinicial = float(input('Quantidade inicial: '))
                
                
                if Qinicial < 0:
                    print('A quantidade inicial não pode ser negativa.')
                    
                else:
                    a = False
                    
                    
            b = True
            while b:        
                rs = float(input('Valor unitário do produto: '))   
                
                if rs < 0:
                    print('O valor do produto não pode ser negativo.')
                    
                else:
                    b = False
                    estoque[nome] = {'quantidade' : Qinicial, 'valor' : rs}
        
        else:
            print('Produto ja cadastrado')
        
                
        
        with open ('memoria.txt','w') as arquivo:
            conteudo = json.dumps(estoque, sort_keys=True, indent=4)
            arquivo.write(conteudo)




# Escolha numero 2, remover item ****************************   FEITO   *******     

    elif escolha == '2':
        
        produto = input('Nome do produto: ')
        nome = produto.lower()
        
        if nome not in estoque:
            print('Elemento não encontrado')
        
        else:
            del estoque[nome]
            print('Elemento Removido')

        with open ('memoria.txt','w') as arquivo:
            conteudo = json.dumps(estoque, sort_keys=True, indent=4)
            arquivo.write(conteudo)   
            
# Escolha numero 3, alterar item ****************************   FEITO   *******      

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
            print('Elemento não encontrado')
            
        with open ('memoria.txt','w') as arquivo:
            conteudo = json.dumps(estoque, sort_keys=True, indent=4)
            arquivo.write(conteudo)
        
# Escolha numero 4, printar estoque *************************   FEITO   *******   

    elif escolha == '4':
        
        soma = 0
        
        print('')
        print('Estoques:')
        for k in estoque:
            if estoque[k]['quantidade'] >= 0:
                print(' -{0} : {1}'.format(k, estoque[k]['quantidade']))
         
        for k in estoque:
            if estoque[k]['quantidade'] < 0:
                    negativo.append(nome)
                    
        print('')
        print('Estoques negativos:')
        for j in negativo:
            print(' -{0} : {1} '.format(j, estoque[j]['quantidade']))
        
        for l in estoque:
            soma += estoque[l]['valor'] * estoque[l]['quantidade']
        
        print('')
        print('Valor monetario: R${0}'.format(soma))
                

# Escolha numero 0, Interromper programa ********************   FEITO   *******   

    elif escolha == '0':
        i = 1
    
    else:
        print('Escolha inválida')
    
    
with open ('memoria.txt','w') as arquivo:
    conteudo = json.dumps(estoque, sort_keys=True, indent=4)
    arquivo.write(conteudo)

print('Até mais')