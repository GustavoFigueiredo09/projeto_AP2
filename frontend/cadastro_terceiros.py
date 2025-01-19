from tkinter import *
from tkinter import ttk

def Cadastro_Terceiros(instance): 
    instance.ClearScreen()

    # Texto de boas-vindas
    select_label = Label(instance.frame_1, text="Bem-Vindo à tela de cadastros de terceiros",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    # Variável para armazenar a opção selecionada
    selecionado = StringVar(value="Cliente")  # Valor inicial

    # Função de callback para alternância
    def alternar_opcao(*args):
        print(f"Opção selecionada: {selecionado.get()}")
        if selecionado.get() == "Cliente":
            print("Configurações adicionais para Cliente.")
        elif selecionado.get() == "Fornecedor":
            print("Configurações adicionais para Fornecedor.")
        elif selecionado.get() == "Transportadora":
            print("Configurações padrão para Transportadora.")

    # Vincular a função de callback à variável
    selecionado.trace("w", alternar_opcao)

    # Criando o OptionMenu
    opcoes = ["Cliente", "Cliente", "Fornecedor", "Transportadora"]
    dropdown = ttk.OptionMenu(instance.frame_1, selecionado, *opcoes)
    dropdown.place(x=200, y=350)

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
    email_label = Label(instance.frame_1, text="Telefone/Celular:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    email_label.place(x=70, y=250)

    email_entry = Entry(instance.frame_1, width=13, font=(instance.font_4, 14))
    email_entry.place(x=200, y=250)

    # Caixa de entrada para "CPF/CNPJ"
    name_label = Label(instance.frame_1, text="CPF/CNPJ:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    name_label.place(x=105, y=300)

    name_entry = Entry(instance.frame_1, width=20, font=(instance.font_4, 14))
    name_entry.place(x=200, y=300)

    # Caixa de entrada para "Categoria"
    email_label = Label(instance.frame_1, text="Categoria:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    email_label.place(x=112, y=350)

    # Caixa de entrada para "Código"
    email_label = Label(instance.frame_1, text="Código:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    email_label.place(x=128, y=400)

    email_entry = Entry(instance.frame_1, width=10, font=(instance.font_4, 14))
    email_entry.place(x=200, y=400)

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
