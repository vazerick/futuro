from datetime import timedelta, datetime

import pandas as pd
from PyQt5.Qt import QFont
from PyQt5.QtWidgets import QTableWidgetItem


class Tabela:

    def __init__(self, widget, item, entrada, previsao, fundo, mes):

        self.widget = widget
        self.labelFundo = fundo.setText
        self.labelMes = mes.setText
        self.atualiza(item, entrada, previsao)

    def atualiza(self, item, entrada, previsao):
        #limpa a tabela
        self.widget.clear()
        self.widget.setRowCount(0)
        self.widget.setColumnCount(5)
        mensal = ""
        mensal_int = 0
        header = ["Item", "Último", "Previsão", "Valor", "Mensal"]
        colunas = ["nome", "ultimo", "prev", "valor", "mensal_int", "mensal"]
        self.widget.setHorizontalHeaderLabels(header)
        self.widget.verticalHeader().setVisible(False)
        entrada = entrada.copy()
        entrada["data"] = entrada["data"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
        tabela = pd.DataFrame(columns=colunas)

        sem_prev = pd.DataFrame(columns=colunas)
        sem_entr = pd.DataFrame(columns=colunas)

        for index, row in item.iterrows():
            historico = entrada[entrada["item"] == index].copy()
            if len(historico):
                historico["vezes"] = historico.apply(lambda row: row["quantia"]*row["unidade"], axis=1)
                nome = row["nome"]
                valor = "R${:.2f}".format(float(row["valor"])).replace(".", ",")
                ultimo = historico["data"].max()
                vezes = historico[historico["data"] == ultimo]["vezes"].item()
                if len(previsao[previsao["id_item"] == index]):
                    freq = previsao[previsao["id_item"] == index]["freq"].item()
                else:
                    freq = pd.NA

                if pd.isna(freq):
                    linha = [
                        nome,
                        ultimo.strftime("%d/%m/%y"),
                        "Sem previsão",
                        valor,
                        mensal_int,
                        mensal
                    ]
                    self.widget.insertRow(0)
                    sem_prev = sem_prev.append(pd.DataFrame([linha], columns=colunas), ignore_index=True, sort=False)
                else:
                    tempo = round(vezes*freq)
                    prev = ultimo + timedelta(days=tempo)
                    mensal_int = ((row["valor"]/timedelta(days=tempo).days)*30)
                    mensal_int = round(mensal_int/5, 0)*5
                    mensal = "R${:.0f}".format(mensal_int)
                    linha = [
                        nome,
                        ultimo.strftime("%d/%m/%y"),
                        # prev.strftime("%d/%m/%y"),
                        prev,
                        valor,
                        mensal_int,
                        mensal
                    ]

                    self.widget.insertRow(0)
                    tabela = tabela.append(pd.DataFrame([linha], columns=colunas), ignore_index=True, sort=False)
                    mensal_int = 0
                    mensal = ""
            else:
                nome = row["nome"]
                valor = "R${:.2f}".format(float(row["valor"])).replace(".", ",")
                linha = [
                    nome,
                    "Sem entrada",
                    "Sem previsão",
                    valor,
                    mensal_int,
                    mensal
                ]
                self.widget.insertRow(0)
                sem_entr = sem_entr.append(pd.DataFrame([linha], columns=colunas), ignore_index=True, sort=False)
        tabela = tabela.sort_values(by=["prev"], ascending=False)

        linha = 0
        # tabela["sort"] = tabela.to_datetime(tabela["prev"])
        mes = 0
        tabela = tabela.sort_values(by=["prev"])
        for index, row in tabela.iterrows():
            font = QFont()
            if row["prev"] < datetime.today() + timedelta(days=30):
                font.setBold(True)
                mes = mes + float(row["valor"].replace("R$", "").replace(",", "."))
            else:
                font.setBold(False)
            row["prev"] = row["prev"].strftime("%d/%m/%y")
            for i, nome in [
                [0, "nome"],
                [1, "ultimo"],
                [2, "prev"],
                [3, "valor"],
                [4, "mensal"]
            ]:
                item = QTableWidgetItem(row[nome])
                item.setFont(font)
                self.widget.setItem(linha, i, item)
                # self.widget.item(linha, i)
            linha += 1

        for index, row in sem_prev.iterrows():
            for i, nome in [
                [0, "nome"],
                [1, "ultimo"],
                [2, "prev"],
                [3, "valor"],
                [4, "mensal"]
            ]:
                item = QTableWidgetItem(row[nome])
                self.widget.setItem(linha, i, item)
            linha += 1

        for index, row in sem_entr.iterrows():
            for i, nome in [
                [0, "nome"],
                [1, "ultimo"],
                [2, "prev"],
                [3, "valor"],
                [4, "mensal"]
            ]:
                item = QTableWidgetItem(row[nome])
                self.widget.setItem(linha, i, item)
            linha += 1
        print(tabela)
        fundo = tabela["mensal_int"].sum()
        mes = round(mes/5, 0)*5
        self.labelFundo("Fundo mensal: " + "R${:.2f}".format(fundo).replace(".", ","))
        self.labelMes("Próximos gastos: " + "R${:.2f}".format(mes).replace(".", ","))
        # self.labelMes(str(mes))

class TabelaHistorico:

    entrada=[]

    def __init__(self, widget):
        self.widget = widget

    def atualiza(self, item, entrada):
        print(entrada)
        self.widget.clear()
        self.widget.setRowCount(0)
        self.widget.setColumnCount(3)
        if bool(item["mensuravel"].item()):
            rotulo_unidade = "Unidade (" + item["unidade"].item() + ")"
        else:
            rotulo_unidade = "Unidade"
        header = ["Data", "Quantia", rotulo_unidade]
        self.widget.setHorizontalHeaderLabels(header)
        self.widget.verticalHeader().setVisible(True)
        self.entrada = entrada.copy()
        self.widget.setRowCount(len(entrada))
        linha = 0
        header_linhas = []
        for index, row in self.entrada.iterrows():
            for i, nome in [
                [0, "data"],
                [1, "quantia"],
                [2, "unidade"],
            ]:
                print(linha, i, row[nome])
                item = QTableWidgetItem(str(row[nome]))
                self.widget.setItem(linha, i, item)
            linha += 1
            header_linhas.append(str(index))
        self.widget.setVerticalHeaderLabels(header_linhas)

    def sinal(self, linha, coluna):
        colunas = ["data", "quantia", "unidade"]
        original = self.entrada.iloc[linha][colunas[coluna]]
        novo = self.widget.item(linha, coluna).text()
        if coluna == 0:
            try:
                data = datetime.strptime(novo, "%d/%m/%y")
            except:
                try:
                    data = datetime.strptime(novo, "%d/%m/%Y")
                    self.widget.item(linha, coluna).setText(datetime.strftime(data, "%d/%m/%y"))
                except:
                    self.widget.item(linha, coluna).setText(original)
        elif coluna == 1:
            try:
                if int(novo) != float(novo):
                    self.widget.item(linha, coluna).setText(original)
            except:
                self.widget.item(linha, coluna).setText(str(original))
        else:
            try:
                novo = novo.replace(",", ".")
                novo = float(novo)
                self.widget.item(linha, coluna).setText(str(novo))
            except:
                self.widget.item(linha, coluna).setText(str(original))
        print("Atualiza:")
        print(linha, coluna)
        print("Original:", original)
        print("Novo:", novo)
