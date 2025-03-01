import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from backend.database.models.usuarios import Usuario  # Importar a classe Usuario

def Cadastro_Usuario(instance): 
    instance.ClearScreen()

    # Texto de boas-vindas
    select_label = Label(instance.frame_1, text="Cadastros de usuários",
                         font=(instance.font_4, 20, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=440, y=10)

    # Texto pesquisa
    search_label = Label(instance.frame_1, text="Pesquisar:",
                         font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    search_label.place(x=335, y=60)

    # Caixa de pesquisa
    search_entry = Entry(instance.frame_1, width=30, font=(instance.font_4, 14))
    search_entry.place(x=420, y=60)

    # Tabela de Usuários
    tree = ttk.Treeview(instance.frame_1, columns=("Nome", "Email", "Login", "Senha", "Categoria"), show="headings")
    tree.heading("Nome", text="Nome")
    tree.heading("Email", text="Email")
    tree.heading("Login", text="Login")
    tree.heading("Senha", text="Senha")
    tree.heading("Categoria", text="Categoria")

    tree.column("Nome", width=200)
    tree.column("Email", width=200)
    tree.column("Login", width=150)
    tree.column("Senha", width=150)
    tree.column("Categoria", width=100)

    tree.place(x=120, y=100, width=950, height=400)

    # Carregando os dados dos usuários
    def carregar_dados_tabela(filtro=None):
        usuario = Usuario()
        dados_usuarios = usuario.busca_todos() if filtro is None else usuario.busca_por_nome(filtro)
        for item in tree.get_children():
            tree.delete(item)
        for usuario in dados_usuarios:
            tree.insert("", "end", values=(usuario['nome'], usuario['email'], usuario['login'], usuario['senha'], "Administrador" if usuario['adm'] == 1 else "Normal"))

    # Filtragem dos nomes para pesquisa
    def filtrar_por_nome():
        nome_busca = search_entry.get().lower()
        if nome_busca:
            carregar_dados_tabela(nome_busca)
        else:
            carregar_dados_tabela()

    # Botão de busca
    search_button = Button(instance.frame_1, text="Buscar", font=(instance.font_4, 12), command=filtrar_por_nome, bg="#67a516", fg="white")
    search_button.place(x=770, y=55)

    # Carregando dados ao iniciar
    carregar_dados_tabela()

    # Edita o usuário
    def editar_usuario():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")
            
            # Janela pop-up para editar as informações do usuário
            editar_window = Toplevel(instance.frame_1)
            editar_window.title("Editar Usuário")
            
            # Define o tamanho da janela pop-up
            width = 400
            height = 500
            screen_width = instance.frame_1.winfo_screenwidth()
            screen_height = instance.frame_1.winfo_screenheight()
            x_position = (screen_width // 2) - (width // 2)
            y_position = (screen_height // 2) - (height // 2)
            editar_window.geometry(f"{width}x{height}+{x_position}+{y_position}")
            
            # Entradas para as informações do usuário
            nome_label = Label(editar_window, text="Nome", font=(instance.font_4, 12))
            nome_label.pack(pady=10, padx=20, anchor="w")
            nome_entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
            nome_entry.insert(0, item_values[0])
            nome_entry.pack(pady=5, padx=20, anchor="w")
            
            email_label = Label(editar_window, text="Email", font=(instance.font_4, 12))
            email_label.pack(pady=10, padx=20, anchor="w")
            email_entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
            email_entry.insert(0, item_values[1])
            email_entry.pack(pady=5, padx=20, anchor="w")
            
            login_label = Label(editar_window, text="Login", font=(instance.font_4, 12))
            login_label.pack(pady=10, padx=20, anchor="w")
            login_entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
            login_entry.insert(0, item_values[2])
            login_entry.pack(pady=5, padx=20, anchor="w")
            
            senha_label = Label(editar_window, text="Senha", font=(instance.font_4, 12))
            senha_label.pack(pady=10, padx=20, anchor="w")
            senha_entry = Entry(editar_window, width=30, font=(instance.font_4, 14), show="*")
            senha_entry.insert(0, item_values[3])
            senha_entry.pack(pady=5, padx=20, anchor="w")
            
            admin_label = Label(editar_window, text="Categoria", font=(instance.font_4, 12))
            admin_label.pack(pady=10, padx=20, anchor="w")
            admin_var = IntVar()
            admin_check = Checkbutton(editar_window, text="Administrador", variable=admin_var, font=(instance.font_4, 12))
            if item_values[4] == "Administrador":
                admin_var.set(1)
            admin_check.pack(pady=5, padx=20, anchor="w")

            # Salva as edições
            def salvar_edicao():
                nome = nome_entry.get()
                email = email_entry.get()
                login = login_entry.get()
                senha = senha_entry.get()
                admin = 1 if admin_var.get() else 0

                if nome and email and login and senha:
                    usuario = Usuario()
                    dados_dict = {
                        "nome": nome,
                        "email": email,
                        "login": login,
                        "senha": senha,
                        "adm": admin
                    }
                    
                    # Atualizar diretamente os dados no banco
                    usuario.update(dados_dict, f'login = "{login}"')  # Usa o login como identificador
                    
                    messagebox.showinfo("Sucesso", "Usuário editado com sucesso!")
                    editar_window.destroy()
                    carregar_dados_tabela()
                else:
                    messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

            # Botão para salvar as edições
            salvar_button = Button(editar_window, text="Salvar", font=(instance.font_4, 12), command=salvar_edicao, bg="#67a516", fg="white")
            salvar_button.pack(pady=20)


    # Remove o usuário
    def remover_usuario():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")
            usuario = Usuario()
            usuario.busca_por_nome(item_values[0])
            usuario.delete(f"nome = '{item_values[0]}'")
            carregar_dados_tabela() 
            messagebox.showinfo("Sucesso", "Usuário removido com sucesso!")

    # Cadastro de novo usuário
    def novo_usuario():
        cadastro_window = Toplevel(instance.frame_1)
        cadastro_window.title("Cadastro de Novo Usuário")

        # Define o tamanho da janela pop-up
        width = 400
        height = 500
        screen_width = instance.frame_1.winfo_screenwidth()
        screen_height = instance.frame_1.winfo_screenheight()
        x_position = (screen_width // 2) - (width // 2)
        y_position = (screen_height // 2) - (height // 2)
        cadastro_window.geometry(f"{width}x{height}+{x_position}+{y_position}")

        # Entrada para as informações do usuário
        nome_label = Label(cadastro_window, text="Nome", font=(instance.font_4, 12))
        nome_label.pack(pady=10,padx=20, anchor="w")
        nome_entry = Entry(cadastro_window, width=30, font=(instance.font_4, 12))
        nome_entry.pack(pady=5, padx=20, anchor="w")

        email_label = Label(cadastro_window, text="Email", font=(instance.font_4, 12))
        email_label.pack(pady=10, padx=20, anchor="w")
        email_entry = Entry(cadastro_window, width=30, font=(instance.font_4, 14))
        email_entry.pack(pady=5, padx=20, anchor="w")

        login_label = Label(cadastro_window, text="Login", font=(instance.font_4, 12))
        login_label.pack(pady=10, padx=20, anchor="w")
        login_entry = Entry(cadastro_window, width=30, font=(instance.font_4, 14))
        login_entry.pack(pady=5, padx=20, anchor="w")

        senha_label = Label(cadastro_window, text="Senha", font=(instance.font_4, 12))
        senha_label.pack(pady=10, padx=20, anchor="w")
        senha_entry = Entry(cadastro_window, width=30, font=(instance.font_4, 14), show="*")
        senha_entry.pack(pady=5, padx=20, anchor="w")

        admin_label = Label(cadastro_window, text="Categoria", font=(instance.font_4, 12))
        admin_label.pack(pady=10, padx=20, anchor="w")
        admin_var = IntVar()
        admin_check = Checkbutton(cadastro_window, text="Administrador", variable=admin_var, font=(instance.font_4, 12))
        admin_check.pack(pady=5, padx=20, anchor="w")

        # Salva o novo usuário
        def salvar_usuario():
            nome = nome_entry.get()
            email = email_entry.get()
            login = login_entry.get()
            senha = senha_entry.get()
            admin = 1 if admin_var.get() else 0

            if nome and email and login and senha:
                usuario = Usuario()
                dados_dict = {
                    "nome": nome,
                    "email": email,
                    "login": login,
                    "senha": senha,
                    "adm": admin
                }
                usuario.registra_usuarios(dados_dict)
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                cadastro_window.destroy()
                carregar_dados_tabela()
            else:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

        # Botão para salvar o novo usuário
        salvar_button = Button(cadastro_window, text="Salvar", font=(instance.font_4, 12), command=salvar_usuario, bg="#67a516", fg="white")
        salvar_button.pack(pady=20)

    # Botões "Novo"
    novo_button = Button(instance.frame_1, text=" + Novo", font=(instance.font_4, 12), command=novo_usuario, bg="#67a516", fg="white")
    novo_button.place(x=475, y=550)

    # Botão "Editar"
    editar_button = Button(instance.frame_1, text="Editar", font=(instance.font_4, 12), command=editar_usuario, bg="#67a516", fg="white")
    editar_button.place(x=580, y=550)

    # Botão "Remover"
    remover_button = Button(instance.frame_1, text="Remover", font=(instance.font_4, 12), command=remover_usuario, bg="#67a516", fg="white")
    remover_button.place(x=675, y=550)
