from tkinter import *
import sqlite3

#banco de dados

def cadastrar_cliente():
    conexao = sqlite3.connect('usuários_e_senhas')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO Usuários VALUES (:nome,:sobrenome,:email,:telefone,:senha)",
              {
                  'nome': entryNome.get(),
                  'sobrenome': entrySobrenome.get(),
                  'email': entryEmail.get(),
                  'telefone': entryTelefone.get(),
                  'senha': entrySenha.get()
              })

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entryNome.delete(0,"end"),
    entrySobrenome.delete(0,"end"),
    entryEmail.delete(0,"end"),
    entryTelefone.delete(0,"end"),
    entrySenha.delete(0,"end")

def j1():

    l_logo.destroy()
    botãoLogin.destroy()
    botãoCadastro.destroy()
    
    labelLogTitle = Label(janela, text='Login de Usuário')
    labelLogTitle.configure(font=('Poppins', 25, 'bold'), bg='orange', fg='white')
    labelLogTitle.grid(padx = 5, row = 0, columnspan=2, sticky=E)
    
    #LABELS
    
    labelInputLogin = Label(janela, text='Email:', background='orange', font=('Poppins 12 bold'))
    labelInputLogin.grid(padx = 5, row = 1, column = 0, sticky=E)
    
    labelInputSenha = Label(janela, text='Senha:', background='orange', font=('Poppins 12 bold'))
    labelInputSenha.grid(padx = 5, row = 2, column = 0, sticky=E)
    
    ##ENTRYS
    
    entryInputLogin = Entry(janela, border=2, font=('Poppins 12'))
    entryInputLogin.grid(pady = 6, row = 1, column = 1, sticky=W)
    
    entrySenha = Entry(janela, text='Senha:', show='*', border=2, font=('Poppins 12'))
    entrySenha.grid(pady = 6, row = 2, column = 1, sticky=W)
    
    ##BOTÃO
    
    botãoConfirmarLog = Button(janela, text='Fazer login', activebackground='yellow', font=('Poppins 12 bold'))
    botãoConfirmarLog.grid(pady = 5, row = 3, columnspan = 2, sticky='we')
    
    janela.config(bd=310)
    janela.mainloop()
    
def j2():
    
    l_logo.destroy()
    botãoLogin.destroy()
    botãoCadastro.destroy()
    
    labelCadastro = Label(janela, text='Cadastro de Usuário')
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
    
    botãoVoltarMenu = Button(janela, text='Voltar', width = 10, activebackground='yellow', font=('Poppins 12 bold'))
    botãoVoltarMenu.grid(pady = 5, row = 6, sticky=E)
    
    botãoConfirmarCad = Button(janela, text='Criar conta', width = 15, activebackground='yellow', command=cadastrar_cliente, font=('Poppins 12 bold'))
    botãoConfirmarCad.grid(pady = 5, row = 6, column = 1, sticky='nswe')
    
    janela.config(bd=220)
    janela.mainloop()

janela = Tk()
janela.title('Autikids')
janela.iconbitmap('icon.ico')
janela.wm_minsize(width=920, height=800)
janela.wm_maxsize(width=920, height=800)
janela.config(bg='orange')

imgLogo = PhotoImage(file='logo_gif.gif')
l_logo = Label(janela, image=imgLogo, bg = 'orange')
l_logo.grid(padx = 25, pady = 15, row=0,sticky='we',  column = 0, columnspan = 1)

imgLogin = PhotoImage(file='login_botão.png')
botãoLogin = Button(janela, image=imgLogin, command = j1,bg = 'orange', border=0, activebackground='orange')
botãoLogin.grid(padx = 25, row=1, sticky='we', column = 0, columnspan = 2)

imgCadastro = PhotoImage(file='criar_botão.png')
botãoCadastro = Button(janela, image=imgCadastro, command = j2, bg = 'orange', border=0, activebackground='orange')
botãoCadastro.grid(padx = 25, pady = 3, row=2, sticky='we', column = 0, columnspan = 2)

janela.config(bd=250)
janela.mainloop()
