from tkinter import *
from tkinter import ttk

def Cadastro_Usuario(instance): 
    instance.ClearScreen()

    # Texto teste
    select_label = Label(instance.frame_1, text="Bem-Vindo a tela de cadastros de usuários",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    # Variável para armazenar a opção selecionada
    selecionado = StringVar(value="Cliente")  # Valor inicial

    # Função de callback para alternância
    def alternar_opcao(*args):
        print(f"Opção selecionada: {selecionado.get()}")
        if selecionado.get() == "Administrador":
            print("Configurações adicionais para Administrador.")
        elif selecionado.get() == "Normal":
            print("Configurações adicionais para Fornecedor.")
        
    # Vincular a função de callback à variável
    selecionado.trace("w", alternar_opcao)

    # Criando o OptionMenu
    opcoes = ["Administrador", "Administrador", "Normal"]
    dropdown = ttk.OptionMenu(instance.frame_1, selecionado, *opcoes)
    dropdown.place(x=200, y=250)

    # Caixa de entrada para "Nome completo"
    name_label = Label(instance.frame_1, text="Nome completo:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    name_label.place(x=70, y=100)

    name_entry = Entry(instance.frame_1, width=40, font=(instance.font_4, 14))
    name_entry.place(x=200, y=100)

    # Caixa de entrada para "Email"
    email_label = Label(instance.frame_1, text="Email:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    email_label.place(x=138, y=150)

    email_entry = Entry(instance.frame_1, width=40, font=(instance.font_4, 14))
    email_entry.place(x=200, y=150)

    # Caixa de entrada para "Data de Nascimento"
    date_label = Label(instance.frame_1, text="Data de nascimento:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    date_label.place(x=40, y=200)

    date_entry = Entry(instance.frame_1, width=13, font=(instance.font_4, 14))
    date_entry.place(x=200, y=200)

    # Caixa de entrada para "Perfil"
    profile_label = Label(instance.frame_1, text="Perfil:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    profile_label.place(x=142, y=250)

    # Caixa de entrada para "Login"
    login_label = Label(instance.frame_1, text="Login:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    login_label.place(x=139, y=300)

    login_entry = Entry(instance.frame_1, width=20, font=(instance.font_4, 14))
    login_entry.place(x=200, y=300)

    # Caixa de entrada para "Senha"
    password_label = Label(instance.frame_1, text="Senha:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    password_label.place(x=135, y=350)

    password_entry = Entry(instance.frame_1, width=13, font=(instance.font_4, 14), show="*")
    password_entry.place(x=200, y=350)

    # Caixa de entrada para "Repetir senha"
    repeat_password_label = Label(instance.frame_1, text="Repetir senha:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    repeat_password_label.place(x=82, y=400)

    repeat_password_entry = Entry(instance.frame_1, width=13, font=(instance.font_4, 14), show="*")
    repeat_password_entry.place(x=200, y=400)

    # Caixa de entrada para "Código"
    code_label = Label(instance.frame_1, text="Código:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    code_label.place(x=128, y=450)

    code_entry = Entry(instance.frame_1, width=10, font=(instance.font_4, 14))
    code_entry.place(x=200, y=450)

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
