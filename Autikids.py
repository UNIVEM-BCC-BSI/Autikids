import pyttsx3
USUÁRIOS = []; SENHAS = []; logado = False
while not logado:
    escolha = (input('\nSelecione uma opção:\n• [1] Fazer Login\n• [2] Criar conta\nR: '))
    if escolha == '1':
        nome_usuario = input('\n•Usuário: ')
        senha_usuario = input('•Senha: ')
        if nome_usuario in USUÁRIOS and senha_usuario in SENHAS:
            logado = True
            break
        else:
            print('\n•Senha ou usuário inválidos. Tente novamente')
    elif escolha == '2':
        nome_usuario = input('\n•Escolha seu nome de usuário: ')
        senha_usuario = input('•Escolha sua senha: ')
        USUÁRIOS.append(str(nome_usuario))
        SENHAS.append(str(senha_usuario))
        print(f'\n•Usuário {nome_usuario} cadastrado com sucesso.')
    else:
        print('\n•Opção inválida. Tente novamente.')

while logado:
    escolha = (input(f'\nOlá, {nome_usuario}!\n•MENU DE INTERAÇÕES:\n\n•[0]Sair\n•[1]Apresentações\n•[2]Estou com fome\n•[3]Estou com sede\n•[4]Quero isso\n•[5]Quero aquilo\n•[6]Me ajude\n•[7]Preciso ir ao banheiro\n\n•R: '))
    if escolha == '0':
        while True:
            s = pyttsx3.init()
            data = "Tem certeza que quer sair?"
            s.say(data)
            s.runAndWait()
            sair = input('\n•Tem certeza que quer sair?\n[0]SIM\n[1]NÃO\nR: ')
            if sair == '0':
                print(f'\nAté mais, {nome_usuario}.')
                s = pyttsx3.init()
                data = f"Até mais, {nome_usuario}."
                s.say(data)
                s.runAndWait()
                exit()
            elif sair == '1':
                break
            else:
                print('\n•Opção inválida. Tente novamente.')
                s = pyttsx3.init()
                data = "Opção inválida. Tente novamente."
                s.say(data)
                s.runAndWait()
    elif escolha == '1':
        s = pyttsx3.init()
        data = f"Olá! Meu nome é {nome_usuario}. Qual seu nome?"
        s.say(data)
        s.runAndWait()
    elif escolha == '2':
        s = pyttsx3.init()
        data = "Estou com fome."
        s.say(data)
        s.runAndWait()
    elif escolha == '3':
        s = pyttsx3.init()
        data = "Estou com sede."
        s.say(data)
        s.runAndWait()
    elif escolha == '4':
        s = pyttsx3.init()
        data = "Quero isso."
        s.say(data)
        s.runAndWait()
    elif escolha == '5':
        s = pyttsx3.init()
        data = "Quero aquilo."
        s.say(data)
        s.runAndWait()
    elif escolha == '6':
        s = pyttsx3.init()
        data = "Me ajude!"
        s.say(data)
        s.runAndWait()
    elif escolha == '7':
        s = pyttsx3.init()
        data = "Preciso ir ao banheiro."
        s.say(data)
        s.runAndWait()
    else:
        print('\n•Opção inválida. Tente novamente.')
        s = pyttsx3.init()
        data = "Opção inválida. Tente novamente."
        s.say(data)
        s.runAndWait()
