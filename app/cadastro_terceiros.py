import re
from tkinter import *
from tkinter import ttk

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

    # Tabela de terceiro
    tree = ttk.Treeview(instance.frame_1, columns=("Razão social", "Nome fantasia", "Email", "Contato", "CPF/CNPJ", "Categoria"), show="headings")

    # Definição dos cabeçalhos
    tree.heading("Razão social", text="Razão social")
    tree.heading("Nome fantasia", text="Nome fantasia")
    tree.heading("Email", text="Email")
    tree.heading("Contato", text="Contato")
    tree.heading("CPF/CNPJ", text="CPF/CNPJ")
    tree.heading("Categoria", text="Categoria")

    tree.column("Razão social", width=200)
    tree.column("Nome fantasia", width=200)
    tree.column("Email", width=200)
    tree.column("Contato", width=150)
    tree.column("CPF/CNPJ", width=150)
    tree.column("Categoria", width=100)

    tree.place(x=80, y=100, width=1050, height=400)

    # Carregando dados do banco
    def carregar_dados_tabela(filtro=None):
        usuario = Terceiros()
        dados_terceiros = terceiros.busca_todos() if filtro is None else terceiros.busca_por_nome(filtro)
        for item in tree.get_children():
            tree.delete(item)
        for terceiro in dados_terceiros:
            tree.insert("", "end", values=(terceiro['razao'], terceiro['nome_fantasia'],  terceiro['email'], terceiro['telefone'], tercerio['cpf_cnpj']))

    # Filtragem dos dados por nome
    def filtrar_por_nome():
        nome_busca = search_entry.get().lower()
        if nome_busca:
            carregar_dados_tabela(nome_busca)
        else:
            carregar_dados_tabela()

    # Botão de busca
    search_button = Button(instance.frame_1, text="Buscar", font=(instance.font_4, 12), command=filtrar_por_nome, bg="#67a516", fg="white")
    search_button.place(x=770, y=55)

    # Carrega dados ao iniciar
    carregar_dados_tabela()

    # Edita o terceiro
    def editar_terceiro():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")
            
            # Janela pop-up para editar as informações do terceiro
            editar_window = Toplevel(instance.frame_1)
            editar_window.title("Editar Terceiro")
            
            # Tamanho da janela pop-up
            width = 400
            height = 500
            screen_width = instance.frame_1.winfo_screenwidth()
            screen_height = instance.frame_1.winfo_screenheight()
            x_position = (screen_width // 2) - (width // 2)
            y_position = (screen_height // 2) - (height // 2)
            editar_window.geometry(f"{width}x{height}+{x_position}+{y_position}")
            
            # Entrada para as informações do tercerio
            razao_label = Label(editar_window, text="Razão social", font=(instance.font_4, 12))
            razao_label.pack(pady=10, padx=20, anchor="w")
            razao_entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
            razao_entry.insert(0, item_values[0])
            razao_entry.pack(pady=5, padx=20, anchor="w")
            
            nome_label = Label(editar_window, text="Nome fantasia", font=(instance.font_4, 12))
            nome_label.pack(pady=10, padx=20, anchor="w")
            nome_entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
            nome_entry.insert(0, item_values[1])
            nome_entry.pack(pady=5, padx=20, anchor="w")
            
            email_label = Label(editar_window, text="Email", font=(instance.font_4, 12))
            email_label.pack(pady=10, padx=20, anchor="w")
            email_entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
            email_entry.insert(0, item_values[2])
            email_entry.pack(pady=5, padx=20, anchor="w")
            
            contato_label = Label(editar_window, text="Contato", font=(instance.font_4, 12))
            contato_label.pack(pady=10, padx=20, anchor="w")
            contato_label = Entry(editar_window, width=30, font=(instance.font_4, 14), show="*")
            contato_entry.insert(0, item_values[3])
            contato_entry.pack(pady=5, padx=20, anchor="w")

            cpf_cnpj_label = Label(editar_window, text="CPF/CNPJ", font=(instance.font_4, 12))
            cpf_cnpj_label.pack(pady=10, padx=20, anchor="w")
            cpf_cnpj_entry = Entry(editar_window, width=30, font=(instance.font_4, 14), show="*")
            cpf_cnpj_entry.insert(0, item_values[3])
            cpf_cnpj_entry.pack(pady=5, padx=20, anchor="w")

            # Função para salvar as edições
            def salvar_edicao():
                razao = razao_entry.get()
                nome = nome_entry.get()
                email = email_entry.get()
                contato = contato_entry.get()
                cpf_cnpj = cpf_cnpj_entry.get()

                if razao and nome and email and contato and cpf_cnpj:
                    tercerio = Terceiro()
                    dados_dict = {
                        "nome": nome,
                        "email": email,
                        "login": login,
                        "senha": senha,
                        "adm": admin
                    }

                    messagebox.showinfo("Sucesso", "Terceiro editado com sucesso!")
                    editar_window.destroy()
                    carregar_dados_tabela()
                else:
                    messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

            # Botão para salvar as edições
            salvar_button = Button(editar_window, text="Salvar", font=(instance.font_4, 12), command=salvar_edicao, bg="#67a516", fg="white")
            salvar_button.pack(pady=20)

    # Remover o terceiro
    def remover_terceiro():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")
            terceiro = Terceiro()
            terceiro.busca_por_nome(item_values[0])
            tercerio.delete(f"nome = '{item_values[0]}'")
            carregar_dados_tabela()
            messagebox.showinfo("Sucesso", "Terceiro removido com sucesso!")

    # Abri o cadastro de novo terceiro
    def novo_terceiro():
        cadastro_window = Toplevel(instance.frame_1)
        cadastro_window.title("Cadastro de Novo Terceiro")

        # Tamanho da janela pop-up
        width = 400
        height = 500
        screen_width = instance.frame_1.winfo_screenwidth()
        screen_height = instance.frame_1.winfo_screenheight()
        x_position = (screen_width // 2) - (width // 2)
        y_position = (screen_height // 2) - (height // 2)
        cadastro_window.geometry(f"{width}x{height}+{x_position}+{y_position}")

        # Entrada para as informações do tercerio
        razao_label = Label(editar_window, text="Razão social", font=(instance.font_4, 12))
        razao_label.pack(pady=10, padx=20, anchor="w")
        razao_entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
        razao_entry.insert(0, item_values[0])
        razao_entry.pack(pady=5, padx=20, anchor="w")
            
        nome_label = Label(editar_window, text="Nome fantasia", font=(instance.font_4, 12))
        nome_label.pack(pady=10, padx=20, anchor="w")
        nome_entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
        nome_entry.insert(0, item_values[1])
        nome_entry.pack(pady=5, padx=20, anchor="w")
            
        email_label = Label(editar_window, text="Email", font=(instance.font_4, 12))
        email_label.pack(pady=10, padx=20, anchor="w")
        email_entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
        email_entry.insert(0, item_values[2])
        email_entry.pack(pady=5, padx=20, anchor="w")
            
        contato_label = Label(editar_window, text="Contato", font=(instance.font_4, 12))
        contato_label.pack(pady=10, padx=20, anchor="w")
        contato_label = Entry(editar_window, width=30, font=(instance.font_4, 14), show="*")
        contato_entry.insert(0, item_values[3])
        contato_entry.pack(pady=5, padx=20, anchor="w")

        cpf_cnpj_label = Label(editar_window, text="CPF/CNPJ", font=(instance.font_4, 12))
        cpf_cnpj_label.pack(pady=10, padx=20, anchor="w")
        cpf_cnpj_entry = Entry(editar_window, width=30, font=(instance.font_4, 14), show="*")
        cpf_cnpj_entry.insert(0, item_values[3])
        cpf_cnpj_entry.pack(pady=5, padx=20, anchor="w")

        # Salva novo tercerio
        def salvar_terceiro():
            razao = razao_entry.get()
            nome = nome_entry.get()
            email = email_entry.get()
            contato = contato_entry.get()
            cpf_cnpj = cpf_cnpj_entry.get()

            if razao and nome and email and contato and cpf_cnpj:
                tercerio = Terceiro()
                dados_dict = {
                    "nome": nome,
                    "email": email,
                    "login": login,
                    "senha": senha,
                    "adm": admin
                }

                usuario.registra_usuarios(dados_dict)
                messagebox.showinfo("Sucesso", "Terceiro cadastrado com sucesso!")
                cadastro_window.destroy()
                carregar_dados_tabela()
            else:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

        # Botão para salvar novo tercerio
        salvar_button = Button(cadastro_window, text="Salvar", font=(instance.font_4, 12), command=salvar_terceiro, bg="#67a516", fg="white")
        salvar_button.pack(pady=20)

    # Botões "Novo"
    novo_button = Button(instance.frame_1, text=" + Novo", font=(instance.font_4, 12), command=novo_terceiro, bg="#67a516", fg="white")
    novo_button.place(x=475, y=550)

    # Botão "Editar"
    editar_button = Button(instance.frame_1, text="Editar", font=(instance.font_4, 12), command=editar_terceiro, bg="#67a516", fg="white")
    editar_button.place(x=580, y=550)

    # Botão "Remover"
    remover_button = Button(instance.frame_1, text="Remover", font=(instance.font_4, 12), command=remover_terceiro, bg="#67a516", fg="white")
    remover_button.place(x=675, y=550)
