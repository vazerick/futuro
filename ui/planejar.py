# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'planejar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(822, 618)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.selecionarPage = QtWidgets.QWidget()
        self.selecionarPage.setObjectName("selecionarPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.selecionarPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.selecionarPage)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.treeWidget = QtWidgets.QTreeWidget(self.selecionarPage)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.botaoProximo1 = QtWidgets.QPushButton(self.selecionarPage)
        self.botaoProximo1.setObjectName("botaoProximo1")
        self.horizontalLayout.addWidget(self.botaoProximo1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.selecionarPage)
        self.estoquePage = QtWidgets.QWidget()
        self.estoquePage.setObjectName("estoquePage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.estoquePage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.estoquePage)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.tabelaEstoque = QtWidgets.QTableWidget(self.estoquePage)
        self.tabelaEstoque.setObjectName("tabelaEstoque")
        self.tabelaEstoque.setColumnCount(5)
        self.tabelaEstoque.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaEstoque.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaEstoque.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaEstoque.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaEstoque.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaEstoque.setHorizontalHeaderItem(4, item)
        self.verticalLayout_3.addWidget(self.tabelaEstoque)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.botaoAnterior1 = QtWidgets.QPushButton(self.estoquePage)
        self.botaoAnterior1.setObjectName("botaoAnterior1")
        self.horizontalLayout_2.addWidget(self.botaoAnterior1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.botaoProximo2 = QtWidgets.QPushButton(self.estoquePage)
        self.botaoProximo2.setObjectName("botaoProximo2")
        self.horizontalLayout_2.addWidget(self.botaoProximo2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.estoquePage)
        self.planejamentoPage = QtWidgets.QWidget()
        self.planejamentoPage.setObjectName("planejamentoPage")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.planejamentoPage)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.planejamentoPage)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabelaPlanejamento = QtWidgets.QTableWidget(self.planejamentoPage)
        self.tabelaPlanejamento.setObjectName("tabelaPlanejamento")
        self.tabelaPlanejamento.setColumnCount(6)
        self.tabelaPlanejamento.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPlanejamento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPlanejamento.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPlanejamento.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPlanejamento.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPlanejamento.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPlanejamento.setHorizontalHeaderItem(5, item)
        self.horizontalLayout_4.addWidget(self.tabelaPlanejamento)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.planejamentoPage)
        self.groupBox.setMinimumSize(QtCore.QSize(220, 0))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelPrimeiro = QtWidgets.QLabel(self.groupBox)
        self.labelPrimeiro.setObjectName("labelPrimeiro")
        self.verticalLayout_5.addWidget(self.labelPrimeiro)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.planejamentoPage)
        self.groupBox_2.setMinimumSize(QtCore.QSize(220, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelUltimo = QtWidgets.QLabel(self.groupBox_2)
        self.labelUltimo.setObjectName("labelUltimo")
        self.verticalLayout_4.addWidget(self.labelUltimo)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.planejamentoPage)
        self.groupBox_3.setMinimumSize(QtCore.QSize(220, 0))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelIntervalo = QtWidgets.QLabel(self.groupBox_3)
        self.labelIntervalo.setObjectName("labelIntervalo")
        self.verticalLayout_6.addWidget(self.labelIntervalo)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.botaoAnterior2 = QtWidgets.QPushButton(self.planejamentoPage)
        self.botaoAnterior2.setObjectName("botaoAnterior2")
        self.horizontalLayout_3.addWidget(self.botaoAnterior2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.planejamentoPage)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Item"))
        self.label.setText(_translate("Dialog", "Selecione os itens para comprar juntos"))
        self.botaoProximo1.setText(_translate("Dialog", "Próximo"))
        self.label_2.setText(_translate("Dialog", "Estoque"))
        item = self.tabelaEstoque.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nome"))
        item = self.tabelaEstoque.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Quantia"))
        item = self.tabelaEstoque.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Unidades"))
        item = self.tabelaEstoque.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Estoque"))
        self.botaoAnterior1.setText(_translate("Dialog", "Anterior"))
        self.botaoProximo2.setText(_translate("Dialog", "Próximo"))
        self.label_3.setText(_translate("Dialog", "Planejamento"))
        item = self.tabelaPlanejamento.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nome"))
        item = self.tabelaPlanejamento.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Quantia"))
        item = self.tabelaPlanejamento.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Unidades"))
        item = self.tabelaPlanejamento.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Comprar"))
        item = self.tabelaPlanejamento.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Previsão"))
        self.groupBox.setTitle(_translate("Dialog", "Primeiro"))
        self.labelPrimeiro.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_2.setTitle(_translate("Dialog", "Último"))
        self.labelUltimo.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_3.setTitle(_translate("Dialog", "Intervalo"))
        self.labelIntervalo.setText(_translate("Dialog", "TextLabel"))
        self.botaoAnterior2.setText(_translate("Dialog", "Anterior"))