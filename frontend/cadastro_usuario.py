from tkinter import *

def Cadastro_Usuario(instance): 
    instance.ClearScreen()

    # Texto teste
    select_label = Label(instance.frame_1, text="Bem-Vindo a telal de cadastros de usuários",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

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
    name_label = Label(instance.frame_1, text="Data de nascimento:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    name_label.place(x=40, y=200)

    name_entry = Entry(instance.frame_1, width=13, font=(instance.font_4, 14))
    name_entry.place(x=200, y=200)

    # Caixa de entrada para "Perfil"
    email_label = Label(instance.frame_1, text="Perfil:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    email_label.place(x=142, y=250)

    email_entry = Entry(instance.frame_1, width=13, font=(instance.font_4, 14))
    email_entry.place(x=200, y=250)

    # Caixa de entrada para "Login"
    name_label = Label(instance.frame_1, text="Login:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    name_label.place(x=139, y=300)

    name_entry = Entry(instance.frame_1, width=20, font=(instance.font_4, 14))
    name_entry.place(x=200, y=300)

    # Caixa de entrada para "Senha"
    email_label = Label(instance.frame_1, text="Senha:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    email_label.place(x=135, y=350)

    email_entry = Entry(instance.frame_1, width=13, font=(instance.font_4, 14))
    email_entry.place(x=200, y=350)

    # Caixa de entrada para "Repetir senha"
    name_label = Label(instance.frame_1, text="Repetir senha:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    name_label.place(x=82, y=400)

    name_entry = Entry(instance.frame_1, width=13, font=(instance.font_4, 14))
    name_entry.place(x=200, y=400)

    # Caixa de entrada para "Código"
    email_label = Label(instance.frame_1, text="Código:",
        font=(instance.font_4, 12), bg=instance.color_2, fg=instance.color_3)
    email_label.place(x=128, y=450)

    email_entry = Entry(instance.frame_1, width=10, font=(instance.font_4, 14))
    email_entry.place(x=200, y=450)

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
