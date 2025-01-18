from tkinter import *
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

def Tela_Lancamentos(root):
    # Limpa tela anterior
    for widget in root.frame_1.winfo_children():
        widget.destroy()

    # Configuração da tela
    root.frame_1.configure(bg="#FDFDE3")

    # Funções
    def scanear():
        # Simula o escaneamento de um código
        entry_codigo.delete(0, tk.END)
        entry_codigo.insert(0, "000122457554412")

    def salvar():
        # Salva os dados inseridos e exibe visual.
        dados = {campo: entry.get() for campo, entry in inputs.items()}
        if all(dados.values()):  # Verifica se todos os campos estão preenchidos
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
            print("Dados salvos:", dados)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")

    def limpar_tudo():
        # Limpa todos os campos
        entry_codigo.delete(0, tk.END)
        for entry in inputs.values():
            entry.delete(0, tk.END)



    # Botão para escanear
    btn_scanear = tk.Button(root.frame_1, text="Scanear", bg="#66CC33", fg="white", font=("Arial bold", 12), command=scanear)
    btn_scanear.place(x=890, y=70, width=100, height=25)

    # Campo para exibir o código escaneado
    entry_codigo = ctk.CTkEntry(root.frame_1, font=("Arial", 12), 
                                width=500, corner_radius=5,fg_color="white",text_color="black",placeholder_text="Código do arquivo")
    entry_codigo.place(x=350, y=70)

    # Campos com labels
    campos = [
        ("Data:", 304, 160),
        ("Valor total da nota:", 202, 210),
        ("Valor total dos produtos:", 156, 260),
        ("Valor dos impostos:", 192, 310),
        ("Operação:", 267, 360),
        ("Emitente:", 272, 410),
        ("Tipo de operação:",664, 160),
        ("Descrição:", 720, 210),
    ]

    # Dicionário para armazenar os inputs
    inputs = {}

    for texto, x, y in campos:
        lbl = tk.Label(root.frame_1, text=texto, bg="#FDFDE3", font=("Helvetica",12,"bold"))
        lbl.place(x=x, y=y)

    #Entradas
    data_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12), width= 200,
                              corner_radius=5,fg_color="white",text_color="black")
    inputs[texto] = data_entry
    data_entry.place(x=350, y=160)

    nota_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12),width=200, 
                             corner_radius=5,fg_color="white", text_color="black")
    inputs[texto] = nota_entry
    nota_entry.place(x=350,y=210)

    produto_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12),width=200, 
                                 corner_radius=5,fg_color="white", text_color="black")
    inputs[texto] = produto_entry
    produto_entry.place(x=350, y=260)

    imp_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12),width=200, 
                             corner_radius=5,fg_color="white", text_color="black")
    inputs[texto] = imp_entry
    imp_entry.place(x=350, y=310)

    oper_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12), width=200, 
                              corner_radius=5,fg_color="white", text_color="black")
    inputs[texto] = oper_entry
    oper_entry.place(x=350,y=360)

    emt_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12), width=200, 
                             corner_radius=5,fg_color="white", text_color="black")
    inputs[texto] = emt_entry
    emt_entry.place(x=350,y=410)
    
    tipo_entry = ctk.CTkEntry(root.frame_1, font=("Arial",12),width=200, 
                              corner_radius=5,fg_color="white", text_color="black")
    inputs[texto] = tipo_entry
    tipo_entry.place(x=810,y=160)

    desc_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12), width=200, 
                              corner_radius=5,fg_color="white", text_color="black")
    inputs[texto] = desc_entry
    desc_entry.place(x=810,y=210)

    # Botões
    btn_salvar = tk.Button(root.frame_1, text="Salvar", bg="#66CC33", fg="white", font=("Arial", 12), command=salvar)
    btn_salvar.place(x=500, y=600, width=120, height=40)

    btn_limpar = tk.Button(root.frame_1, text="Limpar Tudo", bg="#66CC33", fg="white", font=("Arial", 12), command=limpar_tudo)
    btn_limpar.place(x=750, y=600, width=120, height=40)

   #btn_sair = tk.Button(root.frame_1, text="Sair", bg="#FF3333", fg="white", font=("Arial", 12))
   #btn_sair.place(x=750, y=350, width=100, height=30)
    root.mainloop()
