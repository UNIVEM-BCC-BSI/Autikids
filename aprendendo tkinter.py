from tkinter import *
import sqlite3

# #criar banco de dados
# conexão = sqlite3.connect('usuários_e_senhas.db')
# cursor = conexão.cursor()
# cursor.execute(''' CREATE TABLE Usuários (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text,
#     senha text
#     )
# ''')
# conexão.commit()
# conexão.close()

#enviar formulário do usuário para o banco de dados ou não
def Enviar_dados():
    nome = entryNome.get()
    sobrenome = entrySobrenome.get()
    email = entryEmail.get()
    telefone = entryTelefone.get()
    senha = entrySenha.get()
    print(nome, sobrenome, email, telefone, senha)

#cadastrar novo usuário
def criar_conta():
    
    headline.destroy()
    botãoLogin.destroy()
    botãoCadastro.destroy()

    #LABELS
    
    labelCadastro = Label(janela1, text='Cadastro de Usuário')
    labelCadastro.configure(font=('Poppins', 45, 'bold'))
    labelCadastro.grid(padx = 5, row = 0, columnspan = 2, sticky='nswe')
    
    labelNome = Label(janela1, text='Nome:')
    labelNome.grid(padx = 5, row = 1, column = 0, sticky='nswe' )
    
    labelSobrenome = Label(janela1, text='Sobrenome:')
    labelSobrenome.grid(padx = 5, row = 2, column = 0, sticky='nswe')
    
    labelEmail = Label(janela1, text='Email:')
    labelEmail.grid(padx = 5, row = 3, column = 0, sticky='nswe')
    
    labelTelefone = Label(janela1, text='Telefone:')
    labelTelefone.grid(padx = 5, row = 4, column = 0, sticky='nswe')
    
    labelSenha = Label(janela1, text='Senha:')
    labelSenha.grid(padx = 5, row = 5, column = 0, sticky='nswe')
    
    ##ENTRYS
    
    entryNome = Entry(janela1, text='Nome:', border=2)
    entryNome.grid(pady = 6, row = 1, column = 1, sticky='nswe')
    
    entrySobrenome = Entry(janela1, text='Sobrenome:', border=2)
    entrySobrenome.grid(pady = 6, row = 2, column = 1, sticky='nswe')
    
    entryEmail = Entry(janela1, text='Email:', border=2)
    entryEmail.grid(pady = 6, row = 3, column = 1, sticky='nswe')
    
    entryTelefone = Entry(janela1, text='Telefone:', border=2)
    entryTelefone.grid(pady = 6, row = 4, column = 1, sticky='nswe')
    
    entrySenha = Entry(janela1, text='Senha:', show='*', border=2)
    entrySenha.grid(pady = 6, row = 5, column = 1, sticky='nswe')
    
    ##BOTÕES
    
    botãoVoltarMenu = Button(janela1, text='Voltar', width = 30, border = 3, activebackground='SteelBlue1')
    botãoVoltarMenu.grid(pady = 5, row = 6, column = 0, sticky='nswe')
    
    botãoConfirmarCad = Button(janela1, text='Criar conta', width = 30, border = 3, activebackground='SteelBlue1', command = Enviar_dados)
    botãoConfirmarCad.grid(pady = 5, row = 6, column = 1, sticky='nswe')
    
    janela1.config(bd=150)
    
# interface principal

janela1 = Tk()
janela1.title('Autikids')
janela1.iconbitmap('icon.ico')

headline = Label(janela1, text='Autikids')
headline.configure(font=('Poppins', 64, 'bold'))
headline.grid(padx = 25, row=0, sticky='nswe',  column = 0, columnspan = 1)

botãoLogin = Button(janela1, text='Fazer login', highlightthickness='5', activebackground='SteelBlue1')
botãoLogin.grid(padx = 25, row=1, sticky='nswe', column = 0, columnspan = 2)

botãoCadastro = Button(janela1, text='Cadastrar usuário', highlightthickness='5', command=criar_conta, activebackground='SteelBlue1')
botãoCadastro.grid(padx = 25, row=2, sticky='nswe', column = 0, columnspan = 2)
janela1.config(bd=250)

janela1.mainloop()