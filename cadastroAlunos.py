import sqlite3
import tkinter
import os

pastaApp=os.path.dirname(__file__)


def cadastrar_aluno():
    conexao = sqlite3.connect('banco_alunos2.db')
    cursor=conexao.cursor()
    cursor.execute("INSERT INTO alunos VALUES(:nome,:sobrenome,:telefone,:datadenascimento,:endereco,:cep,:bairro)",
                   {
                       'nome':entry_nome.get(),
                       'sobrenome':entry_sobrenome.get(),
                       'telefone':entry_telefone.get(),
                       'datadenascimento':entry_datadenascimento.get(),
                       'endereco':entry_endereco.get(),
                       'cep':entry_cep.get(),
                       'bairro':entry_bairro.get(),



                   }
                   )
    conexao.commit()
    conexao.close()
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_datadenascimento.delete(0,"end")
    entry_endereco.delete(0, "end")
    entry_cep.delete(0,"end")
    entry_bairro.delete(0,"end")


def exporta_alunos():
    conexao = sqlite3.connect('banco_alunos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT *, oid FROM alunos")
    alunos_cadastrados=cursor.fetchall()
    alunos_cadastrados=pd.DataFrame(alunos_cadastrados, columns=['nome','sobrenome','telefone','data de nascimento','endereco','cep','bairro','id_banco'])
    conexao.commit()
    conexao.close()

janela = tkinter.Tk()
janela.title('Autikids')
janela.iconbitmap('icon.ico')
janela.config(bg='orange', bd=150)

# labels:

label_titulo = tkinter.Label(janela, text='Cadastro de aluno')
label_titulo.configure(font=('Poppins', 20, 'bold'), bg='orange', fg='white')
label_titulo.grid(row=0, column=1, columnspan=1)

label_nome= tkinter.Label(janela, text='Nome: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='e')

label_sobrenome= tkinter.Label(janela, text='Sobrenome: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
label_sobrenome.grid(row=2, column=0, padx=10, pady=10, sticky='e')

label_telefone= tkinter.Label(janela, text='Telefone: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
label_telefone.grid(row=3, column=0, padx=10, pady=10, sticky='e')

label_datadenascimento=tkinter.Label(janela,text='Data de Nascimento: ',bg='orange',fg='black',border=2, font=('Poppins 12 bold'))
label_datadenascimento.grid(row=4,column=0,padx=10,pady=10, sticky='e')

label_endereco= tkinter.Label(janela, text='Endereço: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
label_endereco.grid(row=5, column=0, padx=10, pady=10, sticky='e')

label_cep= tkinter.Label(janela, text='CEP: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
label_cep.grid(row=6, column=0, padx=10, pady=10, sticky='e')

label_bairro= tkinter.Label(janela, text='Bairro: ',bg='orange',fg="black",border=2, font=('Poppins 12 bold'))
label_bairro.grid(row=7, column=0, padx=10, pady=10, sticky='e')


# Entrys:

entry_nome= tkinter.Entry(janela, width=30, border=2, font=('Poppins 12'))
entry_nome.grid(row=1, column=1, pady=10)

entry_sobrenome= tkinter.Entry(janela,width=30, border=2, font=('Poppins 12'))
entry_sobrenome.grid(row=2, column=1, pady=10)

entry_telefone= tkinter.Entry(janela,width=30, border=2, font=('Poppins 12'))
entry_telefone.grid(row=3, column=1, pady=10)

entry_datadenascimento=tkinter.Entry(janela,width=30, border=2, font=('Poppins 12'))
entry_datadenascimento.grid(row=4,column=1,pady=10)

entry_endereco= tkinter.Entry(janela,width=30, border=2, font=('Poppins 12'))
entry_endereco.grid(row=5, column=1, pady=10)

entry_cep= tkinter.Entry(janela,width=30, border=2, font=('Poppins 12'))
entry_cep.grid(row=6, column=1, pady=10)

entry_bairro= tkinter.Entry(janela,width=30, border=2, font=('Poppins 12'))
entry_bairro.grid(row=7, column=1, pady=10)

# Botoes:
botao_cadastar= tkinter.Button(janela,text="Cadastrar Aluno", command= cadastrar_aluno, border=2, font=('Poppins 12 bold'), activebackground='yellow')
botao_cadastar.grid(row=8,column=1,pady=10, sticky='nswe')

janela.mainloop()