from tkinter import *
import tkinter as tk
def Tela_Emissao(instance): 
    instance.ClearScreen()

    # Texto teste
    select_label = Label(instance.frame_1, text="Bem-Vindo a tela de Emissão",
                         font=(instance.font_2, 15, 'bold'), bg=instance.color_2, fg=instance.color_3)
    select_label.place(x=40, y=20)

    def limpar():
        entry_CFOP.delete(0, tk.END)
        entry_produto.delete(0, tk.END)
        entry_valor_produto.delete(0, tk.END)
        entry_tributacao.delete(0, tk.END)
        entry_valor_icm.delete(0, tk.END)
        entry_valor_ipi.delete(0, tk.END)
        entry_valor_pis.delete(0, tk.END)
        entry_descontos.delete(0, tk.END)
        entry_observacoes.delete(0, tk.END)

    #Label e Entrada CFOP
    label_CFOP = Label(instance.frame_1, text="CFOP:",bg=instance.color_2,fg=instance.color_3,
                       font=("Arial", 12))
    label_CFOP.place(x=250,y=120)
    entry_CFOP = Entry(instance.frame_1,font=("Arial",12),width=20,
                       foreground="black")
    entry_CFOP.place(x=310,y=120)
    
    #Label e Entrada Produto/Serviço
    label_produto = Label(instance.frame_1,text="Produto/Serviço:",bg=instance.color_2,fg=instance.color_3,
                          font=("Arial", 12))
    label_produto.place(x=180,y=160)
    entry_produto = Entry(instance.frame_1, font=("Arial", 12), width=20,
                          foreground="black" )
    entry_produto.place(x=310,y=160)


    #Label e Entrada Valor produto/serviço
    label_valor_produto = Label(instance.frame_1,text="Valor produto/serviço:", bg=instance.color_2,fg=instance.color_3,
                                font=("Arial", 12))
    label_valor_produto.place(x= 144,y=200)
    entry_valor_produto = Entry(instance.frame_1, font=("Arial", 12), width=20,
                          foreground="black" )
    entry_valor_produto.place(x=310,y=200)


    #Label e Entrada Tributação ICMS
    label_tributacao = Label(instance.frame_1, text="Tributação ICMS:", bg=instance.color_2,fg=instance.color_3,
                             font=("Arial", 12))
    label_tributacao.place(x=175,y=240)
    entry_tributacao = Entry(instance.frame_1, font=("Arial", 12), width=20,
                          foreground="black" )
    entry_tributacao.place(x=310,y=240)


    #Label e Entrada Valor ICMS
    label_valor_icm = Label(instance.frame_1, text="Valor ICMS:", bg=instance.color_2,fg=instance.color_3,
                            font=("Arial", 12))
    label_valor_icm.place(x=210,y=280)
    entry_valor_icm = Entry(instance.frame_1, font=("Arial", 12), width=20,
                          foreground="black" )
    entry_valor_icm.place(x=310,y=280)


    #Label e Entrada Valor IPI
    label_valor_ipi = Label(instance.frame_1, text="Valor IPI:", bg=instance.color_2,fg=instance.color_3,
                            font=("Arial", 12))
    label_valor_ipi.place(x=230,y=320)
    entry_valor_ipi = Entry(instance.frame_1, font=("Arial", 12), width=20,
                          foreground="black" )
    entry_valor_ipi.place(x=310,y=320)



    #Label e Entrada Valor PIS
    label_valor_pis = Label(instance.frame_1, text="Valor PIS:", bg=instance.color_2,fg=instance.color_3,
                            font=("Arial", 12))
    label_valor_pis.place(x=222, y=360)
    entry_valor_pis = Entry(instance.frame_1, font=("Arial", 12), width=20,
                          foreground="black" )
    entry_valor_pis.place(x=310,y=360)


    #Label e Entrada Descontos
    label_descontos = Label(instance.frame_1, text="Descontos:", bg=instance.color_2,fg=instance.color_3,
                            font=("Arial", 12))
    label_descontos.place(x=215, y=400)
    entry_descontos = Entry(instance.frame_1, font=("Arial", 12), width=20,
                          foreground="black" )
    entry_descontos.place(x=310,y=400)


    #Label e Entrada Observações
    label_observacoes = Label(instance.frame_1, text="Observações:", bg=instance.color_2,fg=instance.color_3,
                              font=("Arial", 12))
    label_observacoes.place(x=196,y=440)
    entry_observacoes = Entry(instance.frame_1, font=("Arial", 12), width=40,
                          foreground="black" )
    entry_observacoes.place(x=310,y=440)

    #Botões/ Emitir / Limpar
    botao_emitir = Button(instance.frame_1, text="Emitir",font=("Arial", 12, 'bold'), background=instance.color_4,
                          foreground="black", width=20)
    botao_emitir.place(x=450,y=540)

    #Botão Limpar
    botao_limpar = Button(instance.frame_1, text="Limpar campos",font=("Arial", 12, 'bold'), background=instance.color_4,
                          foreground="black", width=20,command=limpar)
    botao_limpar.place(x=700,y=540)





    