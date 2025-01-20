from tkinter import *
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

def Tela_Lancamentos(root):
    # Limpa tela anterior
    for widget in root.frame_1.winfo_children():
        widget.destroy()


    # Funções
    def scanear():
        # Simula o escaneamento de um código
        entry_codigo.delete(0, tk.END)
        entry_codigo.insert(0, "000122457554412")

    def salvar():
        dados = {"código:": entry_codigo.get(),
                 "Data:": data_entry.get(),
                 "Valor total da nota:": nota_entry.get(),
                 "Valor dos produtos:": produto_entry.get(),
                 "Valor dos impostos:": imp_entry.get(),
                 "Operação:": oper_entry.get(),
                 "Emitente:": emt_entry.get(),
                 "Tipo de operação:": tipo_entry.get(),
                 "Descrição:": desc_entry.get()
        }
        if all(dados.values()):  
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
            print("Dados salvos:", dados)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")   

    def limpar_tudo():
        # Limpa todos os campos
        entry_codigo.delete(0, tk.END)
        data_entry.delete(0,tk.END)
        nota_entry.delete(0,tk.END)
        produto_entry.delete(0,tk.END)
        imp_entry.delete(0,tk.END)
        oper_entry.delete(0,tk.END)
        emt_entry.delete(0,tk.END)
        tipo_entry.delete(0,tk.END)
        desc_entry.delete(0,tk.END)
        


    # Botão para escanear
    btn_scanear = tk.Button(root.frame_1, text="Scanear", bg="#66CC33", fg="white", font=("Arial bold", 12), command=scanear)
    btn_scanear.place(x=890, y=70, width=100, height=25)

    # Campo para exibir o código escaneado
    entry_codigo = ctk.CTkEntry(root.frame_1, font=("Arial", 12), 
                                width=500, corner_radius=5,fg_color="white",text_color="black",placeholder_text="Código do arquivo")
    entry_codigo.place(x=350, y=70)

    #Labels & Entradas 
    lbl_data = tk.Label(root.frame_1, text="Data:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_data.place(x=304,y=160)
    data_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12), width= 200,
                              fg_color="white",text_color="black")
    data_entry.place(x=350, y=160)

    lbl_valor = tk.Label(root.frame_1, text="Valor total da nota:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_valor.place(x=202,y=210)
    nota_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12),width=200, 
                             fg_color="white", text_color="black")
    nota_entry.place(x=350,y=210)

    lbl_produto = tk.Label(root.frame_1, text="Valor total dos produtos:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_produto.place(x=156,y=260)
    produto_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12),width=200, 
                                 fg_color="white", text_color="black")
    produto_entry.place(x=350, y=260)

    lbl_impostos = tk.Label(root.frame_1, text="Valor dos impostos:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_impostos.place(x=192,y=310)
    imp_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12),width=200, 
                             fg_color="white", text_color="black")
    imp_entry.place(x=350, y=310)

    lbl_operacao= tk.Label(root.frame_1, text="Operação:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_operacao.place(x=267,y=360)
    oper_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12), width=200, 
                             fg_color="white", text_color="black")
    oper_entry.place(x=350,y=360)

    lbl_emitente = tk.Label(root.frame_1, text="Emitente:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_emitente.place(x=272,y=410)
    emt_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12), width=200, 
                             fg_color="white", text_color="black")
    emt_entry.place(x=350,y=410)

    lbl_tipo = tk.Label(root.frame_1, text="Tipo de operação:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_tipo.place(x=664,y=160)
    tipo_entry = ctk.CTkEntry(root.frame_1, font=("Arial",12),width=200, 
                              fg_color="white", text_color="black")
    tipo_entry.place(x=810,y=160)

    lbl_descricao = tk.Label(root.frame_1, text="Descrição:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_descricao.place(x=720,y=210)
    desc_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12), width=200, 
                             fg_color="white", text_color="black")
    desc_entry.place(x=810,y=210)

    # Botões
    btn_salvar = tk.Button(root.frame_1, text="Salvar", bg="#66CC33", fg="white", font=("Arial", 12),command=salvar)
    btn_salvar.place(x=400, y=500, width=120, height=40)

    btn_limpar = tk.Button(root.frame_1, text="Limpar Tudo", bg="#66CC33", fg="white", font=("Arial", 12), command=limpar_tudo)
    btn_limpar.place(x=600, y=500, width=120, height=40)

    btn_Excluir = tk.Button(root.frame_1, text="Excluir Lançamento",bg="#A60808", fg="white", font=("Arial"))
    btn_Excluir.place(x=800,y=500,height=40)

