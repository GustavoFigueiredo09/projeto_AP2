from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from backend.database.models.lancamentos import Lancamento
def Tela_Lancamentos(root):
    # Limpa tela anterior
    for widget in root.frame_1.winfo_children():
        widget.destroy()

    style = ttk.Style()
    style.configure("Custom.TCombobox", font=("Arial", 14))  

    def salvar():
        dados = {"data": data_entry.get(),
                #  "codigo":entry_codigo.get(),
                 "valor_total": nota_entry.get(),
                 "valor_pago": produto_entry.get(),
                 "impostos": imp_entry.get(),
                 "operacao": oper_entry.get(),
                 "emitente": emt_entry.get(),
                 "tipo_operacao": cb_tipo.get(),
                 "descricao": desc_entry.get()
        }
        if all(dados.values()):  
            lancamento = Lancamento()
            if dados:
                lancamento.create(dados)
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
            print("Dados salvos:", dados)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")   

    def limpar_tudo():
        # Limpa todos os campos
        # entry_codigo.delete(0, tk.END)
        data_entry.delete(0,tk.END)
        nota_entry.delete(0,tk.END)
        produto_entry.delete(0,tk.END)
        imp_entry.delete(0,tk.END)
        oper_entry.delete(0,tk.END)
        emt_entry.delete(0,tk.END)
        cb_tipo.delete(0, tk.END)
        cb_banco.delete(0, tk.END)
        desc_entry.delete(0,tk.END)
        
    #def excluir_lancamento():
    # 
    # 
    # 
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

    opcoes = ["Entrada", "Saída"]
    cb_tipo = ttk.Combobox(root.frame_1, values=opcoes, width=40, style="Custom.TCombobox")
    cb_tipo.place(x=810,y=160)

    lbl_banco = tk.Label(root.frame_1, text="Banco:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_banco.place(x=720,y=210)

    opcoes_banco = ["Nubank", "Pic-Pay", "Inter", "Itaú", "Mercado Pago", "Caixa", "Will"]
    cb_banco = ttk.Combobox(root.frame_1, values=opcoes_banco, width=40)
    cb_banco.place(x=810,y=210)

    lbl_descricao = tk.Label(root.frame_1, text="Descrição:", bg="#FDFDE3", font=("Helvetica",12,"bold"))
    lbl_descricao.place(x=720,y=260)
    desc_entry = ctk.CTkEntry(root.frame_1, font=("Arial", 12), width=200, 
                             fg_color="white", text_color="black")
    desc_entry.place(x=810,y=260)

    # Botões
    btn_salvar = tk.Button(root.frame_1, text="Salvar", bg="#66CC33", fg="white", font=("Arial", 12),command=salvar)
    btn_salvar.place(x=400, y=500, width=120, height=40)

    btn_limpar = tk.Button(root.frame_1, text="Limpar Tudo", bg="#66CC33", fg="white", font=("Arial", 12), command=limpar_tudo)
    btn_limpar.place(x=600, y=500, width=120, height=40)

    btn_Excluir = tk.Button(root.frame_1, text="Excluir Lançamento",bg="#A60808", fg="white", font=("Arial"))
    btn_Excluir.place(x=800,y=500,height=40)