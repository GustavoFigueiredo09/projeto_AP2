import os
import tkinter as tk
from tkinter import filedialog, messagebox
from functools import partial
import customtkinter as ctk # Customização da interface
from tela_login import LoginScreen  # Importando a tela de login
from tela_inicio import Tela_Inicio # Importando a tela Inicio
from tela_lancamentos import Tela_Lancamentos # Importando a tela Lançamentos
from tela_relatorios import Tela_Relatorios # Importando a tela Relatorios
from tela_cadastros import Tela_Cadastros # Importando a tela Cadastros
from tela_arquivos import Tela_Arquivos # Importando a tela Arquivos
from tela_emissao import Tela_Emissao # Importando a tela Emissão
from cadastro_usuario import Cadastro_Usuario # Importa a tela de cadastro de usuários
from cadastro_terceiros import Cadastro_Terceiros # Importa a tela de cadastro de terceiros

class Cactus_Fiscal:
    def __init__(self, root):
        self.window = root
        self.window.geometry(self.centralizando_tela())  # Ajustando o tamanho da janela inicial
        self.window.resizable(True, True)  # Permitindo redimensionamento da janela

        # Cores
        self.color_1 = "white"  # Branco
        self.color_2 = "#ffffef"  # Bege claro
        self.color_3 = "black"  # Preto
        self.color_4 = "#67a516"  # Verde Claro
        self.color_5 = "#ff914d"  # Laranja

        # Fontes
        self.font_1 = "Helvetica"
        self.font_2 = "Times New Roman"
        self.font_3 = "trebuchet ms"
        self.font_4 = "Arial"

        self.saving_location = ''
        self.PDF_path = []
        self.Arquivo_Lista = None

        # Menubar
        self.menubar = tk.Menu(self.window)

        # Menu principal
        edit = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Menu', menu=edit)
        edit.add_command(label='Inicio', command=self.Home_Page)
        edit.add_separator()
        edit.add_command(label='Lançamentos', command=lambda: Tela_Lancamentos(self))
        edit.add_separator()
        edit.add_command(label='Relatórios', command=lambda: Tela_Relatorios(self))
        edit.add_separator()
        
        # Submenu de cadastros
        cadastros_menu = tk.Menu(edit, tearoff=0)
        cadastros_menu.add_command(label='Cadastro de Usuários', command=lambda: Cadastro_Usuario(self))
        cadastros_menu.add_command(label='Cadastro de Terceiros', command=lambda: Cadastro_Terceiros(self))
        edit.add_cascade(label='Cadastros', menu=cadastros_menu)

        edit.add_separator()
        edit.add_command(label='Arquivos', command=lambda: Tela_Arquivos(self))
        edit.add_separator()
        edit.add_command(label='Emissão', command=lambda: Tela_Emissao(self))

        # Sobre
        about = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Sobre', menu=about)
        about.add_command(label='Sobre', command=self.AboutWindow)

        # Saída
        exit = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Sair', menu=exit)
        exit.add_command(label='Sair', command=self.Exit)

        # Configuração do menubar
        self.window.config(menu=self.menubar)

        # Criando um Frame
        self.frame_1 = tk.Frame(self.window, bg=self.color_2)
        self.frame_1.pack(fill="both", expand=True)  # Fazendo o frame preencher a janela

        self.Home_Page()  # Exibindo a tela inicial ao iniciar

        self.window.title('Cactus Fiscal')

    # Centralizando a janela
    def centralizando_tela(self):
        janela_largura = 1220
        janela_altura = 686
        tela_largura = self.window.winfo_screenwidth()
        tela_altura = self.window.winfo_screenheight()
        pos_x = (tela_largura // 2) - (janela_largura // 2)
        pos_y = (tela_altura // 2) - (janela_altura // 2)
        return f"{janela_largura}x{janela_altura}+{pos_x}+{pos_y}"

    # Exibindo a janela sobre com as informações do projeto
    def AboutWindow(self):
        messagebox.showinfo("Cactus Fiscal", "Cactus Fiscal\nDeveloped by Tropa 2.0")

    # Limpando a tala
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    # Saindo do sistema após clicar no botão "sair"
    def Exit(self):
        self.window.destroy()

    # Exibindo a tela inicial
    def Home_Page(self):
        self.ClearScreen()  # Limpando a tela antes de mostrar a Home

        # Elementos da tela inico
        welcome_label = tk.Label(self.frame_1, text="Bem-vindo à Tela Inicial", font=(self.font_1, 20), bg=self.color_2)
        welcome_label.pack(pady=50)

    # Selecionando arquivos da memória
    def Select_Arquivo(self):
        selected_files = filedialog.askopenfilenames(initialdir="/",
                                                     title="Selecione um arquivo PDF", filetypes=(("PDF files", "*.pdf*"),))
        if selected_files:
            for path in selected_files:
                self.Arquivo_Lista.insert(tk.END, path) # Insere o caminho dos arquivos na caixa de arquivos

    # Exclui itens da lista de arquivos selecionados
    def delete_list_items(self):
        selected_items = self.Arquivo_Lista.curselection()
        for index in selected_items[::-1]:
            self.Arquivo_Lista.delete(index)

# Iniciando a aplicação após o login
def start_main_app():
    root.destroy()  # Fecha a tela de login
    main_root = tk.Tk()
    app = Cactus_Fiscal(main_root)
    main_root.mainloop() # Loop pra interface após o login

if __name__ == "__main__":
    # Tela de login
    root = tk.Tk() # Janela pra tela de login
    login = LoginScreen(root, on_login_success=start_main_app) # Criando a tela de login
    root.mainloop() # Loop pra tela de login
