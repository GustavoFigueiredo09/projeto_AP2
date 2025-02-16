import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def atualizar_grafico(instance):
    

    # Limpa o gráfico anterior, se existir
    for widget in instance.graph_frame.winfo_children():
        widget.destroy()

    # Criar figura do Matplotlib
    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.arange(1, 13)  # Meses de 1 a 12
    y = np.random.randint(10, 100, size=12) #Random vai simular possíveis valores (necessita de conexão com bd)
    ax.plot(x, y, marker="o", linestyle="-", label="Ganhos")
    
    ax.set_xlabel("Meses")
    ax.set_ylabel("Ganhos")
    ax.set_title("Gráfico Mensal")
    ax.legend()
    ax.grid(True)

    #Criar o Canvas e adicionar ao frame
    canvas = FigureCanvasTkAgg(fig, master=instance.graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def iniciar_thread(instance):
    instance.graph_frame.after(100, atualizar_grafico, instance)  #Executa sem thread separada
