# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(191, 232)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nomeLabel = QtWidgets.QLabel(Dialog)
        self.nomeLabel.setObjectName("nomeLabel")
        self.horizontalLayout_4.addWidget(self.nomeLabel)
        self.nomeLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nomeLineEdit.setObjectName("nomeLineEdit")
        self.horizontalLayout_4.addWidget(self.nomeLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.valorLabel = QtWidgets.QLabel(Dialog)
        self.valorLabel.setObjectName("valorLabel")
        self.horizontalLayout_5.addWidget(self.valorLabel)
        self.valorDoubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.valorDoubleSpinBox.setObjectName("valorDoubleSpinBox")
        self.horizontalLayout_5.addWidget(self.valorDoubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.contVelLabel = QtWidgets.QLabel(Dialog)
        self.contVelLabel.setObjectName("contVelLabel")
        self.horizontalLayout_2.addWidget(self.contVelLabel)
        self.contCheckBox = QtWidgets.QCheckBox(Dialog)
        self.contCheckBox.setObjectName("contCheckBox")
        self.horizontalLayout_2.addWidget(self.contCheckBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mensurVelLabel = QtWidgets.QLabel(Dialog)
        self.mensurVelLabel.setObjectName("mensurVelLabel")
        self.horizontalLayout.addWidget(self.mensurVelLabel)
        self.mensCheckBox = QtWidgets.QCheckBox(Dialog)
        self.mensCheckBox.setObjectName("mensCheckBox")
        self.horizontalLayout.addWidget(self.mensCheckBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.unidadeLabel = QtWidgets.QLabel(Dialog)
        self.unidadeLabel.setObjectName("unidadeLabel")
        self.horizontalLayout_6.addWidget(self.unidadeLabel)
        self.unidadeLineEdit = QtWidgets.QLineEdit(Dialog)
        self.unidadeLineEdit.setObjectName("unidadeLineEdit")
        self.horizontalLayout_6.addWidget(self.unidadeLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
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
        Dialog.setWindowTitle(_translate("Dialog", "Item"))
        self.nomeLabel.setText(_translate("Dialog", "Nome"))
        self.valorLabel.setText(_translate("Dialog", "Valor"))
        self.contVelLabel.setText(_translate("Dialog", "Contável"))
        self.mensurVelLabel.setText(_translate("Dialog", "Mensurável"))
        self.unidadeLabel.setText(_translate("Dialog", "Unidade"))
