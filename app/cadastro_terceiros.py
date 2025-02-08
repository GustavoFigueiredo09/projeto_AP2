import re
from tkinter import *
from tkinter import ttk, messagebox
from backend.database.models.terceiros import Terceiros

def Cadastro_Terceiros(instance): 
    instance.ClearScreen()

    # Texto de boas-vindas
    select_label = Label(instance.frame_1, text="Cadastros de terceiros",
                         font=(instance.font_4, 20, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=440, y=10)

    # Caixa de pesquisa
    search_label = Label(instance.frame_1, text="Pesquisar:",
                         font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    search_label.place(x=335, y=60)

    search_entry = Entry(instance.frame_1, width=30, font=(instance.font_4, 14))
    search_entry.place(x=420, y=60)

    # Tabela de terceiros
    tree = ttk.Treeview(instance.frame_1, columns=("Razão social", "Nome fantasia", "Email", "Contato", "CPF/CNPJ"), show="headings")
    for col in ("Razão social", "Nome fantasia", "Email", "Contato", "CPF/CNPJ"):
        tree.heading(col, text=col)
        tree.column(col, width=200)
    
    tree.place(x=80, y=100, width=1050, height=400)

    def carregar_dados_tabela(filtro=None):
        terceiro = Terceiros()
        dados_terceiros = terceiro.read() if filtro is None else terceiro.read(f"razao LIKE '%{filtro}%' OR nome_fantasia LIKE '%{filtro}%'")
        
        tree.delete(*tree.get_children())
        for t in dados_terceiros:
            tree.insert("", "end", values=(t['razao'], t['nome_fantasia'], t['email'], t['telefone'], t['cpf_cnpj']))

    def filtrar_por_nome():
        nome_busca = search_entry.get().strip()
        carregar_dados_tabela(nome_busca if nome_busca else None)

    search_button = Button(instance.frame_1, text="Buscar", font=(instance.font_4, 12), command=filtrar_por_nome, bg="#67a516", fg="white")
    search_button.place(x=770, y=55)

    carregar_dados_tabela()

    def abrir_janela_terceiro(dados=None):
        def salvar():
            novo_dados = {
                "razao": razao_entry.get(),
                "nome_fantasia": nome_entry.get(),
                "email": email_entry.get(),
                "telefone": contato_entry.get(),
                "cpf_cnpj": cpf_cnpj_entry.get()
            }
            
            if all(novo_dados.values()):
                terceiro = Terceiros()
                if dados:
                    terceiro.update(novo_dados, f"razao = '{dados['razao']}'")
                else:
                    terceiro.create(novo_dados)
                messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
                cadastro_window.destroy()
                carregar_dados_tabela()
            else:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        
        cadastro_window = Toplevel(instance.frame_1)
        cadastro_window.title("Editar Terceiro" if dados else "Novo Terceiro")
        cadastro_window.geometry("400x400")
        
        Label(cadastro_window, text="Razão Social").pack()
        razao_entry = Entry(cadastro_window, width=30)
        razao_entry.pack()
        razao_entry.insert(0, dados["razao"] if dados else "")
        
        Label(cadastro_window, text="Nome Fantasia").pack()
        nome_entry = Entry(cadastro_window, width=30)
        nome_entry.pack()
        nome_entry.insert(0, dados["nome_fantasia"] if dados else "")
        
        Label(cadastro_window, text="Email").pack()
        email_entry = Entry(cadastro_window, width=30)
        email_entry.pack()
        email_entry.insert(0, dados["email"] if dados else "")
        
        Label(cadastro_window, text="Contato").pack()
        contato_entry = Entry(cadastro_window, width=30)
        contato_entry.pack()
        contato_entry.insert(0, dados["telefone"] if dados else "")
        
        Label(cadastro_window, text="CPF/CNPJ").pack()
        cpf_cnpj_entry = Entry(cadastro_window, width=30)
        cpf_cnpj_entry.pack()
        cpf_cnpj_entry.insert(0, dados["cpf_cnpj"] if dados else "")
        
        Button(cadastro_window, text="Salvar", command=salvar, bg="#67a516", fg="white").pack()

    def editar_terceiro():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")
            dados = {
                "razao": item_values[0],
                "nome_fantasia": item_values[1],
                "email": item_values[2],
                "telefone": item_values[3],
                "cpf_cnpj": item_values[4]
            }
            abrir_janela_terceiro(dados)
        else:
            messagebox.showerror("Erro", "Selecione um terceiro para editar.")
    
    def remover_terceiro():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")
            terceiro = Terceiros()
            terceiro.delete(f"razao = '{item_values[0]}'")
            messagebox.showinfo("Sucesso", "Terceiro removido com sucesso!")
            carregar_dados_tabela()
        else:
            messagebox.showerror("Erro", "Selecione um terceiro para remover.")
    
    novo_button = Button(instance.frame_1, text="+ Novo", font=(instance.font_4, 12), command=lambda: abrir_janela_terceiro(), bg="#67a516", fg="white")
    novo_button.place(x=375, y=550)

    editar_button = Button(instance.frame_1, text="Editar", font=(instance.font_4, 12), command=editar_terceiro, bg="#67a516", fg="white")
    editar_button.place(x=575, y=550)

    remover_button = Button(instance.frame_1, text="Remover", font=(instance.font_4, 12), command=remover_terceiro, bg="#67a516", fg="white")
    remover_button.place(x=775, y=550)
