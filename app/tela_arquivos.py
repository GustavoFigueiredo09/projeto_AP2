from tkinter import *

def Tela_Arquivos(instance):
    # Limpa a tela
    instance.ClearScreen()

    # Texto selecionar "Selecionar arquivos"
    select_label = Label(instance.frame_1, text="Selecione arquivos",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    # Lista os arquivos selecionados da memória
    instance.Arquivo_Lista = Listbox(instance.frame_1, font=(instance.font_2, 10, 'bold'),
                                     bg=instance.color_2, fg=instance.color_3,
                                     selectbackground=instance.color_5, selectmode=MULTIPLE)
    instance.Arquivo_Lista.place(x=40, y=50, width=500, height=440)

    # Barra de rolagem da caixa de arquivos
    scrollbar = Scrollbar(instance.Arquivo_Lista, orient="vertical")
    scrollbar.config(command=instance.Arquivo_Lista.yview)
    scrollbar.pack(side="right", fill="y")

    # Botão selecionar
    merge_button = Button(instance.frame_1, text="Selecionar",
                          font=(instance.font_3, 15, 'bold'), bg=instance.color_4, fg=instance.color_1,
                          width=12, command=instance.Select_Arquivo)
    merge_button.place(x=350, y=540)

    # Botão Excluir
    delete_button = Button(instance.frame_1, text="Excluir",
                           font=(instance.font_3, 15, 'bold'), bg=instance.color_4, fg=instance.color_1,
                           width=12, command=instance.delete_list_items)
    delete_button.place(x=550, y=540)

    # Botão Salvar
    save_button = Button(instance.frame_1, text="Salvar",
                         font=(instance.font_3, 15, 'bold'), bg=instance.color_4, fg=instance.color_1,
                         width=12, command=instance.delete_list_items)
    save_button.place(x=750, y=540)

    # Texto selecionar "Arquivos salvos"
    select_label2 = Label(instance.frame_1, text="Arquivos salvos",
                          font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label2.place(x=620, y=20)

    # Lista os arquivos já salvos no programa
    instance.Arquivo_Lista2 = Listbox(instance.frame_1, font=(instance.font_2, 10, 'bold'),
                                      bg=instance.color_2, fg=instance.color_3,
                                      selectbackground=instance.color_5, selectmode=MULTIPLE)
    instance.Arquivo_Lista2.place(x=620, y=50, width=500, height=440)

    # Barra de rolagem da caixa de arquivos
    scrollbar2 = Scrollbar(instance.Arquivo_Lista2, orient="vertical")
    scrollbar2.config(command=instance.Arquivo_Lista2.yview)
    scrollbar2.pack(side="right", fill="y")
