from tkinter import *
import tkinter as tk
from tkinter import ttk

def Tela_Inicio(root):
    # Limpando a tela atual
    for widget in root.winfo_children():
        widget.destroy()
    
    # Configurando a tela de início
    frame_1 = Frame(root, bg="white", width=310, height=300, relief="flat")
    frame_1.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    # Adicionando um exemplo de interface
    select_label = Label(frame_1, text=" tela de início...",
                         font=('Arial', 15, 'bold'), bg="white", fg="black")
    select_label.place(x=40, y=20)
