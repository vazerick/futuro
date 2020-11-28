# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 602)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botaoAdicionar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAdicionar.setObjectName("botaoAdicionar")
        self.horizontalLayout.addWidget(self.botaoAdicionar)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.botaoEditar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEditar.setObjectName("botaoEditar")
        self.horizontalLayout.addWidget(self.botaoEditar)
        self.botaoExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.botaoExcluir.setObjectName("botaoExcluir")
        self.horizontalLayout.addWidget(self.botaoExcluir)
        self.botaoHistorico = QtWidgets.QPushButton(self.centralwidget)
        self.botaoHistorico.setObjectName("botaoHistorico")
        self.horizontalLayout.addWidget(self.botaoHistorico)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelFundo = QtWidgets.QLabel(self.centralwidget)
        self.labelFundo.setObjectName("labelFundo")
        self.horizontalLayout_3.addWidget(self.labelFundo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.labelMes = QtWidgets.QLabel(self.centralwidget)
        self.labelMes.setObjectName("labelMes")
        self.horizontalLayout_3.addWidget(self.labelMes)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.modoLabel = QtWidgets.QLabel(self.centralwidget)
        self.modoLabel.setObjectName("modoLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.modoLabel)
        self.modoComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.modoComboBox.setObjectName("modoComboBox")
        self.modoComboBox.addItem("")
        self.modoComboBox.addItem("")
        self.modoComboBox.addItem("")
        self.modoComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.modoComboBox)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupNome = QtWidgets.QGroupBox(self.centralwidget)
        self.groupNome.setObjectName("groupNome")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupNome)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelNome = QtWidgets.QLabel(self.groupNome)
        self.labelNome.setText("")
        self.labelNome.setObjectName("labelNome")
        self.horizontalLayout_7.addWidget(self.labelNome)
        self.verticalLayout_2.addWidget(self.groupNome)
        self.groupUltimo = QtWidgets.QGroupBox(self.centralwidget)
        self.groupUltimo.setObjectName("groupUltimo")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupUltimo)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelUltimo = QtWidgets.QLabel(self.groupUltimo)
        self.labelUltimo.setText("")
        self.labelUltimo.setObjectName("labelUltimo")
        self.horizontalLayout_8.addWidget(self.labelUltimo)
        self.verticalLayout_2.addWidget(self.groupUltimo)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.botaoEstoque = QtWidgets.QPushButton(self.groupBox)
        self.botaoEstoque.setObjectName("botaoEstoque")
        self.horizontalLayout_4.addWidget(self.botaoEstoque)
        spacerItem5 = QtWidgets.QSpacerItem(157, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem6 = QtWidgets.QSpacerItem(1, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.graficoBarra_2 = PlotBarra(self.centralwidget)
        self.graficoBarra_2.setMinimumSize(QtCore.QSize(300, 220))
        self.graficoBarra_2.setObjectName("graficoBarra_2")
        self.horizontalLayout_13.addWidget(self.graficoBarra_2)
        spacerItem7 = QtWidgets.QSpacerItem(1, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.botaoFeito = QtWidgets.QPushButton(self.centralwidget)
        self.botaoFeito.setObjectName("botaoFeito")
        self.verticalLayout_2.addWidget(self.botaoFeito)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Futuro"))
        self.botaoAdicionar.setText(_translate("MainWindow", "Adicionar novo"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar selecionado"))
        self.botaoExcluir.setText(_translate("MainWindow", "Excluir selecionado"))
        self.botaoHistorico.setText(_translate("MainWindow", "Editar historico"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Gás"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hidratante"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Último"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Frequência"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Previsão"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mensal"))
        self.labelFundo.setText(_translate("MainWindow", "TextLabel"))
        self.labelMes.setText(_translate("MainWindow", "TextLabel"))
        self.modoLabel.setText(_translate("MainWindow", "Cálculo"))
        self.modoComboBox.setItemText(0, _translate("MainWindow", "Simples"))
        self.modoComboBox.setItemText(1, _translate("MainWindow", "Cortar limites"))
        self.modoComboBox.setItemText(2, _translate("MainWindow", "Mediana"))
        self.modoComboBox.setItemText(3, _translate("MainWindow", "Ponderada"))
        self.groupNome.setTitle(_translate("MainWindow", "Nome"))
        self.groupUltimo.setTitle(_translate("MainWindow", "Último"))
        self.groupBox.setTitle(_translate("MainWindow", "Estoque"))
        self.botaoEstoque.setText(_translate("MainWindow", "Atualizar"))
        self.botaoFeito.setText(_translate("MainWindow", "Feito!"))
from ui.plotcanvas import PlotBarra
