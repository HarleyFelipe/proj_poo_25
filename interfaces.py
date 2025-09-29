import tkinter as tk
from tkinter import messagebox as mb
from modelos import *

def inicio():
    inicioFr.tkraise()

def cadArma():
     print("fa")

def cadPersonagem():
     print("da")

def pgArma():
     armaFr.tkraise()

def pgClasse():
     classeFr.tkraise()

def pgPersonagem():
     personagemFr.tkraise()

janela = tk.Tk()
janela.title("Elementaria")
janela.geometry("500x500")

ft1 = ("Times New Roman", 18, "bold")
ft2 = ("Times New Roman", 15, "bold")
ft3 = ("Times New Roman", 12)

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

menuB = tk.Menu(janela)
inicioMn = tk.Menu(menuB, tearoff=False)
inicioMn.add_command(label="Início", command=inicio)
inicioMn.add_command(label="Sair", command=janela.quit)
menuB.add_cascade(label="Início", menu=inicioMn)

inicioFr = tk.Frame(janela)

inicioFr.grid_columnconfigure(0, weight=1) 
inicioFr.grid_columnconfigure(1, weight=0) 
inicioFr.grid_columnconfigure(2, weight=1) 
inicioFr.grid_rowconfigure(1, weight=0)    
inicioFr.grid_rowconfigure(2, weight=0)    
inicioFr.grid_rowconfigure(3, weight=1)    

l_titulo = tk.Label(inicioFr, text="Elementaria", font=("Cooper Black", 18, "bold"), justify="center")
l_titulo.grid(padx=5, pady=7, column=1, row=1)

l_txt = tk.Label(inicioFr, text="Vamos criar seu personagem!!", font=("Arial", 12))
l_txt.grid(padx=5, pady=7, column=1, row=2)

fichaMn = tk.Menu(menuB, tearoff=False)
menuB.add_cascade(label="Ficha", menu=fichaMn)

fichaMn.add_command(label="Arma", command=pgArma)
armaFr = tk.Frame(janela)
armaFr.grid_columnconfigure(0, weight=1) 
armaFr.grid_columnconfigure(1, weight=0) 
armaFr.grid_columnconfigure(2, weight=1) 
armaFr.grid_rowconfigure(3, weight=0)   
armaFr.grid_rowconfigure(1, weight=0)    
armaFr.grid_rowconfigure(2, weight=0)    

l_titulo = tk.Label(armaFr, text="Cadastrar Arma", font=ft1, justify="center")
l_titulo.grid(padx=5, pady=7, column=0, row=0, columnspan=3)
l_nome = tk.Label(armaFr, text="Nome", font=ft2)
l_nome.grid(padx=5, pady=5, column=0, row=1)
e_nome = tk.Entry(armaFr, font=ft3)
e_nome.grid(padx=5, pady=5, column=1, row=1) 
l_nivel = tk.Label(armaFr, text="Nível", font=ft2)
l_nivel.grid(padx=5, pady=5, column=0, row=2)
e_nivel = tk.Entry(armaFr, font=ft3)
e_nivel.grid(padx=5, pady=5, column=1, row=2)
l_alcance = tk.Label(armaFr, text="Alcance", font=ft2)
l_alcance.grid(padx=5, pady=5, column=0, row=3)
e_alcance = tk.Entry(armaFr, font=ft3)
e_alcance.grid(padx=5, pady=5, column=1, row=3)

#l_desc = tk.Label(armaFr, text="Descrição", font=ft2, justify="center")
#l_desc.grid(padx=5, pady=5, column=0, row=2)
#e_desc = tk.Text(armaFr, font=ft3, width=3, height=5)
#e_desc.grid(padx=5, pady=5, column=1, row=2, sticky="nesw")

fichaMn.add_command(label="Classe", command=pgClasse)
classeFr = tk.Frame(janela)
l_titulo = tk.Label(classeFr, text="Cadastrar Classe", font=ft1, justify="center")
l_titulo.grid(padx=5, pady=7, column=0, row=0, columnspan=3)
classeFr.grid_columnconfigure(0, weight=1) 
classeFr.grid_columnconfigure(1, weight=0) 
classeFr.grid_columnconfigure(2, weight=1) 
classeFr.grid_rowconfigure(3, weight=1)   
classeFr.grid_rowconfigure(1, weight=0)    
classeFr.grid_rowconfigure(2, weight=0)    

fichaMn.add_command(label="Personagem", command=pgPersonagem)
personagemFr = tk.Frame(janela)
l_titulo = tk.Label(personagemFr, text="Cadastrar Personagem", font=ft1, justify="center")
l_titulo.grid(padx=5, pady=7, column=0, row=0, columnspan=3)
personagemFr.grid_columnconfigure(0, weight=1) 
personagemFr.grid_columnconfigure(1, weight=0) 
personagemFr.grid_columnconfigure(2, weight=1) 
personagemFr.grid_rowconfigure(3, weight=1)   
personagemFr.grid_rowconfigure(1, weight=0)    
personagemFr.grid_rowconfigure(2, weight=0)    

inicioFr.grid(row=0, column=0, sticky="nesw")
armaFr.grid(row=0, column=0, sticky="nesw")
classeFr.grid(row=0, column=0, sticky="nesw")
personagemFr.grid(row=0, column=0, sticky="nesw")

inicioFr.tkraise()

janela.config(menu=menuB)
janela.mainloop()