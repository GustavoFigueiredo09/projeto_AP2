from tkinter import *
import tkinter as tk
from tkinter import ttk

def Tela_Contas(instance): 
    instance.ClearScreen()

    # Texto teste
    select_label = Label(instance.frame_1, text="Bem-Vindo a tela Bancos",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)
  
    # Função para exibir a tabela dentro da janela principal
    def btn_sal_gas_imp():
        
        # Botões de saldo, gastos e impostos
        tk.Button(instance.frame_1, text="SALDO", font=("Arial", 12), bg="green", fg="white", width=15).place(x=100, y=50)
        tk.Entry(instance.frame_1, width=15, ).place(x=100, y=90)
    
        tk.Button(instance.frame_1, text="GASTOS", font=("Arial", 12), bg="green", fg="white", width=15).place(x=300, y=50)
        tk.Entry(instance.frame_1, width=15).place(x=300, y=90)

        tk.Button(instance.frame_1, text="IMPOSTOS", font=("Arial", 12), bg="green", fg="white", width=15).place(x=500, y=50)
        tk.Entry(instance.frame_1, width=15).place(x=500, y=90)
    def tabela():
    
        # Estilo de aparência das colunas
        estilo = ttk.Style()
        estilo.theme_use("default")  # Define o tema padrão
        estilo.configure(
            "Custom.Treeview.Heading", 
            background="green", 
            foreground="black", 
            font=('Arial', 10, 'bold'))
        estilo.map("Custom.Treeview.Heading", 
        background=[("active", "darkgreen")])  # Fundo ao clicar
        
        # Criando o Treeview com o estilo personalizado
        tree = ttk.Treeview(
            selectmode='browse',
            columns=('coluna1', 'coluna2', 'coluna3', 'coluna4'),
            show='headings',
            style="Custom.Treeview"
        )
            
        # Configurando as colunas
        tree.column('coluna1', width=150, minwidth=50, stretch=NO, anchor='center')
        tree.heading('#1', text='Conta')
            
        tree.column('coluna2', width=150, minwidth=50, stretch=NO, anchor='center')
        tree.heading('#2', text='Banco')
            
        tree.column('coluna3', width=100, minwidth=50, stretch=NO, anchor='center')
        tree.heading('#3', text='Saldo')

        tree.column('coluna4', width=100, minwidth=50, stretch=NO, anchor='center')
        tree.heading('#4', text='Situação')

        # Combobox - Selecionar Ativo ou Inativo
        # app = Tk()
        # situacao = ["Ativo", "Inativo"]
        # label_situacao = Label(app,text="Situação")
        # label_situacao.pack()

        # cb_situacao = ttk.Combobox(app,values=label_situacao)
        # cb_situacao.set('') # Deixa a opção vazia
        # cb_situacao.pack()


        # Função para formatar o valor do saldo com o prefixo "R$"
        def formatar_saldo(valor):
            return f"R$ {valor}"
        
        # Inserindo exemplo na tabela
        # Exemplo 1
        elementos = ['45848-7845', 'Nubank', formatar_saldo(400), 'Inativo']
        tree.insert('', END, values=elementos)

        # Exemplo 2
        elementos = ['45848-7845', 'Pic-Pay', formatar_saldo(400), 'Ativo']
        tree.insert('', END, values=elementos)

        # Usando o método place() para centralizar o Treeview
        tree.place(relx=0.5, rely=0.5, anchor='center')

    # Chama a função para exibir a tabela na janela principal
    btn_sal_gas_imp()
    tabela()