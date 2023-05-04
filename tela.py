import tkinter
from tkinter import*
import sqlite3
import os



def semcomando():
    print("")

def cadastrarAlunos():
    exec(open("cadastroAlunos.py").read())


app=Tk()
app.title("Autikids")
app.geometry('500x300')
app.configure(background="#dde")

barrademenus=Menu(app)
menuAlunos=Menu(barrademenus,tearoff=0)
menuAlunos.add_command(label="Novo Cadastro",command=cadastrarAlunos)
menuAlunos.add_command(label="Pesquisar",command=semcomando)
menuAlunos.add_separator()
menuAlunos.add_command(label="Fechar",command=app.quit)
barrademenus.add_cascade(label="Alunos",menu=menuAlunos)

menuInteracoes=Menu(barrademenus,tearoff=0)
menuInteracoes.add_command(label="Alimentação",command=semcomando)
barrademenus.add_cascade(label='Interaçoes',menu=menuInteracoes)


app.config(menu=barrademenus)

app.mainloop()