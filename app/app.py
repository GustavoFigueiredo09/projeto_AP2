import tkinter as tk
from tkinter import filedialog, messagebox
from functools import partial
import customtkinter as ctk  # Customização da interface
from PIL import Image, ImageTk  # Para carregar e exibir a imagem
from tela_login import LoginScreen  # Importando a tela de login
from tela_lancamentos import Tela_Lancamentos  # Importando a tela Lançamentos
from tela_relatorios import Tela_Relatorios  # Importando a tela RelatoriosS
from tela_arquivos import Tela_Arquivos  # Importando a tela Arquivos
from cadastro_usuario import Cadastro_Usuario  # Importa a tela de cadastro de usuários
from cadastro_terceiros import Cadastro_Terceiros  # Importa a tela de cadastro de terceiros
from session import SessaoUsuario

class Cactus_Fiscal:
    def __init__(self, root):
        usuario_atual = SessaoUsuario()
        dados_usuario = usuario_atual.get_usuario()

        self.window = root
        self.window.geometry(self.centralizando_tela())  
        self.window.resizable(True, True)

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
        
        # Submenu de cadastros
        if dados_usuario['adm'] == 1:
            cadastros_menu = tk.Menu(edit, tearoff=0)
            edit.add_separator()
            cadastros_menu.add_command(label='Cadastro de Usuários', command=lambda: Cadastro_Usuario(self))
            cadastros_menu.add_command(label='Cadastro de Terceiros', command=lambda: Cadastro_Terceiros(self))
            edit.add_cascade(label='Cadastros', menu=cadastros_menu)
        
        edit.add_separator()
        edit.add_command(label='Arquivos', command=lambda: Tela_Arquivos(self))
        
        # Sobre dentro do menu principal
        edit.add_separator()
        edit.add_command(label='Sobre', command=self.AboutWindow)
        
        # Configuração do menubar
        self.menubar.add_command(label='Sair', command=self.Exit)
        self.window.config(menu=self.menubar)

        # Criando um Frame
        self.frame_1 = tk.Frame(self.window, bg=self.color_2)
        self.frame_1.pack(fill="both", expand=True)

        self.Home_Page() 

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

    # Limpando a tela
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    # Saindo do sistema após clicar no botão "sair" com confirmação
    def Exit(self):
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja sair?"):
            self.window.destroy()

    # Exibindo a tela inicial com imagem
    def Home_Page(self):
        self.ClearScreen()

        image_path = "images/image_inicio.jpg" 
        img = Image.open(image_path)
        img = img.resize((1220, 686))
        img_tk = ImageTk.PhotoImage(img)

        img_label = tk.Label(self.frame_1, image=img_tk, bg=self.color_2)
        img_label.image = img_tk
        img_label.pack(pady=1)

# Iniciando a aplicação após o login
def start_main_app():
    root.destroy()  # Fecha a tela de login
    main_root = tk.Tk()
    app = Cactus_Fiscal(main_root)
    main_root.mainloop()

if __name__ == "__main__":
    # Tela de login
    root = tk.Tk()  # Janela pra tela de login
    login = LoginScreen(root, on_login_success=start_main_app)  # Criando a tela de login
    root.mainloop()