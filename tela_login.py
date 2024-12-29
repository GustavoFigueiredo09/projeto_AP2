import tkinter as tk
from tkinter import messagebox

class LoginScreen:
    def __init__(self, root, on_login_success):
        self.window = root
        self.on_login_success = on_login_success
        self.window.geometry(self.centralizando_tela())
        self.window.title("Login - Cactus Fiscal")
        self.window.configure(bg="#ffffef")

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

    def validate_login(self):
        username = self.user_entry.get() # input de usuario
        password = self.pass_entry.get() # input de senha

        # Verificando as credenciais pro acesso
        if username == "admin" and password == "1234":  # Credenciais de login
            messagebox.showinfo("Login bem-sucedido", "Bem-vindo ao Cactus Fiscal!") # Confirmando o login realizado
            self.on_login_success() # chama a função que foi passada comoo parametro 
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos.") # Informando erro na tentativa de login
