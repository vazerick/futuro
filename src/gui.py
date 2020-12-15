import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from ui.entrada import Ui_Dialog as Entrada
from ui.pausa import Ui_Dialog as Pausa
from ui.excluir import Ui_Dialog as Excluir
from ui.férias import Ui_Dialog as Ferias
from ui.historico import Ui_Dialog as Historico
from ui.item import Ui_Dialog as Item
from ui.comparar import Ui_Dialog as Comparar
from ui.planejar import Ui_Dialog as Planejar
from ui.main import Ui_MainWindow as Main

class Gui:

    def __init__(self):
# declarações da interface gráfica

        self.app = QApplication(sys.argv)

# janela principal
        self.wMain = QMainWindow()
        self.ui = Main()
        self.ui.setupUi(self.wMain)        

        self.wMain.setWindowIcon(QIcon("resources/icone.png"))

        self.wAdd = QDialog()
        self.uiAdd = Item()
        self.uiAdd.setupUi(self.wAdd)

        self.wEditar = QDialog()
        self.uiEditar = Item()
        self.uiEditar.setupUi(self.wEditar)

        self.wEntrada = QDialog()
        self.uiEntrada = Entrada()
        self.uiEntrada.setupUi(self.wEntrada)

        self.wPausa = QDialog()
        self.uiPausa = Pausa()
        self.uiPausa.setupUi(self.wPausa)

        self.wExcluir = QDialog()
        self.uiExcluir = Excluir()
        self.uiExcluir.setupUi(self.wExcluir)

        self.wHistorico = QDialog()
        self.uiHistorico = Historico()
        self.uiHistorico.setupUi(self.wHistorico)

        self.wFerias = QDialog()
        self.uiFerias = Ferias()
        self.uiFerias.setupUi(self.wFerias)

        self.wComparar = QDialog()
        self.uiComparar = Comparar()
        self.uiComparar.setupUi(self.wComparar)

        self.wPlanejar = QDialog()
        self.uiPlanejar = Planejar()
        self.uiPlanejar.setupUi(self.wPlanejar)
        self.uiPlanejar.stackedWidget.setCurrentIndex(0)

        for janela in [
            self.wMain,
            self.wAdd,
            self.wEditar,
            self.wEntrada,
            self.wExcluir,
            self.wHistorico,
            self.wFerias,
            self.wComparar,
            self.wPlanejar,
            self.wPausa
        ]:
            janela.setWindowModality(Qt.ApplicationModal)       

# inicializa a janela
        self.wMain.show()

    def ajusta(self):
        self.ui.tableWidget.resizeColumnsToContents()
        tamanho_total = self.ui.tableWidget.width()
        colunas = []
        tamanho_tabela = 0
        for i in range(self.ui.tableWidget.columnCount()):
            colunas.append(self.ui.tableWidget.columnWidth(i))
            tamanho_tabela += self.ui.tableWidget.columnWidth(i)
        sobra = tamanho_total - tamanho_tabela
        extra = int(sobra/len(colunas))-3
        for i in range(0, len(colunas)):
            colunas[i] += extra
            self.ui.tableWidget.setColumnWidth(i, colunas[i])
