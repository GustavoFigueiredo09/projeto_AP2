from tkinter import *
import tkinter as tk
from tkinter import ttk

def Tela_Contas(instance): 
    for widget in instance.frame_1.winfo_children():
        widget.destroy()

    # Texto teste
    select_label = Label(instance.frame_1, text="",
                         font=(instance.font_2, 15, 'bold'), background=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)
        
    # Botões de saldo, gastos e impostos
    Label(instance.frame_1, text="SALDO", font=("Arial", 12), bg="green", fg="white", width=15).place(x=400, y=130, anchor="center")
    tk.Entry(instance.frame_1, width=15).place(x=400, y=165, anchor="center")
    
    Label(instance.frame_1, text="GASTOS", font=("Arial", 12), bg="green", fg="white", width=15).place(x=600, y=130, anchor="center")
    tk.Entry(instance.frame_1, width=15).place(x=600, y=165, anchor="center")

    Label(instance.frame_1, text="IMPOSTOS", font=("Arial", 12), bg="green", fg="white", width=15).place(x=800, y=130, anchor="center")
    tk.Entry(instance.frame_1, width=15).place(x=800, y=165, anchor="center")

    # Estilo de aparência das colunas
    estilo = ttk.Style()
    estilo.theme_use("default")  # Define o tema padrão
    estilo.configure(
             "Custom.Treeview.Heading", 
             background="green", 
             foreground="white", 
             font=('Arial', 10, 'bold'))
    estilo.map("Custom.Treeview.Heading", 
         background=[("active", "darkgreen")])  # Fundo ao clicar
        
    # Criando o Treeview com o estilo personalizado
    tree = ttk.Treeview(instance.frame_1,
             selectmode='browse',
             columns=('coluna1', 'coluna2', 'coluna3'),
             show='headings',
             style="Custom.Treeview"
         )
            
    # Configurando as colunas
    tree.column('coluna1', width=150, minwidth=50, stretch=NO, anchor='center')
    tree.heading('#1', text='Conta')
            
    tree.column('coluna2', width=150, minwidth=50, stretch=NO, anchor='center')
    tree.heading('#2', text='Banco')
            
    tree.column('coluna3', width=150, minwidth=50, stretch=NO, anchor='center')
    tree.heading('#3', text='Saldo')

    # Função para formatar o valor do saldo com o prefixo "R$"
    def formatar_saldo(valor):

        return f"R$ {valor}"
        
    # Inserindo exemplo na tabela
        # Exemplo 1
    elementos = ['45848-7845', 'Nubank', formatar_saldo(400)]
    tree.insert('', END, values=elementos)

        # Exemplo 2
    elementos = ['45848-7845', 'Pic-Pay', formatar_saldo(400)]
    tree.insert('', END, values=elementos)

    # Usando o método place() para centralizar o Treeview
    tree.place(relx=0.5, rely=0.5, anchor='center')
