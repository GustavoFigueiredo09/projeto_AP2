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

        # Definir tamanho e centralizar a janela
        width = 400
        height = 450
        screen_width = instance.frame_1.winfo_screenwidth()
        screen_height = instance.frame_1.winfo_screenheight()
        x_position = (screen_width // 2) - (width // 2)
        y_position = (screen_height // 2) - (height // 2)
        cadastro_window.geometry(f"{width}x{height}+{x_position}+{y_position}")

        # Campos de entrada
        labels = ["Razão Social", "Nome Fantasia", "Email", "Contato", "CPF/CNPJ"]
        entries = []

        for i, label_text in enumerate(labels):
            label = Label(cadastro_window, text=label_text, font=(instance.font_4, 12))
            label.pack(pady=5, padx=20, anchor="w")
            entry = Entry(cadastro_window, width=30, font=(instance.font_4, 14))
            entry.insert(0, dados[label_text.lower().replace(" ", "_")] if dados else "")
            entry.pack(pady=5, padx=20, anchor="w")
            entries.append(entry)

        # Mapeando os campos às variáveis corretas
        razao_entry, nome_entry, email_entry, contato_entry, cpf_cnpj_entry = entries

        # Botão para salvar
        salvar_button = Button(cadastro_window, text="Salvar", font=(instance.font_4, 12), command=salvar, bg="#67a516", fg="white")
        salvar_button.pack(pady=20)

    def editar_terceiro():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")

            editar_window = Toplevel(instance.frame_1)
            editar_window.title("Editar Terceiro")

            # Definição do tamanho e centralização da janela
            width = 400
            height = 450
            screen_width = instance.frame_1.winfo_screenwidth()
            screen_height = instance.frame_1.winfo_screenheight()
            x_position = (screen_width // 2) - (width // 2)
            y_position = (screen_height // 2) - (height // 2)
            editar_window.geometry(f"{width}x{height}+{x_position}+{y_position}")

            # Campos de entrada
            labels = ["Razão Social", "Nome Fantasia", "Email", "Telefone", "CPF/CNPJ"]
            entries = []

            for i, label_text in enumerate(labels):
                label = Label(editar_window, text=label_text, font=(instance.font_4, 12))
                label.pack(pady=5, padx=20, anchor="w")
                entry = Entry(editar_window, width=30, font=(instance.font_4, 14))
                entry.insert(0, item_values[i])
                entry.pack(pady=5, padx=20, anchor="w")
                entries.append(entry)

            # Função para salvar alterações
            def salvar_edicao():
                dados_editados = {
                    "razao": entries[0].get(),
                    "nome_fantasia": entries[1].get(),
                    "email": entries[2].get(),
                    "telefone": entries[3].get(),
                    "cpf_cnpj": entries[4].get(),
                }

                if all(dados_editados.values()):  # Verifica se todos os campos estão preenchidos
                    terceiro = Terceiro()
                    terceiro.update(dados_editados, f'cpf_cnpj = "{item_values[4]}"')  # Usa o CPF/CNPJ como identificador

                    messagebox.showinfo("Sucesso", "Terceiro editado com sucesso!")
                    editar_window.destroy()
                    carregar_dados_tabela()
                else:
                    messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

            # Botão para salvar as edições
            salvar_button = Button(editar_window, text="Salvar", font=(instance.font_4, 12), command=salvar_edicao, bg="#67a516", fg="white")
            salvar_button.pack(pady=20)

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
