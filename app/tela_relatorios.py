from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from tgrafico import iniciar_thread

def Tela_Relatorios(instance): 
    instance.ClearScreen()

    # Texto teste
    select_label = Label(instance.frame_1, text="",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    # Botão atualizar 
    botao_atualizar = Button(instance.frame_1, text="Atualizar", font=("Arial", 14, "bold"),
                             bg="#67a516", fg="white", width=15, height=1,
                             command=lambda: iniciar_thread(instance))
    botao_atualizar.place(x=520,y=570)

    #Frame para o gráfico
    instance.graph_frame = Frame(instance.frame_1, width=800, height=400, bg="white")
    instance.graph_frame.place(relx=0.5, rely=0.45, anchor=CENTER)

    iniciar_thread(instance)