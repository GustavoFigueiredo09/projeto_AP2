import os
import customtkinter as ctk
from tkinter import *
from functools import partial
from tkinter import filedialog
from tkinter import ttk, messagebox

class Cactus_Fiscal:
    def __init__(self, root):
        self.window = root  # Atribui a janela ao atributo self.window
        self.window.geometry(self.centralizando_tela())  # Chama o método para centralizar a janela
        
        # Cores
        self.color_1 = "white"
        self.color_2 = "#ffffef"
        self.color_3 = "black"
        self.color_4 = "#67a516"
        self.color_5 = "#ff914d"

        # Fontes
        self.font_1 = "Helvetica"
        self.font_2 = "Times New Roman"
        self.font_3 = "trebuchet ms"

        self.saving_location = ''
        self.PDF_path = []
        self.PDF_List = None

        # Menubar
        self.menubar = Menu(self.window)

        # Menu dinamico
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Menu', menu=edit)
        edit.add_command(label='Inicio', command=self.Home_Page)
        edit.add_separator() # Adiciona o separado no menu dinamico
        edit.add_command(label='Arquivos', command=self.Tela_Arquivos)

        # Adicionando botão 'sobre'
        about = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Sobre', menu=about)
        about.add_command(label='Sobre', command=self.AboutWindow)

        # dando saida no programa
        exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Sair', menu=exit)
        exit.add_command(label='Sair', command=self.Exit)

        # Configurando o menubar
        self.window.config(menu=self.menubar)

        # criando um Frame
        self.frame_1 = Frame(self.window, bg=self.color_2, width=1220, height=686)
        self.frame_1.place(x=0, y=0)
        self.Home_Page()

        # Define o título da janela
        self.window.title('Cactus Fiscal')  

    # Função que centraliza a tela
    def centralizando_tela(self):
        janela_largura = 1220
        janela_altura = 686

        # Obtendo a largura e altura da tela
        tela_largura = self.window.winfo_screenwidth()
        tela_altura = self.window.winfo_screenheight()

        # Calculando a posição para centralizar a janela
        pos_x = (tela_largura // 2) - (janela_largura // 2)
        pos_y = (tela_altura // 2) - (janela_altura // 2)

        # Retornando a string com as dimensões e posição para o método geometry
        return f"{janela_largura}x{janela_altura}+{pos_x}+{pos_y}"

    # Função que exibe a janela "Sobre"
    def AboutWindow(self):
        messagebox.showinfo("Cactus Fiscal", "Cactus Fiscal 25.12.2024\nDeveloped by Tropa 2.0")

    # Função que limpa a tela (remove todos os widgets do frame)
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    # Atualiza o rótulo com o caminho de salvamento
    def Update_Path_Label(self):
        self.path_label.config(text=self.saving_location)

    # Atualiza a página e limpa a tela
    def Update_Rotate_Page(self):
        self.saving_location = ''
        self.ClearScreen()
        self.Home_Page()

    # Função que fecha o programa
    def Exit(self):
        self.window.destroy()

    # Função que exibe a página inicial
    def Home_Page(self):
        self.ClearScreen()        

    # Função que permite selecionar arquivos PDF
    def Select_Arquivo(self):
        selected_files = filedialog.askopenfilenames(initialdir="/",
                                                     title="Selecione um arquivo PDF", filetypes=(("PDF files", "*.pdf*"),))
        if selected_files:
            for path in selected_files:
                self.PDF_List.insert(END, path)

    # Tela "Arquivos"
    def Tela_Arquivos(self):
        self.ClearScreen()

        # Texto selecionar "Selecionar arquivos"
        select_pdf_label = Label(self.frame_1, text="Selecione arquivos",
                                 font=(self.font_2, 15, 'bold'), bg=self.color_2, fg=self.color_3)
        select_pdf_label.place(x=40, y=20)

        # Lista os arquivos selecionados da memoria
        self.PDF_List = Listbox(self.frame_1, font=(self.font_2, 10, 'bold'),
                                bg=self.color_2, fg=self.color_3,
                                selectbackground=self.color_5, selectmode=MULTIPLE)
        self.PDF_List.place(x=40, y=50, width=500, height=440)

        # Barra de rolagem da caixa de arquivos
        scrollbar = Scrollbar(self.PDF_List, orient="vertical")
        scrollbar.config(command=self.PDF_List.yview)
        scrollbar.pack(side="right", fill="y")
        

        # Botão selecionar
        merge_button = Button(self.frame_1, text="Selecionar",
                              font=(self.font_3, 15, 'bold'), bg=self.color_4, fg=self.color_1,
                              width=12, command=self.Select_Arquivo)
        merge_button.place(x=350, y=540)

        # Botão Excluir
        delete_button = Button(self.frame_1, text="Excluir",
                               font=(self.font_3, 15, 'bold'), bg=self.color_4, fg=self.color_1,
                               width=12, command=self.delete_list_items)
        delete_button.place(x=550, y=540)

        # Botão Salvar
        delete_button = Button(self.frame_1, text="Salvar",
                               font=(self.font_3, 15, 'bold'), bg=self.color_4, fg=self.color_1,
                               width=12, command=self.delete_list_items)
        delete_button.place(x=750, y=540)

        # Texto selecionar "Arquivos salvos"
        select_pdf_label2 = Label(self.frame_1, text="Arquivos salvos",
                                 font=(self.font_2, 15, 'bold'), bg=self.color_2, fg=self.color_3)
        select_pdf_label2.place(x=620, y=20)

        # Lista os arquivos já salvos no programa
        self.PDF_List2 = Listbox(self.frame_1, font=(self.font_2, 10, 'bold'),
                                bg=self.color_2, fg=self.color_3,
                                selectbackground=self.color_5, selectmode=MULTIPLE)
        self.PDF_List2.place(x=620, y=50, width=500, height=440)

        # Barra de rolagem da caixa de arquivos
        scrollbar2 = Scrollbar(self.PDF_List2, orient="vertical")
        scrollbar2.config(command=self.PDF_List2.yview)
        scrollbar2.pack(side="right", fill="y")
        
    # Função para excluir itens da lista de arquivos    
    def delete_list_items(self):
        selected_items = self.PDF_List.curselection()
        for index in selected_items[::-1]:
            self.PDF_List.delete(index)

#  Verifica se o script está sendo executado diretamente       
if __name__ == "__main__":
    root = Tk()
    obj = Cactus_Fiscal(root)
    root.mainloop()