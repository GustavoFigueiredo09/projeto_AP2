from tkinter import *

def Tela_Inicio(instance):
    instance.ClearScreen()

    select_label = Label(instance.frame_1, text="Testando tela de inicio...",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)