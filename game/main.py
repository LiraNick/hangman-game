from controller import atualizar, estatisticas, sorteioPalavras

def menu():
    print('JOGO DA FORÇA'.center(25, ' '))
    print('Escolha uma das opções:')
    opcao = int(input('1 - Jogar \n2 - Estatísticas \n3 - Sair\n=> '))
    
    if opcao == 1:  # JOGAR
        print()
        palavra = sorteioPalavras().strip()     # função que escolhe a palavra referente ao nível selecionado
        
        
    print(palavra)
    print(palavra[-1])
    
    
    
menu()