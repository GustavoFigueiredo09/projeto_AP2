from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def Tela_Relatorios(instance): 
    instance.ClearScreen()

    # Texto teste
    select_label = Label(instance.frame_1, text="",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    # Combobox - Selecionar Ano
    anos = ["2025", "2024", "2023"]
    label_ano = Label(instance.frame_1, text="Ano", font=("Arial", 20, "bold") , bg="#67a516", fg="black", width=5,height=1)
    label_ano.place(x=50, y=46)
    
    cb_ano = ttk.Combobox(instance.frame_1, values=anos, width=11, font=("Arial", 14),textvariable="Ano")
    cb_ano.set('')
    cb_ano.place(x=30, y=90)

    # Lista de meses
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    # Criar botões um abaixo do outro no canto esquerdo
    for i, mes in enumerate(meses):
        Button(instance.frame_1, text=mes, font=("Arial", 12), 
               bg="white", fg="black", width=15, relief="solid", borderwidth=1,
               command=lambda m=mes: grafico(instance, m)).place(x=30, y=130 + i * 40)
        
    #Frame para o gráfico
    instance.graph_frame = Frame(instance.frame_1, width=400, height=400, bg="white")
    instance.graph_frame.place(x=400, y=130)

def grafico(instance, mes):
    for widget in instance.graph_frame.winfo_children():
        widget.destroy()

    # Criar figura do matplotlib
    fig, ax = plt.subplots(figsize=(5, 4))
    x = 0.5 + np.arange(8)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    ax.set_title(f"Gráfico de {mes}")
    
    # Inserir gráfico no frame_1
    canvas = FigureCanvasTkAgg(fig, master=instance.graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)
    
    # Atualizar a interface para garantir a exibição
    instance.frame_1.update_idletasks()
