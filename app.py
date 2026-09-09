import os

restaurantes = [{'nome' : 'Sushi Bar', 'categoria' : 'Japonesa', 'ativo' : False}]

def digite_tecla() :
    '''Retorna a tela de menu principal.
    
    Input: Recebe uma informação qualquer.

    Output: Retorna para a tela de menu principal.

    '''

    input('\nDigite Enter para retornar para o menu principal.')
    main()

def  exibir_subtitulo(texto) :
    ''' Limpa o console e em seguida exibe o subtítulo da opção escolhida
    
    Input: Recebe o subtitulo a ser exibido.

    Output: Exibe o subtitulo com uma moldura.

    '''

    os.system('cls')
    linha = '-' * (len(texto) + 4)
    print(linha)
    print(f'{texto}')
    print(f'{linha}\n')


def nome_programa():
    '''Exibe o titulo principal do programa.'''

    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
''')
    
def exibir_opcoes() : 
    '''Exibe as opções disponíveis do programa'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def finalizar_app() :
    '''Exibe a mensagem de finalização do programa.'''

    exibir_subtitulo('Programa Finalizado...')

def opcao_invalida() :
    '''Exibe a mensagem de opção inválida e em seguida exibe a mensagem de retorno ao menu principal.'''

    print('Opção Inválida\n')
    digite_tecla()

def cadastrar_restaurante() :
    '''Esta função serve para cadastrar um novo restaurante à lista de restaurantes.
    
    Inputs:
    - Nome do Restaurante
    - Categoria do Restaurante

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes.
    '''

    exibir_subtitulo('Cadastro de novos restaurantes: ')
    nome_restaurante = input('Defina o nome do Restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria_restaurante, 'ativo' : False}
    if nome_restaurante != '' and categoria_restaurante != '' :
        restaurantes.append(dados_restaurante)
        print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
        digite_tecla()
    else:
        print('\nNome ou Categoria inválidos')
        digite_tecla()

def restaurantes_listados() :
    ''' Exibe os restaurantes cadastrados, seus nomes, categorias, e status atual.'''

    exibir_subtitulo('Restaurantes listados: ')
    print(f'{'Nome Restaurante:'.ljust(22)} | {'Categoria:'.ljust(20)} | {'Status:'}')
    for restaurante in restaurantes :
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativo' if restaurante['ativo'] == True else 'Desativo'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    digite_tecla()

def mudar_estado_restaurante() :
    ''' Altera o estado atual de um restaurante, de Ativo para Desativo e visse versa.
    
    Input: Recebe o nome da função a ter seu status alterado.
    
    Output: Altera o status do restaurante de Desativo para Ativo e visse versa.
    '''

    exibir_subtitulo('Alterando estado do restaurante: ')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes :
        if nome_restaurante == restaurante['nome'] :
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] == True else f'\nO restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'\nO restaurante {nome_restaurante} não foi encontrado')
    digite_tecla()


def escolha_opcao() : 
    ''' Recebe a opção escolhida pelo usuário, e direciona-o para as outras interfaces.
    
    Input: Recebe a opção numérica de 1 a 4.

    Output: Abre a Interface escolhida pelo usuário.
    '''
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1 :
            cadastrar_restaurante()
        elif opcao_escolhida == 2 :
            restaurantes_listados()
        elif opcao_escolhida == 3 :
            mudar_estado_restaurante()
        elif opcao_escolhida == 4 :
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main() : 
    '''Exibe o menu principal do sistema.'''

    os.system('cls')
    nome_programa()
    exibir_opcoes()
    escolha_opcao()

if __name__ == '__main__' : 
    main()