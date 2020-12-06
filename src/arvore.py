from datetime import datetime

import pandas as pd
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QTreeWidgetItem


class Arvore:

    def __init__(self, widget, tabela):

        self.widget = widget
        self.atualiza(tabela)
        self.index = pd.DataFrame([])

    def atualiza(self, tabela):
        self.widget.clear()
        # self.Indice = pd.DataFrame()
        tabela = tabela.copy()
        tabela = tabela.sort_values(by=["inicio"], ascending=True)
        # tabela["inicio"] = tabela.apply(lambda row: datetime.strftime(row["inicio"], "%d/%m/%y"), axis=1)
        # tabela["fim"] = tabela.apply(lambda row: datetime.strftime(row["fim"], "%d/%m/%y"), axis=1)
        if len(tabela) > 0:
            tabela["inicio_d"] = tabela["inicio"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
            tabela["fim_d"] = tabela["fim"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
            tabela["dias"] = tabela.apply(lambda row: row["fim_d"] - row["inicio_d"], axis=1)
            tabela["dias"] = tabela.apply(lambda row: row["dias"].days, axis=1)
            for index, row in tabela.iterrows():
                WidgetItem = QTreeWidgetItem([row["inicio"], row["fim"], str(row["dias"])+ " dias"])
                self.widget.addTopLevelItem(WidgetItem)
        self.widget.expandAll()


class ArvorePlanejar:

    def __init__(self, widget):
        self.widget = widget

    def atualizar(self, tabela):
        self.widget.clear()
        tabela = tabela.copy()
        tabela = tabela.sort_values(by=["nome"], ascending=True)
        if len(tabela):
            for index, row in tabela.iterrows():
                linha = [row["nome"]]
                WidgetItem = QTreeWidgetItem(linha)
                WidgetItem.setCheckState(0, Qt.Unchecked)
                self.widget.addTopLevelItem(WidgetItem)

    def selecionadas(self):
        checked = []
        root = self.widget.invisibleRootItem()
        signal_count = root.childCount()

        for i in range(signal_count):
            item = root.child(i)
            if item.checkState(0) == Qt.Checked:
                checked.append(item.text(0))

        return checked
