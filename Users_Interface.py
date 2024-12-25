import os
import customtkinter as ctk
from tkinter import *
from functools import partial
from tkinter import filedialog
from tkinter import ttk, messagebox
from tela_arquivos import Tela_Arquivos
from tela_relatorios import Tela_Relatorios
from tela_inicio import Tela_Inicio
from tela_cadastros import Tela_Cadastros
from tela_emissao import Tela_Emissao
from tela_lancamentos import Tela_Lancamentos

class Cactus_Fiscal:
    def __init__(self, root):
        self.window = root
        self.window.geometry(self.centralizando_tela())

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
        self.Arquivo_Lista = None

        # Menubar
        self.menubar = Menu(self.window)

        # Menu dinamico
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Menu', menu=edit)
        edit.add_command(label='Inicio', command=lambda: Tela_Inicio(self))
        edit.add_separator()
        edit.add_command(label='Lanaçamentos', command=lambda: Tela_Lancamentos(self))
        edit.add_separator()  
        edit.add_command(label='Relatorios', command=lambda: Tela_Relatorios(self))
        edit.add_separator()
        edit.add_command(label='Cadastros', command=lambda: Tela_Cadastros(self))
        edit.add_separator()
        edit.add_command(label='Arquivos', command=lambda: Tela_Arquivos(self))
        edit.add_separator()
        edit.add_command(label='Emissão', command=lambda: Tela_Emissao(self))

        # Adicionando botão 'sobre'
        about = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Sobre', menu=about)
        about.add_command(label='Sobre', command=self.AboutWindow)

        # Saída
        exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Sair', menu=exit)
        exit.add_command(label='Sair', command=self.Exit)

        # Configuração do menubar
        self.window.config(menu=self.menubar)

        # Criando um Frame
        self.frame_1 = Frame(self.window, bg=self.color_2, width=1220, height=686)
        self.frame_1.place(x=0, y=0)
        self.Home_Page()

        self.window.title('Cactus Fiscal')

    def centralizando_tela(self):
        janela_largura = 1220
        janela_altura = 686
        tela_largura = self.window.winfo_screenwidth()
        tela_altura = self.window.winfo_screenheight()
        pos_x = (tela_largura // 2) - (janela_largura // 2)
        pos_y = (tela_altura // 2) - (janela_altura // 2)
        return f"{janela_largura}x{janela_altura}+{pos_x}+{pos_y}"

    def AboutWindow(self):
        messagebox.showinfo("Cactus Fiscal", "Cactus Fiscal 25.12.2024\nDeveloped by Tropa 2.0")

    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    def Exit(self):
        self.window.destroy()

    def Home_Page(self):
        self.ClearScreen()

    def Select_Arquivo(self):
        selected_files = filedialog.askopenfilenames(initialdir="/",
                                                     title="Selecione um arquivo PDF", filetypes=(("PDF files", "*.pdf*"),))
        if selected_files:
            for path in selected_files:
                self.Arquivo_Lista.insert(END, path)

    def delete_list_items(self):
        selected_items = self.Arquivo_Lista.curselection()
        for index in selected_items[::-1]:
            self.Arquivo_Lista.delete(index)

if __name__ == "__main__":
    root = Tk()
    obj = Cactus_Fiscal(root)
    root.mainloop()
