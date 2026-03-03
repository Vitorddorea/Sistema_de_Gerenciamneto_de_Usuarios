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

    print('1 - Cadastrar usuários')
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

def criarID(usuarios):
    """
    Cria um ID único
    :param usuarios: lista de usuários
    """
    
    if not usuarios:
        return 1
    else:
        ultimo_id = max(usuario['ID'] for usuario in usuarios)
        return ultimo_id + 1

def lerNasc():
    """
    Retorna um ano de nascimento válido
    """

    while True:
        nasc = lerInt('Ano de Nascimento: ')
        if 1900 < nasc < date.today().year:
            break
        else:
            print('\033[31mDigite um ano válido!\033[m')

    return nasc

def cadastrarUsuarios(usuarios):
    """
    Registra usuários e guarda na lista de usuários
    :param usuarios: lista de usuários
    """

    titulos('Cadastrar Usuários')

    usuario = {}

    usuario['ID'] = criarID(usuarios)
    usuario['Nome'] = input('Nome: ')

    nasc = lerNasc()

    usuario['Idade'] =  date.today().year - nasc
    usuarios.append(usuario)

    print('Usuário cadastrado!')

def listarUsuarios(usuarios):
    """
    Lista todos usuários cadastrados
    :param usuarios: lista de usuários
    """

    titulos('Usuários cadastrados')

    if not usuarios:
        print('Nenhum usuários cadastrado!')
    else:
        for usuario in usuarios:
            print(f'ID: {usuario["ID"]} | Nome: {usuario["Nome"]} | Idade: {usuario["Idade"]} anos')

def atualizarUsuario(usuarios):
    """
    Atualiza um usuário com base no seu ID
    :param usuarios: lista de usuários
    """

    titulos('Atualizar usuários')

    encontrado = False

    for usuario in usuarios:
        if usuario['ID'] == opcao:
            usuario['Nome'] = input('Nome: ')
            nasc = lerNasc()
            usuario['Idade'] = date.today().year - nasc
            encontrado = True
            break

    if encontrado:
        print(f'Usuário do ID {opcao} atualizado!')
    else:
        print('Usuário não encontrado.')

def deletarUsuario(usuarios):
    """
    Deleta um usuário com base no seu ID
    :param usuarios: lista de usuários
    """
    
    titulos('Deletar usuário')

    if not usuarios:
        print('Nenhum usuários cadastrado!')
    else:
        listarUsuarios(usuarios)

        opcao = lerInt('Qual usuário você deseja deletar? ID: ')

        for usuario in usuarios:
            if usuario['ID'] == opcao:
                usuarios.remove(usuario)

        print('Usuário do ID {opcao} deletado!')
    
usuarios = []

while True:
    menu()

    while True:
        opcao = lerInt('Escolha uma opção: ')
        if opcao not in (1, 2, 3, 4, 0):
            print('\033[31m Digite uma opção válida! \033[m')
        else:
            break

    if opcao == 1: 
        cadastrarUsuarios(usuarios)
    elif opcao == 2:
        listarUsuarios(usuarios)
    elif opcao == 3:
        atualizarUsuario(usuarios)
    elif opcao == 4:
        deletarUsuario(usuarios)
    elif opcao == 0:
        print('Encerrando programa... ')
        break
        
        