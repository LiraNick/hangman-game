
def cadastroPessoa(player):
    """ Função criada para cadastrar o jogador no txt
    Args:
        player (Dict): Dicionário contendo as informações do jogador
    """
    
    with open('infouser.txt', 'a') as arquivo:  # abre o txt
        arquivo.write(str(player)+"\n")     # adiciona o dicionário ao txt


def atualizar(nome, resultado):
    """Função qcriada para atualizar as infomrações do jogador
    Args:
        nome (str): Nome / nickname do jogador 
        resultado (Boolean): Resultado do jogo (True venceu / False perdeu)
    """
    
    posicao = index = 0        # variável criada para validação do código
    flag = False
    infouser = open('infouser.txt', 'r')   # abre o TXT (leitura)
    player = {'nome':nome}      # Cria o dicionário e atribui o nome do Player
    
    
    ####### VALIDAÇÃO DO PLAYER NO TXT #######
    for linha in infouser:     # pra cada player de infouser
        if nome == eval(linha)['nome']:      # se nome for igual ao dicionário linha na posção nome e resultado for True
            player = eval(linha)     # encontra o player e coloca em um dicionário para alteração futura
            posicao = index
            flag = True       # validação
            
        else :
            index += 1
            
    infouser.close()    # fecha o arquivo
    
    
    ####### "PEGAR" AS INFORMAÇÕES DO PLAYER #######
    if flag :       # se o player já possuir um histórico 
        with open('infouser.txt', 'r') as ler:   # abre o TXT (leitura)
            linhas = ler.readlines()    # cada linha será uma str
            index = 0
            with open('infouser.txt', 'w') as escrever:     # abre o TXT (escrever no arquivo)
                for item in linhas:             # loop para percorrer linha por linha
                    if posicao != index:                    # se posição do loop for diferente da posição do player
                        escrever.write(item)       # escreva linha[c] no txt
                    index += 1
                
                
        ## ATUALIZAÇÃO DAS PORCENTAGENS
        
        player['qPartidas'] += 1    # adiciona + 1 jogo no histórico

        if resultado:   # se resultado for True (ganhou)
            player['vitorias'] += 1         # round(6.4654654984, 1) irá limiar o float a 1 decimal
            player['pVitorias'] = round(player['vitorias'] / player['qPartidas'] * 100, 1)    # cálculo para a porcentagem de vitorias
            player['pDerrotas'] = round(100 - player['pVitorias'], 1)        # cálculo para a porcentagem de derrotas
        
        else:   # perdeu
            player['derrotas'] += 1         # round(6.4654654984, 1) irá limiar o float a 1 decimal
            player['pDerrotas'] = round(player['derrotas'] / player['qPartidas'] * 100, 1)    # cálculo para a porcentagem de derrotas
            player['pVitorias'] = round(100 - player['pDerrotas'], 1)        # cálculo para a porcentagem de vitorias
        
        
        cadastroPessoa(player)   # função que adiciona o player no txt


    else :      # O player não possui um histórico
        
        ## INSERÇÃO DAS PORCENTAGENS 
        if resultado:   # se resultado for True (ganhou)
            player['vitorias'] = 1
            player['pVitorias'] = 100   # 100% de vitorias
            player['pDerrotas'] = 0
        
        else:   # perdeu
            player['derrotas'] = 1
            player['pDerrotas'] = 100   # 100% de derrotas
            player['pVitorias'] = 0
            
        
        cadastroPessoa(player)   # função que adiciona o player no txt


def estatisticas():
    """ Função criada para mostrar as estatisticas e infomrações dos
        Players no jogo
        ### Falta criar uma ordem por % de vitórias ###
    """
    
    infouser = open('infouser.txt', 'r')   # abre o TXT (leitura)
    
    for player in infouser:     # loop para acessar cada linha que estava no txt
        temp = eval(player)     # variável temporária para auxiliar na impressão
                                # eval() transforma em dicionário
        
        print(f'''Player: {temp['nome'].title()}
Quantidade de partidas: {temp['qPartidas']}
Vitórias: {temp['vitorias']}
Derrotas: {temp['derrotas']}
Percentual de Vitórias: {temp['pVitorias']}%
Percentual de Derrotas: {temp['pDerrotas']}%\n''')
            
        {'nome': 'Joao', 'qPartidas': 10, 'vitorias': 1, 'derrotas': 9, 'pVitorias': 10.0, 'pDerrotas': 90.0}    

