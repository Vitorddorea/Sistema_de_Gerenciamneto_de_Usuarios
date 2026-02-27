from datetime import date

def titulos(txt):
    print('=' * 30)
    print(txt.center(30))
    print('=' * 30)

def menu(): 

    titulos('CADASTRADOR DE USUÁRIOS')
    print('1 - Casdatrar usuários')
    print('2 - Listar usuários')
    print('3 - Atualizar usuários')
    print('4 - Deletar usuários')
    print('0 - Encerrar programa')
    print('=' * 30)

def lerInt(txt):
    while True:
        try:
            return int(input(txt))
        except ValueError:
            print('\033[31mDigite um valor válido! \033[m')

def cadastrarUsuarios(usuarios):

    titulos('Cadastrar Usuários')

    usuario = {}
    usuario['ID'] = len(usuarios) + 1 
    usuario['Nome'] = input('Nome: ')
    nasc = lerInt('Ano de Nascimento: ')
    usuario['Idade'] = date.today().year - nasc
    usuarios.append(usuario)

def listarUsuarios(usuarios):
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
        print('Atualizar')
    elif opcao == 4:
        print('Deletar')
    elif opcao == 0:
        print('Encerrando programa... ')
