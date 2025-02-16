import time
from tkinter import messagebox
import tkinter as tk
from backend.database.models.usuarios import Usuario
from session import SessaoUsuario

class LoginScreen:
    def __init__(self, root, on_login_success):
        self.window = root
        self.on_login_success = on_login_success
        self.window.geometry(self.centralizando_tela())
        self.window.title("Login - Cactus Fiscal")
        self.window.configure(bg="#ffffef")

        self.tentativas = 0  # Contador de tentativas
        self.usuario_db = Usuario()

        # Frame principal
        self.frame_1 = tk.Frame(self.window, bg="#ffffef", width=1220, height=686)
        self.frame_1.place(x=0, y=0)

        # Título da tela de login
        self.title_label = tk.Label(self.frame_1, text="Cactus Fiscal", font=("Times New Roman", 28, 'bold'),
                                    bg="#ffffef", fg="black")
        self.title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Campo "usuário"
        self.user_label = tk.Label(self.frame_1, text="Usuário:", font=("Helvetica", 16), bg="#ffffef", fg="black")
        self.user_label.place(relx=0.35, rely=0.4, anchor=tk.E)
        self.user_entry = tk.Entry(self.frame_1, font=("Helvetica", 16), width=30)
        self.user_entry.place(relx=0.36, rely=0.4, anchor=tk.W)

        # Campo "senha"
        self.pass_label = tk.Label(self.frame_1, text="Senha:", font=("Helvetica", 16), bg="#ffffef", fg="black")
        self.pass_label.place(relx=0.35, rely=0.5, anchor=tk.E)
        self.pass_entry = tk.Entry(self.frame_1, font=("Helvetica", 16), width=30, show="*")
        self.pass_entry.place(relx=0.36, rely=0.5, anchor=tk.W)

        # Botão "login"
        self.login_button = tk.Button(self.frame_1, text="Entrar", font=("Helvetica", 16), bg="#67a516", fg="white",
                                      command=self.validate_login)
        self.login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # Centralizando a tela
    def centralizando_tela(self):
        janela_largura = 1220
        janela_altura = 686
        tela_largura = self.window.winfo_screenwidth()
        tela_altura = self.window.winfo_screenheight()
        pos_x = (tela_largura // 2) - (janela_largura // 2)
        pos_y = (tela_altura // 2) - (janela_altura // 2)
        return f"{janela_largura}x{janela_altura}+{pos_x}+{pos_y}"

    # Temporizador após tentativas e falhas
    def temporizador(self, segundos):
        for i in range(segundos, 0, -1):
            self.user_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)
            self.login_button.config(state=tk.DISABLED, text=f"Tente novamente em {i}s")
            self.window.update()
            time.sleep(1)
        self.login_button.config(state=tk.NORMAL, text="Entrar")

    # Validação de login com tentativas
    def validate_login(self):
        username = self.user_entry.get() # Pega o nome de usuário
        password = self.pass_entry.get() # Pega a senha

        if not username or not password:
            messagebox.showwarning("Erro", "Usuário e senha são obrigatórios.")
            return

        resultado = self.usuario_db.buscar_login_e_senha(username, password)

        # Login bem-sucedido
        if resultado:  
            usuario_info = resultado[0]  # Pega os dados do usuário autenticado
            SessaoUsuario().set_usuario(usuario_info)  # Armazena os dados em session.py
            
            cargo = usuario_info.get('admin', 0)
            if cargo == 1:
                messagebox.showinfo("Login", f"Bem-vindo Administrador {username}!")
            else:
                messagebox.showinfo("Login", f"Bem-vindo {username}!")
            
            self.on_login_success()
        
        # Login falhou
        else:  
            self.tentativas += 1
            if self.tentativas >= 3:
                messagebox.showerror("Erro", "Número máximo de tentativas. Aguarde 5 segundos.")
                self.temporizador(5)
                self.tentativas = 0
            else:
                messagebox.showerror("Erro", f"Usuário ou senha incorretos. Tentativa {self.tentativas}/3.")
