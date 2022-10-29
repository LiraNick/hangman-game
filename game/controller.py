

def atualizar(nome, resultado):
    # NOME str
    # resultado Boolean
    posicao = index = 0        # variável criada para validação do código
    flag = False
    infouser = open('infouser.txt', 'r')   # abre o TXT (leitura)

    for linha in infouser:     # pra cada player de infouser
        if nome == eval(linha)['nome']:      # se nome for igual ao dicionário linha na posção nome e resultado for True
            player = eval(linha)     # encontra o player e coloca em um dicionário para alteração futura
            posicao = index
            flag = True       # validação
            
        else :
            index += 1
            
    infouser.close()    # fecha o arquivo
    
    if flag :
        with open('infouser.txt', 'r') as ler:   # abre o TXT (leitura)
            linhas = ler.readlines()    # cada linha será uma str
            index = 0
            with open('infouser.txt', 'w') as escrever:     # abre o TXT (escrever no arquivo)
                for item in linhas:             # loop para percorrer linha por linha
                    if posicao != index:                    # se posição do loop for diferente da posição do player
                        escrever.write(item)       # escreva linha[c] no txt
                    index += 1
                    
    ######  até aqui apaga no nome do txt #######
    # precisa colocar no txt com as informações atualizadas 
    # as informações anteriores do player estão no dicionário player
    # criar uma função com valores pré-estabelecidos para inserção de dados c
    
    
      
        print(type(player))             
                    
                    
                    
                    
    
    else :
        print('não possui nome no txt') # se o flag for false 
        ######  inserir o player no txt com os dados  ######
