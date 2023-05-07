import tkinter
from tkinter import*
import sqlite3
import os
from subprocess import run
Autikids=os.path.dirname(__file__)



def semcomando():
    print("")

def cadastrarAluno():
    run("c:\Autikids\cadastroAlunos.exe")

def interacao():
    exec(open("Autikids Tela de Interações..py").read())






app=Tk()
app.title("Autikids")
app.geometry('1920x1080')
app.configure(background="#dde")
app.iconbitmap('icon.ico')
imgLogo=PhotoImage(file=Autikids+"\\logo_autikids.png")
logo=Label(app,image=imgLogo,bg='orange')
logo.place(x=500,y=90)
app.config(bg='orange')

barrademenus=Menu(app)
menuAlunos=Menu(barrademenus,tearoff=0)
menuAlunos.add_command(label="Novo Cadastro",command=cadastrarAluno)
menuAlunos.add_command(label="Pesquisar",command=semcomando)
menuAlunos.add_separator()
menuAlunos.add_command(label="Fechar",command=app.quit)
barrademenus.add_cascade(label="Alunos",menu=menuAlunos)

menuconfiguracao=Menu(barrademenus,tearoff=0)
menuconfiguracao.add_command(label="Login",command=semcomando)
menuconfiguracao.add_command(label="Ajustes",command=semcomando)
barrademenus.add_cascade(label='Configurações',menu=menuconfiguracao)

app.config(menu=barrademenus)

imgAlimentacao = PhotoImage(file='botão_alimentação.gif')
b_Alimentacao = Button(app, image=imgAlimentacao, bg='orange', border=0, activebackground='orange', command=semcomando)
b_Alimentacao.place(x=800,y=400)

imgInteracao = PhotoImage(file='botão_interações.gif')
b_Interacao = Button(app, image=imgInteracao, bg='orange', border=0, activebackground='orange', command=interacao)
b_Interacao.place(x=300,y=400)

app.config(menu=barrademenus)


app.mainloop()