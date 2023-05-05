from tkinter import *
import pyttsx3

#defs botões

def b1():
    s = pyttsx3.init()
    data = f"Olá! Meu nome é Exemplo. Qual seu nome?"
    s.say(data)
    s.runAndWait()

def b2():
    s = pyttsx3.init()
    data = f"Estou com fome."
    s.say(data)
    s.runAndWait()

def b3():
    s = pyttsx3.init()
    data = f"Estou com sede."
    s.say(data)
    s.runAndWait()
    
def b4():
    s = pyttsx3.init()
    data = f"Onde fica o banheiro?"
    s.say(data)
    s.runAndWait()
    
def b5():
    s = pyttsx3.init()
    data = f"Preciso de ajuda!"
    s.say(data)
    s.runAndWait()
    
def b6():
    s = pyttsx3.init()
    data = f"Quero isso."
    s.say(data)
    s.runAndWait()
    
def b7():
    s = pyttsx3.init()
    data = f"Quero aquilo."
    s.say(data)
    s.runAndWait()
    
def b8():
    s = pyttsx3.init()
    data = f"Obrigado."
    s.say(data)
    s.runAndWait()

janela = Tk()
janela.title('Autikids')
janela.iconbitmap('icon.ico')
janela.wm_minsize(width=1450, height=800)
janela.wm_maxsize(width=1450, height=800)
janela.config(bg='orange')

imgLogo = PhotoImage(file='logo_teladeinterações.gif')
l_logo = Label(janela, image=imgLogo, bg = 'orange').grid(pady=20, row=0, sticky='wens', columnspan=4)

imgApresentações = PhotoImage(file='botão_apresentações.gif')
b_Apresentações = Button(janela, image=imgApresentações, bg = 'orange', border=0, activebackground='orange', command=b1)
b_Apresentações.grid(column = 0, row=1, sticky='we', padx=35)

imgFome = PhotoImage(file='botão_fome.gif')
b_Fome = Button(janela, image=imgFome, bg = 'orange', border=0, activebackground='orange', command=b2)
b_Fome.grid(column = 1, row=1, sticky='we', padx=35)

imgSede = PhotoImage(file='botão_sede.gif')
b_Sede = Button(janela, image=imgSede, bg = 'orange', border=0, activebackground='orange', command=b3)
b_Sede.grid(column = 2, row=1, sticky='we', padx=35)

imgBanheiro = PhotoImage(file='botão_banheiro.gif')
b_Banheiro = Button(janela, image=imgBanheiro, bg = 'orange', border=0, activebackground='orange', command=b4)
b_Banheiro.grid(column = 3, row=1, sticky='we', padx=35)

imgAjuda = PhotoImage(file='botão_ajuda.gif')
b_Ajuda = Button(janela, image=imgAjuda, bg = 'orange', border=0, activebackground='orange', command=b5)
b_Ajuda.grid(column = 0, row=2, sticky='we', padx=35, pady=20)

imgIsso = PhotoImage(file='botão_isso.gif')
b_Isso = Button(janela, image=imgIsso, bg = 'orange', border=0, activebackground='orange', command=b6)
b_Isso.grid(column = 1, row=2, sticky='we', padx=35, pady=20)

imgAquilo = PhotoImage(file='botão_aquilo.gif')
b_Aquilo = Button(janela, image=imgAquilo, bg = 'orange', border=0, activebackground='orange', command=b7)
b_Aquilo.grid(column = 2, row=2, sticky='we', padx=35, pady=20)

imgObrigado = PhotoImage(file='botão_obrigado.gif')
b_Obrigado = Button(janela, image=imgObrigado, bg = 'orange', border=0, activebackground='orange', command=b8)
b_Obrigado.grid(column = 3, row=2, sticky='we', padx=35, pady=20)

janela.config(bd=10)
janela.mainloop()