import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
from modelos import *

def inicio():
    inicioFr.tkraise()

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

def nomeS(listB):
    slc = listB.curselection()
    if not slc:
        return None
    idx = slc[0]
    
    for i in range(idx, -1, -1):
        line = listB.get(i)
        if line.strip().startswith(">Nome"):
            parts = line.split(":")
            if len(parts) >= 2:
                return parts[1].strip()
            else:
                return line.replace(">Nome", "").strip()
   
    line = listB.get(idx)
    if ":" in line:
        return line.split(":")[-1].strip()
    return None

def salvar(pg): 
     if pg == armaFr:
          try:
               nivelA = int(e_nivelA.get())
          except:
               mb.showerror("Erro", "Nível é obrigatório precisa ser um número!")
          try:
               nomeA = e_nomeA.get().strip()
               alcanceA = e_alcanceA.get().strip()
               descricaoA =  t_descA.get("1.0",  "end-1c").strip()
          except:
               mb.showerror("Erro", "Nome, Alcance e Descrição são obrigatórios!")
               return
          
          municaoA = e_municaoA.get().strip()
          Arma.create(nome=nomeA, nivel=nivelA, alcance=alcanceA, municao=municaoA, descricao=descricaoA)
          limpar(armaFr)

     elif pg == classeFr:
          try:
               nomeC = e_nomeC.get().strip()  
               descricaoC = t_descC.get("1.0",  "end-1c").strip()
          except:
               mb.showerror("Erro", "Nome e Descrição são obrigatórios!")
               return
          
          bonusC = t_bonusC.get("1.0",  "end-1c").strip()
          onusC = t_onusC.get("1.0",  "end-1c").strip()

          Classe.create(nome=nomeC, bonus=bonusC, onus=onusC, descricao=descricaoC)
          limpar(classeFr)

     elif pg == personagemFr:
          try:
               nomeP = e_nomeP.get().strip()
               descricaoP = t_descP.get("1.0", "end-1c").strip()
               armaNome = c_armaP.get().strip()
               classeNome = c_classeP.get().strip()

               armaP = Arma.get(Arma.nome == armaNome) if armaNome else None
               classeP = Classe.get(Classe.nome == classeNome)
          except:
               mb.showerror("Erro", "Nome, Descrição e Classe são obrigatórios!")
               return

          Personagem.create(nome=nomeP, descricao=descricaoP, arma=armaP, classe=classeP)
          limpar(personagemFr)

def atualizarLB(listB):
     if listB == lb_armaR:
          lb_armaR.delete(0, tk.END)

          armaCad = Arma.select()

          for arma in armaCad:
               lb_armaR.insert(tk.END, "-" * 100)
               lb_armaR.insert(tk.END, f">Nome      :  {(arma.nome)}")
               lb_armaR.insert(tk.END, f">Nível        :  {(arma.nivel)}")
               lb_armaR.insert(tk.END, f">Alcance   :  {(arma.alcance)}")
               mun = (arma.municao)
               lb_armaR.insert(tk.END, f">Munição :  {mun if mun else 'Nenhuma'}")
               lb_armaR.insert(tk.END, f">Descrição:  {(arma.descricao)}")     

     elif listB == lb_classeR:
          lb_classeR.delete(0, tk.END)

          classeCad = Classe.select()

          for classe in classeCad:
               lb_classeR.insert(tk.END, "-" * 100)
               lb_classeR.insert(tk.END, f">Nome       :  {(classe.nome)}")
               bonus = (classe.bonus)
               onus = (classe.onus)
               lb_classeR.insert(tk.END, f">Bônus       :  {bonus if bonus else 'Nenhum'}")
               lb_classeR.insert(tk.END, f">Ônus        :  {onus if onus else 'Nenhum'}")
               lb_classeR.insert(tk.END, f">Descrição:  {(classe.descricao)}")  

     elif listB == lb_persoR:
          lb_persoR.delete(0, tk.END)

          persoCad = Personagem.select()

          for perso in persoCad:
               lb_persoR.insert(tk.END, "-" * 100)
               lb_persoR.insert(tk.END, f">Nome      :  {(perso.nome)}")
               lb_persoR.insert(tk.END, f">Descrição:  {(perso.descricao)}")
               try:
                    arma_nome = perso.arma.nome if perso.arma else None
               except:
                    arma_nome = None
               lb_persoR.insert(tk.END, f">Arma       :  {(arma_nome) if arma_nome else 'Não possui'}")
               try:
                    classe_nome = perso.classe.nome if perso.classe else None
               except:
                    classe_nome = None
               lb_persoR.insert(tk.END, f">Classe      :  {(classe_nome)}") 

def atualizarCB():
    c_armaP['values'] = [(arma.nome) for arma in Arma.select()]
    c_classeP['values'] = [(classe.nome) for classe in Classe.select()]

def excluir(listB):
     nomeEx = nomeS(listB)
     if not nomeEx:
          mb.showwarning("Aviso", "Selecione um item válido (linha com '>Nome').")
          return

     try:
          if listB == lb_armaR:
               ex = Arma.get(Arma.nome == nomeEx)
               ex.delete_instance()
          elif listB == lb_classeR:
               ex = Classe.get(Classe.nome == nomeEx)
               ex.delete_instance()
          elif listB == lb_persoR:
               ex = Personagem.get(Personagem.nome == nomeEx)
               ex.delete_instance()
     except Exception as exc:
          mb.showerror("Erro", f"Falha ao excluir: {exc}")
          return
     
     atualizarLB(listB)
     atualizarCB()

def editar2(pg):
     if pg == armaFr:
          edt.nome = e_nomeA.get().strip()
          edt.nivel = int(e_nivelA.get())
          edt.alcance = e_alcanceA.get().strip()
          edt.municao = e_municaoA.get().strip() or None
          edt.descricao = t_descA.get("1.0", "end-1c").strip()
          edt.save()
          limpar(armaFr)
          

     elif pg == classeFr:
          edt.nome = e_nomeC.get().strip()
          edt.bonus = t_bonusC.get("1.0", "end-1c").strip() or None
          edt.onus = t_onusC.get("1.0", "end-1c").strip() or None
          edt.descricao = t_descC.get("1.0", "end-1c").strip()
          edt.save()
          limpar(classeFr)
          

     elif pg == personagemFr:
          edt.nome = e_nomeP.get().strip()
          edt.descricao = t_descP.get("1.0", "end-1c").strip()
          arma_nome = c_armaP.get().strip()
          classe_nome = c_classeP.get().strip()
          edt.arma = Arma.get(Arma.nome == arma_nome) if arma_nome else None
          edt.classe = Classe.get(Classe.nome == classe_nome) if classe_nome else None
          edt.save()
          limpar(personagemFr)
     
     pgRelatorio()

def alterarBt():
     b_salvarA.config(text="Salvar", command=lambda: (salvar(armaFr), atualizarLB(lb_armaR), atualizarCB()))
     b_salvarC.config(text="Salvar", command=lambda: (salvar(classeFr), atualizarLB(lb_classeR), atualizarCB()))
     b_salvarP.config(text="Salvar", command=lambda: (salvar(personagemFr), atualizarLB(lb_persoR), atualizarCB()))

def editar(listB):
    global edt
    edt = None

    slc = listB.curselection()
    if not slc:
          return
    nome = nomeS(listB)
    if not nome:
        mb.showwarning("Aviso", "Selecione uma linha válida contendo '>Nome'.")
        return

    if listB == lb_armaR:
        edt = Arma.get(Arma.nome == nome)
        e_nomeA.delete(0, tk.END)
        e_nomeA.insert(0, (edt.nome))
        e_nivelA.delete(0, tk.END)
        e_nivelA.insert(0, (edt.nivel))
        e_alcanceA.delete(0, tk.END)
        e_alcanceA.insert(0, (edt.alcance))
        e_municaoA.delete(0, tk.END)
        e_municaoA.insert(0, (edt.municao))
        t_descA.delete("1.0", tk.END)
        t_descA.insert("1.0", (edt.descricao))
        pgArma()
        
        b_salvarA.config(text="Editar", command=lambda: (editar2(armaFr), atualizarLB(lb_armaR), alterarBt()))
        


    elif listB == lb_classeR:
        edt = Classe.get(Classe.nome == nome)
        e_nomeC.delete(0, tk.END)
        e_nomeC.insert(0, (edt.nome))
        t_bonusC.delete("1.0", tk.END)
        t_bonusC.insert("1.0", (edt.bonus))
        t_onusC.delete("1.0", tk.END)
        t_onusC.insert("1.0", (edt.onus))
        t_descC.delete("1.0", tk.END)
        t_descC.insert("1.0", (edt.descricao))
        pgClasse()

        b_salvarC.config(text="Editar", command=lambda: (editar2(classeFr), atualizarLB(lb_classeR), alterarBt()))

    elif listB == lb_persoR:
        edt = Personagem.get(Personagem.nome == nome)
        e_nomeP.delete(0, tk.END)
        e_nomeP.insert(0, (edt.nome))
        t_descP.delete("1.0", tk.END)
        t_descP.insert("1.0", (edt.descricao))
        try:
            c_armaP.set((edt.arma.nome) if edt.arma else "")
        except:
            c_armaP.set("")
        try:
            c_classeP.set((edt.classe.nome) if edt.classe else "")
        except:
            c_classeP.set("")
        pgPersonagem()

        b_salvarP.config(text="Editar", command=lambda: (editar2(personagemFr), atualizarLB(lb_persoR), alterarBt()))


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

b_editarAR = tk.Button(relatorioFr, text="Editar", font=ft2, command=lambda: editar(lb_armaR))
b_editarAR.grid(padx=5, pady=5, column=1, row=1, sticky="ew")
b_excluirAR = tk.Button(relatorioFr, text="Excluir", font=ft2, command=lambda: (excluir(lb_armaR)))
b_excluirAR.grid(padx=5, pady=5, column=2, row=1, sticky="ew")

l_classeR = tk.Label(relatorioFr, text="Classes", font=ft2, justify="left")
l_classeR.grid(padx=5, pady=5, column=0, row=3)
lb_classeR = tk.Listbox(relatorioFr, width=30, height=7)
lb_classeR.grid(padx=5, pady=5, column=0, row=4, sticky="ew", columnspan=3)
atualizarLB(lb_classeR)

b_editarCR = tk.Button(relatorioFr, text="Editar", font=ft2, command=lambda: editar(lb_classeR))
b_editarCR.grid(padx=5, pady=5, column=1, row=3, sticky="ew")
b_excluirCR = tk.Button(relatorioFr, text="Excluir", font=ft2, command=lambda: (excluir(lb_classeR)))
b_excluirCR.grid(padx=5, pady=5, column=2, row=3, sticky="ew")

l_persoR = tk.Label(relatorioFr, text="Personagens", font=ft2, justify="left")
l_persoR.grid(padx=5, pady=5, column=0, row=5)
lb_persoR = tk.Listbox(relatorioFr, width=30, height=7)
lb_persoR.grid(padx=5, pady=5, column=0, row=6, sticky="ew", columnspan=3)
atualizarLB(lb_persoR)

b_editarPR = tk.Button(relatorioFr, text="Editar", font=ft2, command=lambda: editar(lb_persoR))
b_editarPR.grid(padx=5, pady=5, column=1, row=5, sticky="ew")
b_excluirPR = tk.Button(relatorioFr, text="Excluir", font=ft2, command=lambda: (excluir(lb_persoR)))
b_excluirPR.grid(padx=5, pady=5, column=2, row=5, sticky="ew")


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
b_salvarA = tk.Button(armaFr, text="Salvar", font=ft2, command=lambda: (salvar(armaFr), atualizarLB(lb_armaR), atualizarCB()))
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
t_bonusC = tk.Text(classeFr, font=ft3, width=3, height=3)
t_bonusC.grid(padx=5, pady=5, column=1, row=2, sticky="nesw")
l_onusC = tk.Label(classeFr, text="Ônus", font=ft2, justify="center")
l_onusC.grid(padx=5, pady=5, column=0, row=3)
t_onusC = tk.Text(classeFr, font=ft3, width=3, height=3)
t_onusC.grid(padx=5, pady=5, column=1, row=3, sticky="nesw")
l_descC = tk.Label(classeFr, text="Descrição", font=ft2, justify="center")
l_descC.grid(padx=5, pady=5, column=0, row=4)
t_descC = tk.Text(classeFr, font=ft3, width=3, height=5)
t_descC.grid(padx=5, pady=5, column=1, row=4, sticky="nesw")

b_limparC = tk.Button(classeFr, text="Limpar", font=ft2, command=lambda: limpar(classeFr))
b_limparC.grid(padx=5, pady=5, column=1, row=5, sticky="ew")
b_salvarC = tk.Button(classeFr, text="Salvar", font=ft2, command=lambda: (salvar(classeFr), atualizarLB(lb_classeR), atualizarCB()))
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
l_descP = tk.Label(personagemFr, text="Descrição", font=ft2, justify="center")
l_descP.grid(padx=5, pady=5, column=0, row=2)
t_descP = tk.Text(personagemFr, font=ft3, width=3, height=5)
t_descP.grid(padx=5, pady=5, column=1, row=2, sticky="nesw")
l_armaP = tk.Label(personagemFr, text="Arma", font=ft1, justify="center")
l_armaP.grid(padx=5, pady=7, column=0, row=3)
armasP = [(arma.nome) for arma in Arma.select()]
c_armaP = ttk.Combobox(personagemFr, values=armasP)
c_armaP.grid(padx=5, pady=5, column=1, row=3)
l_classeP = tk.Label(personagemFr, text="Classe", font=ft1, justify="center")
l_classeP.grid(padx=5, pady=7, column=0, row=4)
classesP = [(classe.nome) for classe in Classe.select()]
c_classeP = ttk.Combobox(personagemFr, values=classesP)
c_classeP.grid(padx=5, pady=5, column=1, row=4)

b_limparP = tk.Button(personagemFr, text="Limpar", font=ft2, command=lambda: limpar(personagemFr))
b_limparP.grid(padx=5, pady=5, column=1, row=5, sticky="ew")
b_salvarP = tk.Button(personagemFr, text="Salvar", font=ft2, command=lambda: (salvar(personagemFr), atualizarLB(lb_persoR), atualizarCB()))
b_salvarP.grid(padx=5, pady=5, column=2, row=5, sticky="ew")


inicioFr.grid(row=0, column=0, sticky="nesw")
armaFr.grid(row=0, column=0, sticky="nesw")
classeFr.grid(row=0, column=0, sticky="nesw")
personagemFr.grid(row=0, column=0, sticky="nesw")
relatorioFr.grid(row=0, column=0, sticky="nesw")

inicioFr.tkraise()

janela.config(menu=menuB)
janela.mainloop()
