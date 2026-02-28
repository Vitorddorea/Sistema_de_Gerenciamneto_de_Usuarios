from datetime import date

def titulos(txt):
    """
    -> Padronizador de títulos
    :param txt: o texto do título
    """

    print('=' * 30)
    print(txt.center(30))
    print('=' * 30)


def menu(): 
    """
    -> Menu do programa
    """

    titulos('CADASTRADOR DE USUÁRIOS')

    print('1 - Casdatrar usuários')
    print('2 - Listar usuários')
    print('3 - Atualizar usuários')
    print('4 - Deletar usuários')
    print('0 - Encerrar programa')
    print('=' * 30)


def lerInt(txt):
    """
    -> Retorna um número inteiro
    :param txt: texto do input
    """

    while True:
        try:
            return int(input(txt))
        except ValueError:
            print('\033[31mDigite um valor válido! \033[m')


def cadastrarUsuarios(usuarios):
    """
    Registra usuários e guarda na lista de usuários
    :param usuarios: lista de usuários
    """

    titulos('Cadastrar Usuários')

    usuario = {}
    usuario['ID'] = len(usuarios) + 1 
    usuario['Nome'] = input('Nome: ')

    while True:
        nasc = lerInt('Ano de Nascimento: ')
        if 1900 < nasc < date.today().year:
            break
        else:
            print('\033[31mDigite um ano válido!\033[m')

    usuario['Idade'] =  date.today().year - nasc
    usuarios.append(usuario)

def listarUsuarios(usuarios):
    """
    Lista todos usuários cadastrados
    :param usuarios: lista de usuários
    """

    titulos('Usuários cadastrados')

    for usuario in usuarios:
        print(f'ID: {usuario["ID"]} | Nome: {usuario["Nome"]} | Idade: {usuario["Idade"]} anos')


#def atualizarUsuario(usuarios):

#def deletarUsuario():

usuarios = []

while True:
    menu()

    opcao = lerInt('Escolha uma opção: ')

    if opcao == 1: 
        cadastrarUsuarios(usuarios)
    elif opcao == 2:
        listarUsuarios(usuarios)
    elif opcao == 3:
        print('Funcao em desenvolvimento')
        print('Atualizar')
    elif opcao == 4:
        print('Funcao em desenvolvimento')
        print('Deletar')
    elif opcao == 0:
        print('Encerrando programa... ')
        break