#OBS: Em todas as linhas: "ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')" altere o caminho do arquivo para que funcione corretamente.

from tkinter import *
from tkinter import messagebox
from customtkinter import *
import playsound as ps
import sqlite3
import pyttsx3

def cadastrar_aluno():

    ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
    conexao = sqlite3.connect('banco_alunos2.db')
    cursor=conexao.cursor()
    cursor.execute("INSERT INTO alunos VALUES(:nome,:sobrenome,:telefone,:datadenascimento,:endereco,:cep,:bairro)",
        {
                'nome':entry_nomeAluno.get(),
                'sobrenome':entry_sobrenome.get(),
                'telefone':entry_telefone.get(),
                'datadenascimento':entry_datadenascimento.get(),
                'endereco':entry_endereco.get(),
                'cep':entry_cep.get(),
                'bairro':entry_bairro.get(),
        })

    conexao.commit()
    conexao.close()
        
    entry_nomeAluno.delete(0,"end")
    entry_sobrenome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_datadenascimento.delete(0,"end")
    entry_endereco.delete(0, "end")
    entry_cep.delete(0,"end")
    entry_bairro.delete(0,"end")

def logado():
    
    ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
    entryInputEmail.destroy()
    entryInputSenha.destroy()
    botãoVoltarMenu.destroy()
    botãoConfirmarLog.destroy()
    labelInputLogin.destroy()
    labelInputSenha.destroy()
    labelLogTitle.destroy()
    
    def semcomando():
        ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
        print("")
    
    def NovoCadastro():

        ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
        canvasHud2.destroy()
        b_Alimentacao.destroy()
        b_Interacao.destroy()
        logo.destroy()

        global entry_nomeAluno
        global entry_sobrenome
        global entry_telefone
        global entry_datadenascimento
        global entry_endereco
        global entry_cep
        global entry_bairro

        label_titulo = Label(janela, text='Cadastro de aluno')
        label_titulo.configure(font=('Poppins', 20, 'bold'), bg='orange', fg='white')
        label_titulo.grid(row=0, column=1, columnspan=1)

        label_nome= Label(janela, text='Nome: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
        label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        label_sobrenome= Label(janela, text='Sobrenome: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
        label_sobrenome.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        label_telefone= Label(janela, text='Telefone: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
        label_telefone.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        label_datadenascimento= Label(janela,text='Data de Nascimento: ',bg='orange',fg='black',border=2, font=('Poppins 12 bold'))
        label_datadenascimento.grid(row=4,column=0,padx=10,pady=10, sticky='e')

        label_endereco= Label(janela, text='Endereço: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
        label_endereco.grid(row=5, column=0, padx=10, pady=10, sticky='e')

        label_cep= Label(janela, text='CEP: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
        label_cep.grid(row=6, column=0, padx=10, pady=10, sticky='e')

        label_bairro= Label(janela, text='Bairro: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
        label_bairro.grid(row=7, column=0, padx=10, pady=10, sticky='e')

        # Entrys:
            
        entry_nomeAluno= Entry(janela, width=30, border=2, font=('Poppins 12'))
        entry_nomeAluno.grid(row=1, column=1, pady=10)

        entry_sobrenome= Entry(janela,width=30, border=2, font=('Poppins 12'))
        entry_sobrenome.grid(row=2, column=1, pady=10)

        entry_telefone= Entry(janela,width=30, border=2, font=('Poppins 12'))
        entry_telefone.grid(row=3, column=1, pady=10)

        entry_datadenascimento= Entry(janela,width=30, border=2, font=('Poppins 12'))
        entry_datadenascimento.grid(row=4,column=1,pady=10)

        entry_endereco= Entry(janela,width=30, border=2, font=('Poppins 12'))
        entry_endereco.grid(row=5, column=1, pady=10)

        entry_cep= Entry(janela,width=30, border=2, font=('Poppins 12'))
        entry_cep.grid(row=6, column=1, pady=10)

        entry_bairro= Entry(janela,width=30, border=2, font=('Poppins 12'))
        entry_bairro.grid(row=7, column=1, pady=10)

        # Botoes:
        botao_cadastar= Button(janela,text="Cadastrar Aluno", command = cadastrar_aluno, border=2, font=('Poppins 12 bold'), activebackground='yellow')
        botao_cadastar.grid(row=8,column=1,pady=10, sticky='nswe')

        janela.mainloop()
    
    def interacao():
        
        logo.destroy()
        b_Alimentacao.destroy()
        b_Interacao.destroy()
        canvasHud2.destroy()

        def b1():
            ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
            s = pyttsx3.init()
            data = f"Olá! Meu nome é José. Qual seu nome?"
            s.say(data)
            s.runAndWait()

        def b2():
            ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
            s = pyttsx3.init()
            data = f"Estou com fome."
            s.say(data)
            s.runAndWait()

        def b3():
            ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
            s = pyttsx3.init()
            data = f"Estou com sede."
            s.say(data)
            s.runAndWait()
            
        def b4():
            ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
            s = pyttsx3.init()
            data = f"Onde fica o banheiro?"
            s.say(data)
            s.runAndWait()
            
        def b5():
            ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
            s = pyttsx3.init()
            data = f"Preciso de ajuda!"
            s.say(data)
            s.runAndWait()
            
        def b6():
            ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
            s = pyttsx3.init()
            data = f"Quero isso."
            s.say(data)
            s.runAndWait()
            
        def b7():
            ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
            s = pyttsx3.init()
            data = f"Quero aquilo."
            s.say(data)
            s.runAndWait()
            
        def b8():
            ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
            s = pyttsx3.init()
            data = f"Obrigado."
            s.say(data)
            s.runAndWait()

        janela.wm_minsize(width=1450, height=800)
        janela.wm_maxsize(width=1450, height=800)
        
        imgLogo = PhotoImage(file='logo2.png')
        l_logo = Label(janela, image=imgLogo, bg = 'orange')
        l_logo.grid(pady=20, row=0, sticky='wens', columnspan=4)

        imgApresentações = PhotoImage(file='botão_apresentações.png')
        b_Apresentações = Button(janela, image=imgApresentações, bg = 'orange', border=0, activebackground='orange', command=b1)
        b_Apresentações.grid(column = 0, row=1, sticky='we', padx=35)

        imgFome = PhotoImage(file='botão_fome.png')
        b_Fome = Button(janela, image=imgFome, bg = 'orange', border=0, activebackground='orange', command=b2)
        b_Fome.grid(column = 1, row=1, sticky='we', padx=35)

        imgSede = PhotoImage(file='botão_sede.png')
        b_Sede = Button(janela, image=imgSede, bg = 'orange', border=0, activebackground='orange', command=b3)
        b_Sede.grid(column = 2, row=1, sticky='we', padx=35)

        imgBanheiro = PhotoImage(file='botão_banheiro.png')
        b_Banheiro = Button(janela, image=imgBanheiro, bg = 'orange', border=0, activebackground='orange', command=b4)
        b_Banheiro.grid(column = 3, row=1, sticky='we', padx=35)

        imgAjuda = PhotoImage(file='botão_ajuda.png')
        b_Ajuda = Button(janela, image=imgAjuda, bg = 'orange', border=0, activebackground='orange', command=b5)
        b_Ajuda.grid(column = 0, row=2, sticky='we', padx=35, pady=20)

        imgIsso = PhotoImage(file='botão_isso.png')
        b_Isso = Button(janela, image=imgIsso, bg = 'orange', border=0, activebackground='orange', command=b6)
        b_Isso.grid(column = 1, row=2, sticky='we', padx=35, pady=20)

        imgAquilo = PhotoImage(file='botão_aquilo.png')
        b_Aquilo = Button(janela, image=imgAquilo, bg = 'orange', border=0, activebackground='orange', command=b7)
        b_Aquilo.grid(column = 2, row=2, sticky='we', padx=35, pady=20)

        imgObrigado = PhotoImage(file='botão_obrigado.png')
        b_Obrigado = Button(janela, image=imgObrigado, bg = 'orange', border=0, activebackground='orange', command=b8)
        b_Obrigado.grid(column = 3, row=2, sticky='we', padx=35, pady=20)

        janela.config(bd=10)
        janela.mainloop()
    
    barrademenus=Menu(janela)
    menuAlunos=Menu(barrademenus,tearoff=0)
    menuAlunos.add_command(label="Novo Cadastro",command=NovoCadastro)
    menuAlunos.add_command(label="Pesquisar",command=semcomando)
    menuAlunos.add_separator()
    menuAlunos.add_command(label="Fechar",command=janela.quit)
    barrademenus.add_cascade(label="Alunos",menu=menuAlunos)

    menuconfiguracao=Menu(barrademenus,tearoff=0)
    menuconfiguracao.add_command(label="Login",command=semcomando)
    menuconfiguracao.add_command(label="Ajustes",command=semcomando)
    barrademenus.add_cascade(label='Configurações',menu=menuconfiguracao)

    janela.config(menu=barrademenus)

    imgLogo=PhotoImage(file="logo2.png")
    logo=Label(janela,image=imgLogo,bg='orange')
    logo.grid(row=0, columnspan=2, pady=50)

    imgCanvas = PhotoImage(file='canvas2.png')
    canvasHud2 = Canvas(janela, width=640, height=329, bg='orange', highlightthickness=0)
    canvasHud2.create_image(0, 0, image=imgCanvas, anchor='nw')
    canvasHud2.grid(columnspan=2, rowspan=2)

    imgAlimentacao = PhotoImage(file='botão_alimentação.png')
    b_Alimentacao = Button(janela, image=imgAlimentacao, bg='white', border=0, activebackground='white', command=semcomando)
    b_Alimentacao.grid(row=1, column=1, pady=25)

    imgInteracao = PhotoImage(file='botão_interações.png')
    b_Interacao = Button(janela, image=imgInteracao, bg='white', border=0, activebackground='white', command=interacao)
    b_Interacao.grid(row=1, column=0, pady=25)

    janela.config(menu=barrademenus)

    janela.config(bd=150)
    janela.mainloop()

#banco de dados funcionário
def cadastrar_cliente():
    
    global conexao
    global c
    
    global nomeUp
    global sobrenomeUp
    global emailUp
    global telefoneUp
    global senhaUp
    
    ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
    
    conexao = sqlite3.connect('funcionários.db')
    c = conexao.cursor()
    
    nomeUp = entryNome.get().strip()
    sobrenomeUp = entrySobrenome.get().strip()
    emailUp = entryEmail.get().strip()
    telefoneUp = entryTelefone.get().strip()
    senhaUp = entrySenha.get().strip()
    
    if not nomeUp or not sobrenomeUp or not emailUp or not telefoneUp or not senhaUp:
        messagebox.showerror(title='Autikids Cadastro', message='Preencha todos os campos.')
        
    elif len(senhaUp) < 8:
        
        messagebox.showerror(title='Autikids Cadastro', message='Sua senha deve ter no mínimo 8 caracteres.')
        entrySenha.delete(0,"end")
        
    elif nomeUp.upper() in senhaUp.upper() or senhaUp.upper() in nomeUp.upper():
        
        messagebox.showerror(title='Autikids Cadastro', message='Sua senha não pode conter seu nome ou vice-versa.')
        entrySenha.delete(0,"end")
    
    else:
        
        c.execute("SELECT * FROM Usuários WHERE email=?", (emailUp,))
        emailCheck = c.fetchone()
        
        if emailCheck is None:
            #Inserir dados na tabela:
            c.execute("INSERT INTO Usuários VALUES (:nome,:sobrenome,:email,:telefone,:senha)",
                    {
                        'nome': entryNome.get().strip(),
                        'sobrenome': entrySobrenome.get().strip(),
                        'email': entryEmail.get().strip(),
                        'telefone': entryTelefone.get().strip(),
                        'senha': entrySenha.get().strip()
                    })

            # Commit das mudanças:
            conexao.commit()

            # Fechar o banco de dados:
            conexao.close()
            
            # #Apaga os valores das caixas de entrada
            entryNome.delete(0,"end"),
            entrySobrenome.delete(0,"end"),
            entryEmail.delete(0,"end"),
            entryTelefone.delete(0,"end"),
            entrySenha.delete(0,"end")

            messagebox.showinfo(title='Autikids Cadastro', message=f'Usuário {nomeUp} cadastrado com sucesso!\nVolte para o menu e faça Login.')
            
        else:
            messagebox.showerror(title='Autikids Cadastro', message='Este Email já está cadastrado.')
            entryEmail.delete(0,"end") 

def logar():
    
    ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
    inputEmail = entryInputEmail.get().strip()
    inputSenha = entryInputSenha.get().strip()
    
    if not inputEmail or not inputSenha:
        
        messagebox.showerror(title='Autikids Login', message='Preencha os campos.')
    
    else:
        
        conexao = sqlite3.connect('funcionários.db')
        c = conexao.cursor()
        
        c.execute("SELECT * FROM Usuários WHERE email=? AND senha=?", (inputEmail, inputSenha))
        res = c.fetchone()
        
        if res is None:
            messagebox.showerror(title='Autikids Login', message=f'Email ou senha incorreto(s). Tente novamente.')
            entryInputEmail.delete(0,"end"),
            entryInputSenha.delete(0,"end")
        
        else:
            messagebox.showinfo(title='Autikids Login', message=f'Login feito com sucesso. Bem vindo(a), {res[0]}.')
            logado()
            
def j1_to_j0(): 
    
    global canvasHud
    global l_logo
    global botãoLogin
    global botãoCadastro
        
    labelLogTitle.destroy()
    labelInputLogin.destroy()
    labelInputSenha.destroy()
    
    entryInputEmail.destroy()
    entryInputSenha.destroy()
    
    botãoVoltarMenu.destroy()
    botãoConfirmarLog.destroy()

    ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
    
    imgCanvas = PhotoImage(file='img_frame1.png')
    canvasHud = Canvas(janela, width=465, height=291, bg='orange', highlightthickness=0)
    canvasHud.create_image(0, 0, image=imgCanvas, anchor='nw')
    canvasHud.grid(columnspan=1, rowspan=3)
    
    imgLogo = PhotoImage(file='logo.png')
    l_logo = Label(janela, image=imgLogo, bg = 'white')
    l_logo.grid(padx = 21, row=0, sticky='wes',  column = 0, columnspan = 1)

    imgLogin = PhotoImage(file='login_botão.png')
    botãoLogin = Button(janela, image=imgLogin, command = j1,bg = 'white', border=0, activebackground='white', cursor='hand2')
    botãoLogin.grid(padx = 21, row=1, sticky='wes', column = 0, columnspan = 2)

    imgCadastro = PhotoImage(file='criar_botão.png')
    botãoCadastro = Button(janela, image=imgCadastro, command = j2, bg = 'white', border=0, activebackground='white', cursor='hand2')
    botãoCadastro.grid(padx = 21, pady = 3, row=2, sticky='wen', column = 0, columnspan = 2)

    janela.config(bd=230)
    janela.mainloop()

def j2_to_j0():
    
    global canvasHud
    global l_logo
    global botãoLogin
    global botãoCadastro
    
    ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
    
    labelCadastro.destroy()
    labelNome.destroy()
    labelSobrenome.destroy()
    labelEmail.destroy()
    labelTelefone.destroy()
    labelSenha.destroy()
    
    entryNome.destroy()
    entrySobrenome.destroy()
    entryEmail.destroy()
    entryTelefone.destroy()
    entrySenha.destroy()
    
    botãoVoltarMenu.destroy()
    botãoConfirmarCad.destroy()

    imgCanvas = PhotoImage(file='img_frame1.png')
    canvasHud = Canvas(janela, width=465, height=291, bg='orange', highlightthickness=0)
    canvasHud.create_image(0, 0, image=imgCanvas, anchor='nw')
    canvasHud.grid(columnspan=1, rowspan=3)

    imgLogo = PhotoImage(file='logo.png')
    l_logo = Label(janela, image=imgLogo, bg = 'white')
    l_logo.grid(padx = 21, row=0, sticky='wes',  column = 0, columnspan = 1)

    imgLogin = PhotoImage(file='login_botão.png')
    botãoLogin = Button(janela, image=imgLogin, command = j1,bg = 'white', border=0, activebackground='white', cursor='hand2')
    botãoLogin.grid(padx = 21, row=1, sticky='wes', column = 0, columnspan = 2)

    imgCadastro = PhotoImage(file='criar_botão.png')
    botãoCadastro = Button(janela, image=imgCadastro, command = j2, bg = 'white', border=0, activebackground='white', cursor='hand2')
    botãoCadastro.grid(padx = 21, pady = 3, row=2, sticky='wen', column = 0, columnspan = 2)

    janela.config(bd=230)
    janela.mainloop()

def j1():

    canvasHud.destroy()
    l_logo.destroy()
    botãoLogin.destroy()
    botãoCadastro.destroy()
    
    global labelLogTitle
    global labelInputLogin
    global labelInputSenha
    
    global entryInputEmail
    global entryInputSenha
    
    global botãoVoltarMenu
    global botãoConfirmarLog
    
    ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
    
    labelLogTitle = Label(janela, text='Login de Funcionário')
    labelLogTitle.configure(font=('Poppins', 25, 'bold'), bg='orange', fg='white')
    labelLogTitle.grid(padx = 5, row = 0, column=1, sticky='nswe')
    
    #LABELS
    
    labelInputLogin = Label(janela, text='Email:', background='orange', font=('Poppins 12 bold'))
    labelInputLogin.grid(padx = 5, row = 1, column=0, sticky='we')
    
    labelInputSenha = Label(janela, text='Senha:', background='orange', font=('Poppins 12 bold'))
    labelInputSenha.grid(padx = 5, row = 2, column=0, sticky='we')
    
    ##ENTRYS
    
    entryInputEmail = Entry(janela, border=2, font=('Poppins 12'))
    entryInputEmail.grid(row = 1, column=1, sticky='we', pady=15)
    
    entryInputSenha = Entry(janela, show='*', border=2, font=('Poppins 12'))
    entryInputSenha.grid(row = 2, column=1, sticky='we')
    
    ##BOTÃO
    
    botãoVoltarMenu = Button(janela, text='Voltar', activebackground='#fdd42a', font=('Poppins 12 bold'), command=j1_to_j0, cursor='hand2')
    botãoVoltarMenu.grid(pady = 15, row = 5, column=0, sticky='we')
    
    botãoConfirmarLog = Button(janela, text='Fazer login', activebackground='#fdd42a', font=('Poppins 12 bold'), command=logar, cursor='hand2')
    botãoConfirmarLog.grid(pady = 15, row = 5, column=1, sticky='we')
    
    janela.config(bd=230)
    janela.mainloop()
    
def j2():
    
    canvasHud.destroy()
    l_logo.destroy()
    botãoLogin.destroy()
    botãoCadastro.destroy()
    
    global labelCadastro
    global labelNome
    global labelSobrenome
    global labelEmail
    global labelTelefone
    global labelSenha
    
    global entryNome
    global entrySobrenome
    global entryEmail
    global entryTelefone
    global entrySenha
    
    global botãoVoltarMenu
    global botãoConfirmarCad
    
    ps.playsound('C:/Users/samub/OneDrive/Área de Trabalho/fac/Autikids/menuclick.wav')
    
    labelCadastro = Label(janela, text='Cadastro de Funcionário')
    labelCadastro.configure(font=('Poppins', 20, 'bold'), bg='orange', fg='white')
    labelCadastro.grid(padx = 5, row = 0, column=1)
    
    labelNome = Label(janela, text='Nome:', background='orange', font=('Poppins 12 bold'))
    labelNome.grid(padx = 5, row = 1, column = 0, sticky=E)
    
    labelSobrenome = Label(janela, text='Sobrenome:', background='orange', font=('Poppins 12 bold'))
    labelSobrenome.grid(padx = 5, row = 2, column = 0, sticky=E)
    
    labelEmail = Label(janela, text='Email:', background='orange', font=('Poppins 12 bold'))
    labelEmail.grid(padx = 5, row = 3, column = 0, sticky=E)
    
    labelTelefone = Label(janela, text='Telefone:', background='orange', font=('Poppins 12 bold'))
    labelTelefone.grid(padx = 5, row = 4, column = 0, sticky=E)
    
    labelSenha = Label(janela, text='Senha:', background='orange', font=('Poppins 12 bold'))
    labelSenha.grid(padx = 5, row = 5, column = 0, sticky=E)
    
    ##ENTRYS
    
    entryNome = Entry(janela, text='Nome:', border=2, font=('Poppins 12'))
    entryNome.grid(pady = 6, row = 1, column = 1, sticky='nswe')
    
    entrySobrenome = Entry(janela, text='Sobrenome:', border=2, font=('Poppins 12'))
    entrySobrenome.grid(pady = 6, row = 2, column = 1, sticky='nswe')
    
    entryEmail = Entry(janela, text='Email:', border=2, font=('Poppins 12'), width=30)
    entryEmail.grid(pady = 6, row = 3, column = 1, sticky='nswe')
    
    entryTelefone = Entry(janela, text='Telefone:', border=2, font=('Poppins 12'))
    entryTelefone.grid(pady = 6, row = 4, column = 1, sticky='nswe')
    
    entrySenha = Entry(janela, text='Senha:', show='*', border=2, font=('Poppins 12'))
    entrySenha.grid(pady = 6, row = 5, column = 1, sticky='nswe')
    
    ##BOTÕES
    
    botãoVoltarMenu = Button(janela, text='Voltar', width = 10, activebackground='#fdd42a', font=('Poppins 12 bold'), command=j2_to_j0, cursor='hand2')
    botãoVoltarMenu.grid(pady = 5, row = 6, sticky=E)
    
    botãoConfirmarCad = Button(janela, text='Criar conta', width = 15, activebackground='#fdd42a', command=cadastrar_cliente, font=('Poppins 12 bold'), cursor='hand2')
    botãoConfirmarCad.grid(pady = 5, row = 6, column = 1, sticky='nswe')
    
    janela.config(bd=220)
    janela.mainloop()

janela = Tk()
janela.title('Autikids')
janela.iconbitmap('icon.ico')

# janela.wm_minsize(width=920, height=800)
# janela.wm_maxsize(width=920, height=800)
janela.config(bg='orange')

imgCanvas = PhotoImage(file='img_frame1.png')
canvasHud = Canvas(janela, width=465, height=291, bg='orange', highlightthickness=0)
canvasHud.create_image(0, 0, image=imgCanvas, anchor='nw')
canvasHud.grid(columnspan=1, rowspan=3)

imgLogo = PhotoImage(file='logo.png')
l_logo = Label(janela, image=imgLogo, bg = 'white')
l_logo.grid(padx = 21, row=0, sticky='wes',  column = 0, columnspan = 1)

imgLogin = PhotoImage(file='login_botão.png')
botãoLogin = Button(janela, image=imgLogin, command = j1,bg = 'white', border=0, activebackground='white', cursor='hand2')
botãoLogin.grid(padx = 21, row=1, sticky='wes', column = 0, columnspan = 2)

imgCadastro = PhotoImage(file='criar_botão.png')
botãoCadastro = Button(janela, image=imgCadastro, command = j2, bg = 'white', border=0, activebackground='white', cursor='hand2')
botãoCadastro.grid(padx = 21, pady = 3, row=2, sticky='wen', column = 0, columnspan = 2)

janela.config(bd=230)
janela.mainloop()
