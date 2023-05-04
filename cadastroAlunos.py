import sqlite3
import tkinter
import os


pastaApp=os.path.dirname(__file__)

# conexao = sqlite3.connect('banco_alunos.db')
#
# cursor=conexao.cursor()
# cursor.execute(''' CREATE TABLE Alunos (
#          Nome text,
#          Sobrenome text,
#          Telefone text,
#          Endereço text,
#          Observação text
#          )
# ''')
# conexao.commit()
# conexao.close()

def cadastrar_aluno():
    conexao = sqlite3.connect('banco_alunos.db')
    cursor=conexao.cursor()
    cursor.execute("INSERT INTO alunos VALUES(:nome,:sobrenome,:telefone,:endereco,:observacao)",
                   {
                       'nome':entry_nome.get(),
                       'sobrenome':entry_sobrenome.get(),
                       'telefone':entry_telefone.get(),
                       'endereco':entry_telefone.get(),
                       'observacao':entry_observacao.get()

                   }
                   )
    conexao.commit()
    conexao.close()
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_endereco.delete(0, "end")
    entry_observacao.delete(0, "end")

def exporta_alunos():
    conexao = sqlite3.connect('banco_alunos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT *, oid FROM alunos")
    alunos_cadastrados=cursor.fetchall()
    alunos_cadastrados=pd.DataFrame(alunos_cadastrados, columns=['nome','sobrenome','telefone','endereco','observacao','id_banco'])
    alunos_cadastrados.to_excel('banco_alunos.xlsx')
    conexao.commit()
    conexao.close()


janela = tkinter.Tk()
janela.title('Autikids')
janela.iconbitmap('icon.ico')
janela.geometry("700x400")
# labels:

label_nome= tkinter.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome= tkinter.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=20, pady=10)

label_telefone= tkinter.Label(janela, text='Telefone')
label_telefone.grid(row=2, column=0, padx=10, pady=10)

label_endereco= tkinter.Label(janela, text='Endereço')
label_endereco.grid(row=3, column=0, padx=10, pady=10)

label_observacao= tkinter.Label(janela, text='Observação')
label_observacao.grid(row=4, column=0, padx=10, pady=10)

# Entrys:

entry_nome= tkinter.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome= tkinter.Entry(janela,width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_telefone= tkinter.Entry(janela,width=30)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)

entry_endereco= tkinter.Entry(janela,width=30)
entry_endereco.grid(row=3, column=1, padx=10, pady=10)

entry_observacao= tkinter.Entry(janela,width=30)
entry_observacao.grid(row=4, column=1, padx=10, pady=10)

# Botoes:
botao_cadastar= tkinter.Button(janela,text="Cadastrar Aluno", command= cadastrar_aluno)
botao_cadastar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)







janela.mainloop()

