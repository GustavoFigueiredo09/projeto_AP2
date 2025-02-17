from tkinter import *
from tkinter import filedialog
from session import SessaoUsuario
from backend.database.models.arquivos import Arquivo
import os

def Tela_Arquivos(instance):
    instance.ClearScreen()

    # Chamando as informações do usuário
    usuario_atual = SessaoUsuario().get_usuario()
    if usuario_atual:
        print(f"Usuário logado: {usuario_atual['nome']}")
    
    # Caixa para mostrar arquivos selecionados
    instance.arquivo_crud = Arquivo()
    instance.usuario_login = usuario_atual['login'] if usuario_atual else None

    select_label = Label(instance.frame_1, text="Selecione arquivos",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    instance.Arquivo_Lista = Listbox(instance.frame_1, font=(instance.font_2, 10, 'bold'),
                                     bg=instance.color_2, fg=instance.color_3,
                                     selectbackground=instance.color_5, selectmode=MULTIPLE)
    instance.Arquivo_Lista.place(x=40, y=50, width=500, height=440)

    scrollbar = Scrollbar(instance.Arquivo_Lista, orient="vertical")
    scrollbar.config(command=instance.Arquivo_Lista.yview)
    scrollbar.pack(side="right", fill="y")

    # Botão selecionar
    merge_button = Button(instance.frame_1, text="Selecionar",
                          font=(instance.font_3, 15, 'bold'), bg=instance.color_4, fg=instance.color_1,
                          width=12, command=lambda: Select_Arquivo(instance))
    merge_button.place(x=350, y=540)

    # Botão Excluir
    delete_button = Button(instance.frame_1, text="Excluir",
                           font=(instance.font_3, 15, 'bold'), bg=instance.color_4, fg=instance.color_1,
                           width=12, command=lambda: Delete_Arquivo(instance))
    delete_button.place(x=550, y=540)

    # Botão salvar
    save_button = Button(instance.frame_1, text="Salvar",
                         font=(instance.font_3, 15, 'bold'), bg=instance.color_4, fg=instance.color_1,
                         width=12, command=lambda: Save_Arquivo(instance))
    save_button.place(x=750, y=540)

    # Caixa para mostrar arquivos salvos
    select_label2 = Label(instance.frame_1, text="Arquivos salvos",
                          font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label2.place(x=620, y=20)

    instance.Arquivo_Lista2 = Listbox(instance.frame_1, font=(instance.font_2, 10, 'bold'),
                                      bg=instance.color_2, fg=instance.color_3,
                                      selectbackground=instance.color_5, selectmode=MULTIPLE)
    instance.Arquivo_Lista2.place(x=620, y=50, width=500, height=440)

    scrollbar2 = Scrollbar(instance.Arquivo_Lista2, orient="vertical")
    scrollbar2.config(command=instance.Arquivo_Lista2.yview)
    scrollbar2.pack(side="right", fill="y")

    Load_Saved_Arquivos(instance)

# Selecionando arquivos da memória
def Select_Arquivo(instance):
    selected_files = filedialog.askopenfilenames(initialdir="/", title="Selecione um arquivo PDF", 
                                                 filetypes=(("PDF files", "*.pdf*"),))
    for path in selected_files:
        instance.Arquivo_Lista.insert(END, path)

# Salvando arquivos no banco em forma .blob
def Save_Arquivo(instance):
    arquivos_selecionados = instance.Arquivo_Lista.get(0, END)
    for caminho in arquivos_selecionados:
        nome_arquivo = os.path.basename(caminho)
        with open(caminho, "rb") as file:
            arquivo_blob = file.read()
        instance.arquivo_crud.create(instance.usuario_login, nome_arquivo, arquivo_blob)
    instance.Arquivo_Lista.delete(0, END)
    Load_Saved_Arquivos(instance)

# Atualiza caixa com arquivos do usuário 
def Load_Saved_Arquivos(instance):
    instance.Arquivo_Lista2.delete(0, END)
    arquivos = instance.arquivo_crud.busca_nome_do_arquivo(instance.usuario_login)
    for arquivo in arquivos:
        instance.Arquivo_Lista2.insert(END, arquivo['nome_arquivo'])

# Deletando arquivos 
def Delete_Arquivo(instance):
    # Exclui da lista de arquivos salvos
    selecionados = instance.Arquivo_Lista2.curselection()
    for index in selecionados[::-1]:
        nome_arquivo = instance.Arquivo_Lista2.get(index)
        instance.arquivo_crud.excluir_arquivo(nome_arquivo)
        instance.Arquivo_Lista2.delete(index)
    
    # Exclui da lista de arquivos selecionados
    arquivos_selecionados = instance.Arquivo_Lista.curselection()
    for index in arquivos_selecionados[::-1]:
        instance.Arquivo_Lista.delete(index)
    
    # Atualizando a lista de arquivos salvos após a exclusão
    Load_Saved_Arquivos(instance)