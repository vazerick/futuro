# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrada.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(204, 238)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupNome = QtWidgets.QGroupBox(Dialog)
        self.groupNome.setObjectName("groupNome")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupNome)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelNome = QtWidgets.QLabel(self.groupNome)
        self.labelNome.setText("")
        self.labelNome.setObjectName("labelNome")
        self.horizontalLayout_7.addWidget(self.labelNome)
        self.verticalLayout.addWidget(self.groupNome)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.valorLabel = QtWidgets.QLabel(Dialog)
        self.valorLabel.setObjectName("valorLabel")
        self.horizontalLayout.addWidget(self.valorLabel)
        self.valorDoubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.valorDoubleSpinBox.setMaximum(999.99)
        self.valorDoubleSpinBox.setObjectName("valorDoubleSpinBox")
        self.horizontalLayout.addWidget(self.valorDoubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.quantiaLabel = QtWidgets.QLabel(Dialog)
        self.quantiaLabel.setObjectName("quantiaLabel")
        self.horizontalLayout_3.addWidget(self.quantiaLabel)
        self.quantiaSpinBox = QtWidgets.QSpinBox(Dialog)
        self.quantiaSpinBox.setMaximum(999)
        self.quantiaSpinBox.setObjectName("quantiaSpinBox")
        self.horizontalLayout_3.addWidget(self.quantiaSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.unidadeLabel = QtWidgets.QLabel(Dialog)
        self.unidadeLabel.setObjectName("unidadeLabel")
        self.horizontalLayout_2.addWidget(self.unidadeLabel)
        self.unidadeDoubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.unidadeDoubleSpinBox.setMaximum(9999.99)
        self.unidadeDoubleSpinBox.setObjectName("unidadeDoubleSpinBox")
        self.horizontalLayout_2.addWidget(self.unidadeDoubleSpinBox)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dataLabel = QtWidgets.QLabel(Dialog)
        self.dataLabel.setObjectName("dataLabel")
        self.horizontalLayout_4.addWidget(self.dataLabel)
        self.dataDateEdit = QtWidgets.QDateEdit(Dialog)
        self.dataDateEdit.setCalendarPopup(True)
        self.dataDateEdit.setDate(QtCore.QDate(2020, 1, 1))
        self.dataDateEdit.setObjectName("dataDateEdit")
        self.horizontalLayout_4.addWidget(self.dataDateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Entrada"))
        self.groupNome.setTitle(_translate("Dialog", "Nome"))
        self.valorLabel.setText(_translate("Dialog", "Valor"))
        self.quantiaLabel.setText(_translate("Dialog", "Quantia"))
        self.unidadeLabel.setText(_translate("Dialog", "Unidade"))
        self.label.setText(_translate("Dialog", "kg"))
        self.dataLabel.setText(_translate("Dialog", "Data"))
