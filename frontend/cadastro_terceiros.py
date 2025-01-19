import re
from tkinter import *
from tkinter import ttk

def Cadastro_Terceiros(instance): 
    instance.ClearScreen()

    # Restrigindo a entrar para aceitar apenas numeros
    def validar_entrada_numerica(char):
        return bool(re.match("[0-9]", char))

    # Texto de boas-vindas
    select_label = Label(instance.frame_1, text="Bem-Vindo à tela de cadastros de terceiros",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    # Armazenar a opção selecionada
    selecionado = StringVar(value="Cliente")  

    # Caixa de seleção
    def alternar_opcao(*args):
        print(f"Opção selecionada: {selecionado.get()}")
        if selecionado.get() == "Cliente":
            print("Configurações adicionais para Cliente.")
        elif selecionado.get() == "Fornecedor":
            print("Configurações adicionais para Fornecedor.")
        elif selecionado.get() == "Transportadora":
            print("Configurações padrão para Transportadora.")

    selecionado.trace("w", alternar_opcao)

    # Caixa de entrada para "Razão social"
    name_label = Label(instance.frame_1, text="Razão Social:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    name_label.place(x=90, y=100)

    name_entry = Entry(instance.frame_1, width=40, font=(instance.font_4, 14))
    name_entry.place(x=200, y=100)

    # Caixa de entrada para "Nome fantasia"
    email_label = Label(instance.frame_1, text="Nome fantasia:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    email_label.place(x=82, y=150)

    email_entry = Entry(instance.frame_1, width=40, font=(instance.font_4, 14))
    email_entry.place(x=200, y=150)

    # Caixa de entrada para "Email"
    name_label = Label(instance.frame_1, text="Email:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    name_label.place(x=142, y=200)

    name_entry = Entry(instance.frame_1, width=30, font=(instance.font_4, 14))
    name_entry.place(x=200, y=200)

    # Caixa de entrada para "Telefone/Celular"
    telefone_label = Label(instance.frame_1, text="Telefone/Celular:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    telefone_label.place(x=70, y=250)

    # Variável de controle para validação de números
    validate_cmd_numerico = instance.frame_1.register(validar_entrada_numerica)

    telefone_entry = Entry(instance.frame_1, width=13, font=(instance.font_4, 14), validate="key", validatecommand=(validate_cmd_numerico, "%S"))
    telefone_entry.place(x=200, y=250)

    # Caixa de entrada para "CPF/CNPJ"
    cpf_cnpj_label = Label(instance.frame_1, text="CPF/CNPJ:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    cpf_cnpj_label.place(x=105, y=300)

    cpf_cnpj_entry = Entry(instance.frame_1, width=20, font=(instance.font_4, 14), validate="key", validatecommand=(validate_cmd_numerico, "%S"))
    cpf_cnpj_entry.place(x=200, y=300)

    # Caixa de entrada para "Categoria"
    categoria_label = Label(instance.frame_1, text="Categoria:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    categoria_label.place(x=112, y=350)

    opcoes = ["Cliente", "Cliente", "Fornecedor", "Transportadora"]
    dropdown = ttk.OptionMenu(instance.frame_1, selecionado, *opcoes)
    dropdown.place(x=200, y=350)

    # Caixa de entrada para "Código"
    codigo_label = Label(instance.frame_1, text="Código:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    codigo_label.place(x=128, y=400)

    codigo_entry = Entry(instance.frame_1, width=10, font=(instance.font_4, 14), validate="key", validatecommand=(validate_cmd_numerico, "%S"))
    codigo_entry.place(x=200, y=400)

    # Botão Salvar
    merge_button = Button(instance.frame_1, text="Salvar",
                          font=(instance.font_3, 15, 'bold'), bg=instance.color_4, fg=instance.color_1,
                          width=12, command=instance.Select_Arquivo)
    merge_button.place(x=350, y=540)

    # Botão Excluir
    delete_button = Button(instance.frame_1, text="Excluir",
                           font=(instance.font_3, 15, 'bold'), bg=instance.color_4, fg=instance.color_1,
                           width=12, command=instance.delete_list_items)
    delete_button.place(x=550, y=540)

    # Botão Consultar
    save_button = Button(instance.frame_1, text="Consultar",
                         font=(instance.font_3, 15, 'bold'), bg=instance.color_4, fg=instance.color_1,
                         width=12, command=instance.delete_list_items)
    save_button.place(x=750, y=540)
