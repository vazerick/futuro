# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comparar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(378, 236)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.quantiaLabel = QtWidgets.QLabel(self.groupBox)
        self.quantiaLabel.setObjectName("quantiaLabel")
        self.horizontalLayout_3.addWidget(self.quantiaLabel)
        self.quantiaSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.quantiaSpinBox.setMaximum(999)
        self.quantiaSpinBox.setObjectName("quantiaSpinBox")
        self.horizontalLayout_3.addWidget(self.quantiaSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.unidadeLabel = QtWidgets.QLabel(self.groupBox)
        self.unidadeLabel.setObjectName("unidadeLabel")
        self.horizontalLayout_2.addWidget(self.unidadeLabel)
        self.unidadeDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.unidadeDoubleSpinBox.setMaximum(9999.99)
        self.unidadeDoubleSpinBox.setObjectName("unidadeDoubleSpinBox")
        self.horizontalLayout_2.addWidget(self.unidadeDoubleSpinBox)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.valorLabel = QtWidgets.QLabel(self.groupBox)
        self.valorLabel.setObjectName("valorLabel")
        self.horizontalLayout.addWidget(self.valorLabel)
        self.valorDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.valorDoubleSpinBox.setMaximum(999.99)
        self.valorDoubleSpinBox.setObjectName("valorDoubleSpinBox")
        self.horizontalLayout.addWidget(self.valorDoubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.quantiaLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.quantiaLabel_2.setObjectName("quantiaLabel_2")
        self.horizontalLayout_4.addWidget(self.quantiaLabel_2)
        self.quantiaNovoSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.quantiaNovoSpinBox.setMaximum(999)
        self.quantiaNovoSpinBox.setObjectName("quantiaNovoSpinBox")
        self.horizontalLayout_4.addWidget(self.quantiaNovoSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.unidadeLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.unidadeLabel_2.setObjectName("unidadeLabel_2")
        self.horizontalLayout_5.addWidget(self.unidadeLabel_2)
        self.unidadeNovoDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.unidadeNovoDoubleSpinBox.setMaximum(9999.99)
        self.unidadeNovoDoubleSpinBox.setObjectName("unidadeNovoDoubleSpinBox")
        self.horizontalLayout_5.addWidget(self.unidadeNovoDoubleSpinBox)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.valorLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.valorLabel_2.setObjectName("valorLabel_2")
        self.horizontalLayout_6.addWidget(self.valorLabel_2)
        self.valorNovoDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.valorNovoDoubleSpinBox.setMaximum(999.99)
        self.valorNovoDoubleSpinBox.setObjectName("valorNovoDoubleSpinBox")
        self.horizontalLayout_6.addWidget(self.valorNovoDoubleSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelMensalVelho = QtWidgets.QLabel(Dialog)
        self.labelMensalVelho.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMensalVelho.setObjectName("labelMensalVelho")
        self.horizontalLayout_8.addWidget(self.labelMensalVelho)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.labelMensalNovo = QtWidgets.QLabel(Dialog)
        self.labelMensalNovo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMensalNovo.setObjectName("labelMensalNovo")
        self.horizontalLayout_8.addWidget(self.labelMensalNovo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.labelDiferenca = QtWidgets.QLabel(Dialog)
        self.labelDiferenca.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDiferenca.setObjectName("labelDiferenca")
        self.horizontalLayout_8.addWidget(self.labelDiferenca)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Item"))
        self.label.setText(_translate("Dialog", "nome"))
        self.groupBox.setTitle(_translate("Dialog", "Último"))
        self.quantiaLabel.setText(_translate("Dialog", "Quantia"))
        self.unidadeLabel.setText(_translate("Dialog", "Unidade"))
        self.label_5.setText(_translate("Dialog", "kg"))
        self.valorLabel.setText(_translate("Dialog", "Valor"))
        self.groupBox_2.setTitle(_translate("Dialog", "Novo"))
        self.quantiaLabel_2.setText(_translate("Dialog", "Quantia"))
        self.unidadeLabel_2.setText(_translate("Dialog", "Unidade"))
        self.label_6.setText(_translate("Dialog", "kg"))
        self.valorLabel_2.setText(_translate("Dialog", "Valor"))
        self.labelMensalVelho.setText(_translate("Dialog", "mensal"))
        self.labelMensalNovo.setText(_translate("Dialog", "mensal novo"))
        self.labelDiferenca.setText(_translate("Dialog", "diferença"))