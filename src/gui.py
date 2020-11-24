import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from ui.entrada import Ui_Dialog as Entrada
from ui.excluir import Ui_Dialog as Excluir
from ui.historico import Ui_Dialog as Historico
from ui.item import Ui_Dialog as Item
from ui.main import Ui_MainWindow as Main


# import do PyQt5
# import das janelas

class Gui:

    def __init__(self):
# declarações da interface gráfica
        print("Gerando a interface gráfica")

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

        self.wExcluir = QDialog()
        self.uiExcluir = Excluir()
        self.uiExcluir.setupUi(self.wExcluir)

        self.wHistorico = QDialog()
        self.uiHistorico = Historico()
        self.uiHistorico.setupUi(self.wHistorico)

        for janela in [
            self.wMain,
            self.wAdd,
            self.wEditar,
            self.wEntrada,
            self.wExcluir,
            self.wHistorico,
        ]:
            janela.setWindowModality(Qt.ApplicationModal)       

# inicializa a janela
        self.wMain.show()
