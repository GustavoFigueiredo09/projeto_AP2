import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from backend.database.models.lancamentos import Lancamento

def atualizar_grafico(instance):
    # Limpa o gráfico anterior, se existir
    for widget in instance.graph_frame.winfo_children():
        widget.destroy()

    lancamentos = Lancamento()
    # Dados de cada categoria (supondo que cada método retorne uma lista de tuplas)

    saldo = lancamentos.busca_saldo()
    print(saldo)
    dados = { 
        "Entradas": lancamentos.busca_soma_entradas(),
        "Saidas": lancamentos.busca_soma_saidas(), 
        "Impostos": lancamentos.busca_soma_impostos()
    }

    print(dados['Entradas'])
    # Paleta de cores para cada categoria
    cores = ["#86cf05", "#C70039", "#FFC300"]

    # Criar figura
    fig, ax = plt.subplots(figsize=(10, 4))

    # Loop para plotar cada categoria
    for (categoria, valores), cor in zip(dados.items(), cores):

        # Converte as datas e extrai os valores
        datas = [datetime.strptime(mes + "-01", "%Y-%m-%d") for mes, _ in valores]
        montantes = [valor for _, valor in valores]
        ax.plot(datas, montantes, marker="o", linestyle=":", label=categoria, color=cor, markersize=4, linewidth=1.5)
    
    datas_ganhos = [datetime.strptime(mes + "-01", "%Y-%m-%d") for mes, _ in saldo]
    montantes_ganhos = [valor for _, valor in saldo]
    ax.plot(datas_ganhos, montantes_ganhos, marker="o", linestyle="-", label="Saldo", color="#0ca8fa", markersize=5, linewidth=1.7)

    # Configurações do gráfico
    ax.set_xlabel("Meses")
    ax.set_ylabel("Valores (R$)")
    ax.set_title("Comparação Mensal: Ganhos, Entradas, Saídas e Impostos")
    ax.legend()
    ax.grid(True, linestyle='--', linewidth=0.5)

    # Formatando datas no eixo X
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    fig.autofmt_xdate()

    # Integrar o gráfico no frame do Tkinter
    canvas = FigureCanvasTkAgg(fig, master=instance.graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Fechar a figura para não acumular memória
    plt.close(fig)

def iniciar_thread(instance):
    instance.graph_frame.after(100, atualizar_grafico, instance)
