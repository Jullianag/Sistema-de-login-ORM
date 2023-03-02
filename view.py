from controller import ControllerCadastro, ControllerLogin

while True:
    print('\n-- Menu --\n'
          '1 - cadastrar\n'
          '2 - logar\n'
          '3 - Sair\n')

    decidir = int(input('Escolha: '))

    if decidir == 1:
        print('\n.:Cadastro de funcionário:.\n')
        nome = input('Digite seu nome: ')
        email = input('Digite seu e-mail: ')
        senha = input('Digite sua senha: ')
        senha2 = input('Confirme a senha: ')

        resultado = ControllerCadastro.cadastrar(nome, email, senha, senha2)

        if resultado == 2:
            print('Nome inválido!')
        elif resultado == 3:
            print('E-mail maior que o permitido!')
        elif resultado == 4:
            print('Senha inválida!')
        elif resultado == 5:
            print('E-mail já cadastrado na base de dados!')
        elif resultado == 6:
            print('Erro interno do sistema!')
        elif resultado == 7:
            print('As senhas devem ser iguais!')
        elif resultado == 1:
            print('Cadastro realizado com sucesso!')

    elif decidir == 2:
        print('\n.:Login:.\n')
        email = input('E-mail: ')
        senha = input('Senha: ')
        resultado = ControllerLogin.login(email, senha)

        if not resultado:
            print('Email ou senha inválidos!')
        else:
            print(resultado)
    else:
        print('Saindo do sistema...')
        break