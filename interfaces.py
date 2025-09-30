import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
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

def pgRelatorio():
     relatorioFr.tkraise()

def limpar(pg):
    for campo in pg.winfo_children():
        if isinstance(campo, tk.Entry):
            campo.delete(0, tk.END)
        elif isinstance(campo, tk.Text):
            campo.delete("1.0", tk.END)
        elif isinstance(campo, ttk.Combobox):
            campo.set("")

def salvar(pg): 
     if pg == armaFr:
          nomeA = e_nomeA.get()
          nivelA = int(e_nivelA.get())
          alcanceA = e_alcanceA.get()
          municaoA = e_municaoA.get()
          descricaoA =  t_descA.get("1.0",  "end-1c")

          armaC = Arma.create(nome=nomeA, nivel=nivelA, alcance=alcanceA, municao=municaoA, descricao=descricaoA)
          limpar(armaFr)

     elif pg == classeFr:
          nomeC = e_nomeC.get()
          bonusC = t_bonusC.get("1.0",  "end-1c")
          onusC = t_onusC.get("1.0",  "end-1c")
          descricaoC = t_descC.get("1.0",  "end-1c")

          classeC = Classe.create(nome=nomeC, bonus=bonusC, onus=onusC, descricao=descricaoC)
          limpar(classeFr)

     elif pg == personagemFr:
          nomeP = e_nomeP.get()
          descricaoP = t_descP.get("1.0", "end-1c")
          armaP = Arma.get(Arma.nome == c_armaP.get())
          classeP = Classe.get(Classe.nome == c_classeP.get())

          personagemC = Personagem.create(nome=nomeP, descricao=descricaoP, arma=armaP, classe=classeP)
          limpar(personagemFr)

def atualizarLB(listB):
     if listB == lb_armaR:
          lb_armaR.delete(0, tk.END)

          armaCad = Arma.select()

          for arma in armaCad:
               lb_armaR.insert(tk.END, f"--------------------------------------------------------------------------------------------------------------------")
               lb_armaR.insert(tk.END, f">Nome      :  {arma.nome}")
               lb_armaR.insert(tk.END, f">Nível        :  {arma.nivel}")
               lb_armaR.insert(tk.END, f">Alcance   :  {arma.alcance}")
               lb_armaR.insert(tk.END, f">Munição :  {arma.municao}")
               lb_armaR.insert(tk.END, f">Descrição:  {arma.descricao}")     

     elif listB == lb_classeR:
          lb_classeR.delete(0, tk.END)

          classeCad = Classe.select()

          for classe in classeCad:
               lb_classeR.insert(tk.END, f"--------------------------------------------------------------------------------------------------------------------")
               lb_classeR.insert(tk.END, f">Nome       :  {classe.nome}")
               lb_classeR.insert(tk.END, f">Bônus       :  {classe.bonus}")
               lb_classeR.insert(tk.END, f">Ônus        :  {classe.onus}")
               lb_classeR.insert(tk.END, f">Descrição:  {classe.descricao}")  

     elif listB == lb_persoR:
          lb_persoR.delete(0, tk.END)

          persoCad = Personagem.select()

          for perso in persoCad:
               lb_persoR.insert(tk.END, f"--------------------------------------------------------------------------------------------------------------------")
               lb_persoR.insert(tk.END, f">Nome      :  {perso.nome}")
               lb_persoR.insert(tk.END, f">Descrição:  {perso.descricao}")  
               lb_persoR.insert(tk.END, f">Arma       :  {perso.arma.nome}")
               lb_persoR.insert(tk.END, f">Classe      :  {perso.classe.nome}")
          
def excluir(listB):
     if listB == lb_armaR:

          slc = lb_armaR.curselection()[0]
          linha = lb_armaR.get(slc)

          nomeEx = linha.split(":")[1].strip()

          ex = Arma.get(Arma.nome == nomeEx)
          ex.delete_instance()

     elif listB == lb_classeR:

          slc = lb_classeR.curselection()[0]
          linha = lb_classeR.get(slc)

          nomeEx = linha.split(":")[1].strip()

          ex = Classe.get(Classe.nome == nomeEx)
          ex.delete_instance()

     elif listB == lb_persoR:

          slc = lb_persoR.curselection()[0]
          linha = lb_persoR.get(slc)

          nomeEx = linha.split(":")[1].strip()

          ex = Personagem.get(Personagem.nome == nomeEx)
          ex.delete_instance()

def editar2(pg):
     if pg == armaFr:
          edt.nome = e_nomeA.get()
          edt.nivel = int(e_nivelA.get())
          edt.alcance = e_alcanceA.get()
          edt.municao = e_municaoA.get()
          edt.descricao =  t_descA.get("1.0",  "end-1c")
          edt.save()

          limpar(armaFr)
          relatorioFr.tkraise()

     elif pg == classeFr:
          edt.nome = e_nomeC.get()
          edt.bonus = t_bonusC.get("1.0",  "end-1c")
          edt.onus = t_onusC.get("1.0",  "end-1c")
          edt.descricao = t_descC.get("1.0",  "end-1c")
          edt.save()

          limpar(classeFr)
          relatorioFr.tkraise()

     elif pg == personagemFr:
          edt.nome = e_nomeP.get()
          edt.descricao = t_descP.get("1.0", "end-1c")
          edt.arma = Arma.get(Arma.nome == c_armaP.get())
          edt.classe = Classe.get(Classe.nome == c_classeP.get())
          edt.save()

          limpar(personagemFr)
          relatorioFr.tkraise()

def editar(listB):
    global edt
    edt = None
    slc = listB.curselection()

    linha = listB.get(slc[0])  
    nome = linha.split(":")[1].strip()  

    if listB == lb_armaR:
        edt = Arma.get(Arma.nome == nome)
        e_nomeA.delete(0, tk.END)
        e_nomeA.insert(0, edt.nome)
        e_nivelA.delete(0, tk.END)
        e_nivelA.insert(0, edt.nivel)
        e_alcanceA.delete(0, tk.END)
        e_alcanceA.insert(0, edt.alcance)
        e_municaoA.delete(0, tk.END)
        e_municaoA.insert(0, edt.municao)
        t_descA.delete("1.0", tk.END)
        t_descA.insert("1.0", edt.descricao)
        pgArma()
        
        b_salvarA.config(text="Editar", command=lambda: (editar2(armaFr), atualizarLB(lb_armaR)))

    elif listB == lb_classeR:
        edt = Classe.get(Classe.nome == nome)
        e_nomeC.delete(0, tk.END)
        e_nomeC.insert(0, edt.nome)
        t_bonusC.delete("1.0", tk.END)
        t_bonusC.insert("1.0", edt.bonus)
        t_onusC.delete("1.0", tk.END)
        t_onusC.insert("1.0", edt.onus)
        t_descC.delete("1.0", tk.END)
        t_descC.insert("1.0", edt.descricao)
        pgClasse()

        b_salvarC.config(text="Editar", command=lambda: (editar2(classeFr), atualizarLB(lb_classeR)))

    elif listB == lb_persoR:
        edt = Personagem.get(Personagem.nome == nome)
        e_nomeP.delete(0, tk.END)
        e_nomeP.insert(0, edt.nome)
        t_descP.delete("1.0", tk.END)
        t_descP.insert("1.0", edt.descricao)
        c_armaP.set(edt.arma.nome)
        c_classeP.set(edt.classe.nome)
        pgPersonagem()

        b_salvarP.config(text="Editar", command=lambda: (editar2(personagemFr), atualizarLB(lb_persoR)))

janela = tk.Tk()
janela.title("Elementaria")
janela.geometry("600x600")

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

l_titulo = tk.Label(inicioFr, text="Elementária", font=("Cooper Black", 18, "bold"), justify="center")
l_titulo.grid(padx=5, pady=7, column=1, row=1)
l_txt = tk.Label(inicioFr, text="Vamos criar seu personagem!!", font=("Arial", 12))
l_txt.grid(padx=5, pady=7, column=1, row=2)

fichaMn = tk.Menu(menuB, tearoff=False)
menuB.add_cascade(label="Ficha", menu=fichaMn)

relatorioMn = tk.Menu(menuB, tearoff=False)
menuB.add_cascade(label="Relatório", menu=relatorioMn)

relatorioMn.add_command(label="Relatório", command=pgRelatorio)
relatorioFr = tk.Frame(janela)
relatorioFr.grid_columnconfigure(0, weight=1) 
relatorioFr.grid_columnconfigure(1, weight=0) 
relatorioFr.grid_columnconfigure(2, weight=1)  
relatorioFr.grid_rowconfigure(7, weight=1)

l_tituloR = tk.Label(relatorioFr, text="Relatórios", font=ft1, justify="center")
l_tituloR.grid(padx=5, pady=7, column=0, row=0, columnspan=3)
l_armaR = tk.Label(relatorioFr, text="Armas", font=ft2, justify="left")
l_armaR.grid(padx=5, pady=5, column=0, row=1)
lb_armaR = tk.Listbox(relatorioFr, width=30, height=7)
lb_armaR.grid(padx=5, pady=5, column=0, row=2, sticky="ew", columnspan=3)
atualizarLB(lb_armaR)

b_editarR = tk.Button(relatorioFr, text="Editar", font=ft2, command=lambda: editar(lb_armaR))
b_editarR.grid(padx=5, pady=5, column=1, row=1, sticky="ew")
b_excluirR = tk.Button(relatorioFr, text="Excluir", font=ft2, command=lambda: (excluir(lb_armaR), atualizarLB(lb_armaR)))
b_excluirR.grid(padx=5, pady=5, column=2, row=1, sticky="ew")

l_classeR = tk.Label(relatorioFr, text="Classes", font=ft2, justify="left")
l_classeR.grid(padx=5, pady=5, column=0, row=3)
lb_classeR = tk.Listbox(relatorioFr, width=30, height=7)
lb_classeR.grid(padx=5, pady=5, column=0, row=4, sticky="ew", columnspan=3)
atualizarLB(lb_classeR)

b_editarR = tk.Button(relatorioFr, text="Editar", font=ft2, command=lambda: editar(lb_classeR))
b_editarR.grid(padx=5, pady=5, column=1, row=3, sticky="ew")
b_excluirR = tk.Button(relatorioFr, text="Excluir", font=ft2, command=lambda: (excluir(lb_classeR), atualizarLB(lb_classeR)))
b_excluirR.grid(padx=5, pady=5, column=2, row=3, sticky="ew")

l_persoR = tk.Label(relatorioFr, text="Personagens", font=ft2, justify="left")
l_persoR.grid(padx=5, pady=5, column=0, row=5)
lb_persoR = tk.Listbox(relatorioFr, width=30, height=7)
lb_persoR.grid(padx=5, pady=5, column=0, row=6, sticky="ew", columnspan=3)
atualizarLB(lb_persoR)

b_editarR = tk.Button(relatorioFr, text="Editar", font=ft2, command=lambda: editar(lb_persoR))
b_editarR.grid(padx=5, pady=5, column=1, row=5, sticky="ew")
b_excluirR = tk.Button(relatorioFr, text="Excluir", font=ft2, command=lambda: (excluir(lb_persoR), atualizarLB(lb_persoR)))
b_excluirR.grid(padx=5, pady=5, column=2, row=5, sticky="ew")


fichaMn.add_command(label="Arma", command=pgArma)
armaFr = tk.Frame(janela)
armaFr.grid_columnconfigure(0, weight=1) 
armaFr.grid_columnconfigure(1, weight=0) 
armaFr.grid_columnconfigure(2, weight=1) 
armaFr.grid_rowconfigure(6, weight=1)

l_tituloA = tk.Label(armaFr, text="Cadastrar Arma", font=ft1, justify="center")
l_tituloA.grid(padx=5, pady=7, column=0, row=0, columnspan=3)
l_nomeA = tk.Label(armaFr, text="Nome", font=ft2)
l_nomeA.grid(padx=5, pady=5, column=0, row=1)
e_nomeA = tk.Entry(armaFr, font=ft3)
e_nomeA.grid(padx=5, pady=5, column=1, row=1) 
l_nivelA = tk.Label(armaFr, text="Nível", font=ft2)
l_nivelA.grid(padx=5, pady=5, column=0, row=2)
e_nivelA = tk.Entry(armaFr, font=ft3)
e_nivelA.grid(padx=5, pady=5, column=1, row=2)
l_alcanceA = tk.Label(armaFr, text="Alcance", font=ft2)
l_alcanceA.grid(padx=5, pady=5, column=0, row=3)
e_alcanceA = tk.Entry(armaFr, font=ft3)
e_alcanceA.grid(padx=5, pady=5, column=1, row=3)
l_municaoA = tk.Label(armaFr, text="Munição", font=ft2, )
l_municaoA.grid(padx=5, pady=5, column=0, row=4)
e_municaoA = tk.Entry(armaFr, font=ft3)
e_municaoA.grid(padx=5, pady=5, column=1, row=4)
l_descA = tk.Label(armaFr, text="Descrição", font=ft2, justify="center")
l_descA.grid(padx=5, pady=5, column=0, row=5)
t_descA = tk.Text(armaFr, font=ft3, width=3, height=5)
t_descA.grid(padx=5, pady=5, column=1, row=5, sticky="nesw")

b_limparA = tk.Button(armaFr, text="Limpar", font=ft2, command=lambda: (limpar(armaFr)))
b_limparA.grid(padx=5, pady=5, column=1, row=6, sticky="ew")
b_salvarA = tk.Button(armaFr, text="Salvar", font=ft2, command=lambda: (salvar(armaFr), atualizarLB(lb_armaR)))
b_salvarA.grid(padx=5, pady=5, column=2, row=6, sticky="ew")


fichaMn.add_command(label="Classe", command=pgClasse)
classeFr = tk.Frame(janela)
classeFr.grid_columnconfigure(0, weight=1) 
classeFr.grid_columnconfigure(1, weight=0) 
classeFr.grid_columnconfigure(2, weight=1)  

l_tituloC = tk.Label(classeFr, text="Cadastrar Classe", font=ft1, justify="center")
l_tituloC.grid(padx=5, pady=7, column=0, row=0, columnspan=3)
l_nomeC = tk.Label(classeFr, text="Nome", font=ft2)
l_nomeC.grid(padx=5, pady=5, column=0, row=1)
e_nomeC = tk.Entry(classeFr, font=ft3)
e_nomeC.grid(padx=5, pady=5, column=1, row=1) 
l_bonusC = tk.Label(classeFr, text="Bônus", font=ft2, justify="center")
l_bonusC.grid(padx=5, pady=5, column=0, row=2)
t_bonusC = tk.Text(classeFr, font=ft3, width=3, height=5)
t_bonusC.grid(padx=5, pady=5, column=1, row=2, sticky="nesw")
l_onusC = tk.Label(classeFr, text="Ônus", font=ft2, justify="center")
l_onusC.grid(padx=5, pady=5, column=0, row=3)
t_onusC = tk.Text(classeFr, font=ft3, width=3, height=5)
t_onusC.grid(padx=5, pady=5, column=1, row=3, sticky="nesw")
l_descC = tk.Label(classeFr, text="Descrição", font=ft2, justify="center")
l_descC.grid(padx=5, pady=5, column=0, row=4)
t_descC = tk.Text(classeFr, font=ft3, width=3, height=5)
t_descC.grid(padx=5, pady=5, column=1, row=4, sticky="nesw")

b_limparC = tk.Button(classeFr, text="Limpar", font=ft2, command=lambda: limpar(classeFr))
b_limparC.grid(padx=5, pady=5, column=1, row=5, sticky="ew")
b_salvarC = tk.Button(classeFr, text="Salvar", font=ft2, command=lambda: (salvar(classeFr), atualizarLB(lb_classeR)))
b_salvarC.grid(padx=5, pady=5, column=2, row=5, sticky="ew")


fichaMn.add_command(label="Personagem", command=pgPersonagem)
personagemFr = tk.Frame(janela)
personagemFr.grid_columnconfigure(0, weight=1) 
personagemFr.grid_columnconfigure(1, weight=0) 
personagemFr.grid_columnconfigure(2, weight=1) 
personagemFr.grid_rowconfigure(5, weight=1)

l_tituloP = tk.Label(personagemFr, text="Cadastrar Personagem", font=ft1, justify="center")
l_tituloP.grid(padx=5, pady=7, column=0, row=0, columnspan=3)
l_nomeP = tk.Label(personagemFr, text="Nome", font=ft1, justify="center")
l_nomeP.grid(padx=5, pady=7, column=0, row=1)
e_nomeP = tk.Entry(personagemFr, font=ft3)
e_nomeP.grid(padx=5, pady=5, column=1, row=1) 
l_descP = tk.Label( personagemFr, text="Descrição", font=ft2, justify="center")
l_descP.grid(padx=5, pady=5, column=0, row=2)
t_descP = tk.Text(personagemFr, font=ft3, width=3, height=5)
t_descP.grid(padx=5, pady=5, column=1, row=2, sticky="nesw")
l_armaP = tk.Label(personagemFr, text="Arma", font=ft1, justify="center")
l_armaP.grid(padx=5, pady=7, column=0, row=3)
armasP = [f"{arma.nome}" for arma in Arma.select()]
c_armaP = ttk.Combobox(personagemFr, values=armasP)
c_armaP.grid(padx=5, pady=5, column=1, row=3) 
l_classeP = tk.Label(personagemFr, text="Classe", font=ft1, justify="center")
l_classeP.grid(padx=5, pady=7, column=0, row=4)
classesP = [f"{classe.nome}" for classe in Classe.select()]
c_classeP = ttk.Combobox(personagemFr, values=classesP)
c_classeP.grid(padx=5, pady=5, column=1, row=4) 

b_limparP = tk.Button(personagemFr, text="Limpar", font=ft2, command=lambda: limpar(personagemFr))
b_limparP.grid(padx=5, pady=5, column=1, row=5, sticky="ew")
b_salvarP = tk.Button(personagemFr, text="Salvar", font=ft2, command=lambda: (salvar(personagemFr), atualizarLB(lb_persoR)))
b_salvarP.grid(padx=5, pady=5, column=2, row=5, sticky="ew")


inicioFr.grid(row=0, column=0, sticky="nesw")
armaFr.grid(row=0, column=0, sticky="nesw")
classeFr.grid(row=0, column=0, sticky="nesw")
personagemFr.grid(row=0, column=0, sticky="nesw")
relatorioFr.grid(row=0, column=0, sticky="nesw")

inicioFr.tkraise()

janela.config(menu=menuB)
janela.mainloop()
