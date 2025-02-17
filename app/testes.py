import tkinter as tk
from tkinter import ttk

# Criando a janela principal
root = tk.Tk()
root.title("Lista Suspensa com Combobox")
root.geometry("300x200")

# Função para capturar o valor selecionado
def selecionar():
    valor_selecionado = combobox.get()
    print(f"Selecionado: {valor_selecionado}")

# Lista de opções
opcoes = ["Pago", "Pendente", "Indevido", "Aguardando", "Desconhecida"]

# Criando a Combobox
combobox = ttk.Combobox(root, values=opcoes)
combobox.set("Selecione uma opção")  # Define um valor padrão ou inicial
combobox.pack(pady=20)

# Botão para confirmar a seleção
botao = tk.Button(root, text="Confirmar", command=selecionar)
botao.pack()

# Inicia o loop principal
root.mainloop()