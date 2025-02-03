from tkinter import *
import tkinter as tk
from tkinter import ttk

def Tela_Contas(instance): 
    instance.ClearScreen()

    # Texto teste
    select_label = Label(instance.frame_1, text="Bem-Vindo a tela Bancos",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    