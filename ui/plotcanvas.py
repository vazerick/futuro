import matplotlib.ticker as ticker
import numpy as np
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QDate, QDateTime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotBarra(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=75):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor="#C2D5E8")

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.titulo = "Título"
        self.nome_valores = "Valores"
        self.nome_rotulos = "Rotulos"

    def plot(self, frequencia, historico):
        ax = self.fig.add_subplot(111)
        ax.clear()

        tick = frequencia
        tick = round(tick / 4)
        yticks = [0, tick, tick * 2, tick * 3, tick * 4]

        erro = (1-frequencia/(tick*4))*100
        erro = abs(erro)

        if erro >= 5:
            yticks.append(frequencia)

        count = 4
        while tick * count < max(historico):
            yticks.append(tick * count)
            count += 1
        ax.set_yticks(yticks, minor=False)
        ax.yaxis.grid(True, which='major', linewidth=0.5)


        step = round(len(historico)/10)
        if not step:
            step = 1

        xticks = range(step, len(historico), step)
        ax.set_xticks(xticks, minor=False)

        cores = ["#35978F"] * len(historico)
        cores[-1] = "#003C30"
        barras = ax.bar(range(1, len(historico)+1), historico, color=cores)
        media = frequencia
        ax.set_facecolor("#F5CBF5")
        ax.axhline(y=media, zorder=0, color="#BF812D", linewidth=2.5)

        if len(self.titulo):
            ax.set_title(self.titulo)

        rotulos = []
        if len(historico) > 1:
            rotulos.append(min(historico[0:-1]))
            rotulos.append(max(historico[0:-1]))
        else:
            rotulos.append(historico[0])
        # rotulos.append(historico[-1])
        rotulos = list(set(rotulos))

        for barra, valor in zip(barras, historico):
            if valor in rotulos:
                height = barra.get_height()
                ax.text(barra.get_x() + barra.get_width() / 2, height - 1, valor,
                        ha='center', va='bottom')
                rotulos.remove(valor)
        barra = barras[-1]
        valor = historico[-1]
        height = barra.get_height()
        ax.text(barra.get_x() + barra.get_width() / 2, height - 1, valor,
                ha='center', va='bottom')

        self.draw()

    def limpa(self):
        ax = self.fig.add_subplot(111)
        ax.clear()
        self.draw()
