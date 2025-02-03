import re
from tkinter import *
from tkinter import ttk
from backend.database.models.usuarios import Usuario  # Importar a classe Usuario

def Cadastro_Usuario(instance): 
    instance.ClearScreen()

    # Texto de boas-vindas
    select_label = Label(instance.frame_1, text="Cadastros de usuários",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    # Caixa de pesquisa
    search_label = Label(instance.frame_1, text="Pesquisar:",
                         font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    search_label.place(x=335, y=60)

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

    def carregar_dados_tabela(filtro=None):
        # Criar uma instância da classe Usuario
        usuario = Usuario()

        # Consultar todos os usuários ou filtrar por nome
        dados_usuarios = usuario.busca_todos() if filtro is None else usuario.busca_por_nome(filtro)

        # Limpar a tabela antes de inserir os novos dados
        for item in tree.get_children():
            tree.delete(item)

        # Inserir os dados na tabela
        for usuario in dados_usuarios:
            tree.insert("", "end", values=(usuario['nome'], usuario['email'], usuario['login'], usuario['senha'], "Administrador" if usuario['admin'] == 1 else "Normal"))

    def filtrar_por_nome():
        nome_busca = search_entry.get().lower()
        if nome_busca:
            # Chama a função de carregar dados filtrados
            carregar_dados_tabela(nome_busca)
        else:
            # Se o campo estiver vazio, carregar todos os dados
            carregar_dados_tabela()

    # Botão de buscar
    search_button = Button(instance.frame_1, text="Buscar", font=(instance.font_4, 12), command=filtrar_por_nome)
    search_button.place(x=770, y=55)

    # Carregar todos os dados ao iniciar
    carregar_dados_tabela()  # Carregar todos os dados na tabela ao iniciar

    # Função para adicionar um novo usuário
    def novo_usuario():
        # Aqui você pode abrir uma nova tela ou realizar a inserção diretamente
        print("Abrir formulário para adicionar um novo usuário.")

    # Função para editar um usuário
    def editar_usuario():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")
            print(f"Editar usuário: {item_values}")
            # Aqui você pode abrir um formulário para editar os dados do usuário selecionado

    # Função para remover um usuário
    def remover_usuario():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")
            usuario = Usuario()
            usuario.busca_por_nome(item_values[0])  # Filtrar pelo nome para encontrar o ID
            # Agora, você pode remover o usuário da base de dados
            print(f"Remover usuário: {item_values}")
            # Remover da tabela (remover do banco de dados)
            usuario.delete(f"nome = '{item_values[0]}'")
            # Atualizar a tabela
            carregar_dados_tabela()

    # Botões de ações
    novo_button = Button(instance.frame_1, text=" + Novo", font=(instance.font_4, 12), command=novo_usuario)
    novo_button.place(x=475, y=550)

    editar_button = Button(instance.frame_1, text="Editar", font=(instance.font_4, 12), command=editar_usuario)
    editar_button.place(x=580, y=550)

    remover_button = Button(instance.frame_1, text="Remover", font=(instance.font_4, 12), command=remover_usuario)
    remover_button.place(x=675, y=550)
