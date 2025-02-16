from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar
from backend.database.models.lancamentos import Lancamento

def Tela_Lancamentos(root):
    # Limpa tela anterior
    for widget in root.frame_1.winfo_children():
        widget.destroy()

    style = ttk.Style()
    style.configure("Custom.TCombobox", font=("Arial", 14))  

    def salvar():
        dados = {"codigo":entry_cod.get(),
                 "data": data_entry.get(),
                 "valor_total": nota_entry.get(),
                 "valor_pago": produto_entry.get(),
                 "impostos": imp_entry.get(),
                 "operacao": oper_entry.get(),
                 "emitente": emt_entry.get(),
                 "tipo_operacao": cb_tipo.get(),
                 "banco": cb_banco.get(),
                 "descricao": desc_entry.get()
        }
        if all(dados.values()):  
            lancamento = Lancamento()
            if dados:
                if lancamento.read(filtro=f'codigo = {dados['codigo']}'):
                    messagebox.showwarning("Aviso", "Dado já existe no banco! Favor inserir outro código.")
                    return
                
                lancamento.create(dados)
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
            print("Dados salvos:", dados)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")   

    def limpar_tudo():
        # Limpa todos os campos
        entry_cod.delete(0, tk.END)
        data_entry.delete(0,tk.END)
        nota_entry.delete(0,tk.END)
        produto_entry.delete(0,tk.END)
        imp_entry.delete(0,tk.END)
        oper_entry.delete(0,tk.END)
        emt_entry.delete(0,tk.END)
        cb_tipo.delete(0, tk.END)
        cb_banco.delete(0, tk.END)
        desc_entry.delete(0,tk.END)
    
    def excluir_lancamento():
        codigo = entry_cod.get().strip()
        print(codigo)
        lancamento = Lancamento()  # Criando um objeto da classe Lancamento

        if not codigo:
            messagebox.showwarning("Aviso", "Digite um código antes de excluir!")
            return

        try: 
            lancamento.remove_por_codigo(codigo) # Chama diretamente a função
            messagebox.showinfo("Sucesso", "Lançamento excluído com sucesso!")
  
        except:
            messagebox.showwarning("Aviso", "Nenhum lançamento encontrado com esse código!")
    

    def abrir_calendario():
    
        def selecionar_data():
            # Insere a data selecionada no campo de entrada e fecha o calendário.
            data_entry.delete(0, tk.END)
            data_entry.insert(0, cal.get_date())
            top.destroy()

        # Criando a janela do calendário
        top = tk.Toplevel(root.frame_1)
        top.title("Selecionar Data")

        largura = 200
        altura = 240
        pos_x = 420  # Posição X na tela
        pos_y = 230  # Posição Y na tela
        top.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")  # Define tamanho e posição
        top.maxsize(200,240)

        cal = Calendar(top, date_pattern="yyyy-mm-dd")  # Define o formato da data
        cal.pack(pady=10)

        ttk.Button(top, text="Selecionar", command=selecionar_data).pack(pady=5)


    #Labels & Entradas 
    label_lancamento = Label(root.frame_1, text="Tela de Lançamentos", font=("Arial", 15, "bold"),bg="#FDFDE3")
    label_lancamento.place(x=600,y=10)

    label_cod = Label(root.frame_1, text="Código:", bg="#FDFDE3", font=("Arial", 12))
    label_cod.place(x=285, y=110)
    entry_cod = Entry(root.frame_1,font=("Arial", 12),width= 72 )
    entry_cod.place(x=350, y=110)

    #LABEL E ENTRADA DATA
    lbl_data = tk.Label(root.frame_1, text="Data:", bg="#FDFDE3", font=("Arial",12))
    lbl_data.place(x=304,y=160)
    data_entry = Entry(root.frame_1, font=("Arial", 12), width= 20)
    data_entry.place(x=350, y=160)

    #LABEL E ENTRADA VALOR
    lbl_valor = tk.Label(root.frame_1, text="Valor total da nota:", bg="#FDFDE3", font=("Arial",12))
    lbl_valor.place(x=210,y=210)
    nota_entry = Entry(root.frame_1, font=("Arial", 12),width=20)
    nota_entry.place(x=350,y=210)

    #LABEL E ENTRADA PRODUTO
    lbl_produto = tk.Label(root.frame_1, text="Valor total dos produtos:", bg="#FDFDE3", font=("Arial",12))
    lbl_produto.place(x=170,y=260)
    produto_entry = Entry(root.frame_1, font=("Arial", 12),width=20)
    produto_entry.place(x=350, y=260)

    #LABEL E ENTRADA IMPOSTOS
    lbl_impostos = tk.Label(root.frame_1, text="Valor dos impostos:", bg="#FDFDE3", font=("Arial",12))
    lbl_impostos.place(x=200,y=310)
    imp_entry = Entry(root.frame_1, font=("Arial", 12),width=20)
    imp_entry.place(x=350, y=310)

    #LABEL E ENTRADA OPERAÇÃO
    lbl_operacao= tk.Label(root.frame_1, text="Operação:", bg="#FDFDE3", font=("Arial",12))
    lbl_operacao.place(x=267,y=360)
    oper_entry = Entry(root.frame_1, font=("Arial", 12), width=20)
    oper_entry.place(x=350,y=360)

    #LABEL E ENTRADA EMITENTE
    lbl_emitente = tk.Label(root.frame_1, text="Emitente:", bg="#FDFDE3", font=("Arial",12))
    lbl_emitente.place(x=274,y=410)
    emt_entry = Entry(root.frame_1, font=("Arial", 12), width=20)
    emt_entry.place(x=350,y=410)

    #LABEL TIPO DE OPERÇÃO E COMBOBOX OPÇÕES
    lbl_tipo = tk.Label(root.frame_1, text="Tipo de operação:", bg="#FDFDE3", font=("Arial",12))
    lbl_tipo.place(x=668,y=160)
    opcoes = ["Entrada", "Saída"]
    cb_tipo = ttk.Combobox(root.frame_1, values=opcoes, width=27, style="Custom.TCombobox")
    cb_tipo.place(x=810,y=160)

    #LABEL BANCO E COMBOBOX OPÇÕES DE BANCO
    lbl_banco = tk.Label(root.frame_1, text="Banco:", bg="#FDFDE3", font=("Arial",12))
    lbl_banco.place(x=748,y=210)
    opcoes_banco = ["Nubank", "Pic-Pay", "Inter", "Itaú", "Mercado Pago", "Caixa", "Will"]
    cb_banco = ttk.Combobox(root.frame_1, values=opcoes_banco, width=27)
    cb_banco.place(x=810,y=210)

    # LABEL E ENTRADA DESCRIÇÃO
    lbl_descricao = tk.Label(root.frame_1, text="Descrição:", bg="#FDFDE3", font=("Arial",12))
    lbl_descricao.place(x=720,y=260)
    desc_entry = Entry(root.frame_1, font=("Arial", 12), width=20)
    desc_entry.place(x=810,y=260)

    # Botões
    btn_salvar = tk.Button(root.frame_1, text="Salvar", bg="#66CC33", fg="white", font=("Arial", 12),command=salvar)
    btn_salvar.place(x=400, y=500, width=120, height=40)

    btn_limpar = tk.Button(root.frame_1, text="Limpar Tudo", bg="#66CC33", fg="white", font=("Arial", 12), command=limpar_tudo)
    btn_limpar.place(x=600, y=500, width=120, height=40)

    btn_Excluir = tk.Button(root.frame_1, text="Excluir Lançamento",bg="#A60808", fg="white", font=("Arial"), command=excluir_lancamento)
    btn_Excluir.place(x=800,y=500,height=40)

    btn_calendario = ttk.Button(root.frame_1, text="Data",command=abrir_calendario)
    btn_calendario.place(x=265,y=160)