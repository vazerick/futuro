from datetime import timedelta, datetime
from math import floor
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.Qt import QFont
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView


class Tabela:

    def __init__(self, widget, item, entrada, previsao, estoque, ferias, fundo, mes, dif, corte):

        self.widget = widget
        self.labelFundo = fundo.setText
        self.labelMes = mes.setText
        self.labelDif = dif.setText
        self.atualiza(item, entrada, previsao, estoque, ferias, corte)

    def atualiza(self, item, entrada, previsao, estoque, ferias, corte):
        #limpa a tabela
        self.widget.clear()
        self.widget.setRowCount(0)
        self.widget.setColumnCount(5)
        mensal = ""
        mensal_int = 0
        fator_estoque = 1
        flag = 0
        header = ["Item", "Último", "Previsão", "Valor", "Mensal"]
        colunas = ["nome", "ultimo", "prev", "valor", "mensal_int", "mensal", "fator_estoque", "flag"]
        self.widget.setHorizontalHeaderLabels(header)
        self.widget.verticalHeader().setVisible(False)
        entrada = entrada.copy()
        entrada["data"] = entrada["data"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
        tabela = pd.DataFrame(columns=colunas)
        ferias = ferias.copy()
        if len(ferias) > 0:
            ferias["inicio"] = ferias["inicio"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
            ferias["fim"] = ferias["fim"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
            ferias["dias"] = ferias.apply(lambda row: row["fim"] - row["inicio"], axis=1)
            ferias["dias"] = ferias.apply(lambda row: row["dias"].days, axis=1)

        em_pausa = pd.DataFrame(columns=colunas)
        sem_prev = pd.DataFrame(columns=colunas)
        sem_entr = pd.DataFrame(columns=colunas)

        for index, row in item.iterrows():
            flag = 0
            fator_estoque = 1
            historico = entrada[entrada["item"] == index].copy()
            if len(historico):
                historico["vezes"] = historico.apply(lambda row: row["quantia"]*row["unidade"], axis=1)
                nome = row["nome"]
                valor = "R${:.2f}".format(float(row["valor"])).replace(".", ",")
                ultimo = historico["data"].max()
                vezes = historico[historico["data"] == ultimo]["vezes"].iloc[-1].item()
                if len(previsao[previsao["id_item"] == index]):
                    freq = previsao[previsao["id_item"] == index]["freq"].item()
                else:
                    freq = pd.NA

                if pd.isna(freq):
                    linha = [
                        nome,
                        # ultimo.strftime("%d/%m/%y"),
                        ultimo,
                        "Sem previsão",
                        valor,
                        mensal_int,
                        mensal,
                        fator_estoque,
                        flag
                    ]
                    self.widget.insertRow(0)
                    sem_prev = sem_prev.append(pd.DataFrame([linha], columns=colunas), ignore_index=True, sort=False)
                elif vezes == 0:
                    linha = [
                        nome,
                        "Pausa",
                        "Sem previsão",
                        valor,
                        mensal_int,
                        mensal,
                        fator_estoque,
                        flag
                    ]
                    self.widget.insertRow(0)
                    em_pausa = em_pausa.append(pd.DataFrame([linha], columns=colunas), ignore_index=True, sort=False)
                else:
                    tempo = round(vezes*freq)
                    if tempo == 0:
                        tempo = 1
                    prev = ultimo + timedelta(days=tempo)
                    pausa = 0
                    if len(ferias) > 0 and bool(int(row["pausa"])):
                        quantia_estoque = estoque[estoque["item"] == index]["quantia"]
                        if len(quantia_estoque):
                            quantia_estoque = quantia_estoque.item()
                        else:
                            quantia_estoque = 0
                        quantia_estoque += 1
                        limite = ultimo + timedelta(days=tempo)*quantia_estoque
                        for ferias_index, ferias_row in ferias.iterrows():
                            ferias_inicio = ferias.loc[ferias_index]["inicio"]
                            ferias_fim = ferias.loc[ferias_index]["fim"]
                            intervalo = pd.Interval(ultimo,
                                                    prev)
                            intervalo_total = pd.Interval(ultimo,
                                                    limite)
                            if ferias_inicio in intervalo:
                                dias_ferias = ferias.loc[ferias_index]["dias"].item()
                                prev = prev + timedelta(days=dias_ferias)
                                pausa += dias_ferias
                            elif ferias_inicio in intervalo_total:
                                flag += 1
                    mensal_int = ((row["valor"]/timedelta(days=tempo).days)*30)
                    mensal_int = round(mensal_int/5, 0)*5
                    if mensal_int > row["valor"]:
                        fator_estoque = mensal_int/row["valor"]
                        # fator_estoque = int(fator_estoque)
                    mensal = "R${:.0f}".format(mensal_int)
                    linha = [
                        nome,
                        ultimo.strftime("%d/%m/%y"),
                        # prev.strftime("%d/%m/%y"),
                        prev,
                        valor,
                        mensal_int,
                        mensal,
                        fator_estoque,
                        flag
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
                    mensal,
                    fator_estoque,
                    flag
                ]
                self.widget.insertRow(0)
                sem_entr = sem_entr.append(pd.DataFrame([linha], columns=colunas), ignore_index=True, sort=False)

        linha = 0

        mes = 0

        tabela = tabela.sort_values(by=["prev"])

        sem_prev = sem_prev.sort_values(by=["ultimo"])
        sem_prev["ultimo"] = sem_prev["ultimo"].apply(lambda row: datetime.strftime(row, "%d/%m/%y"))

        sem_entr = sem_entr.sort_values(by=["nome"])

        for index, row in tabela.iterrows():
            font = QFont()
            if row["prev"] < datetime.today() + timedelta(days=corte):
                temp = item[item["nome"] == row["nome"]]
                id_item =temp.index.item()
                quantia_estoque = estoque[estoque["item"] == id_item]
                fator_estoque = row["fator_estoque"]
                fator_estoque = fator_estoque*(corte/30)
                if len(quantia_estoque) > 0:
                    quantia_estoque = quantia_estoque["quantia"].item()
                else:
                    quantia_estoque = 0
                if quantia_estoque < fator_estoque and not (row["flag"]):
                    font.setBold(True)
                    valor = float(row["valor"].replace("R$", "").replace(",", "."))
                    if fator_estoque > 1:
                        valor = valor * floor(fator_estoque - quantia_estoque)
                    mes = mes + valor
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
                tabela_item = QTableWidgetItem(row[nome])
                tabela_item.setFont(font)
                self.widget.setItem(linha, i, tabela_item)
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

        for index, row in em_pausa.iterrows():
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

        fundo = tabela["mensal_int"].sum()
        mes = round(mes/5, 0)*5
        dif = fundo - mes
        self.labelFundo("Fundo mensal: " + "R${:.2f}".format(fundo).replace(".", ","))
        self.labelMes("Próximos gastos: " + "R${:.2f}".format(mes).replace(".", ","))
        self.labelDif("Diferença: " + "R${:.2f}".format(dif).replace(".", ","))
        # self.labelMes(str(mes))
        self.widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.widget.setSortingEnabled(True)
        self.tabela = tabela


class TabelaHistorico:

    entrada=[]

    def __init__(self, widget):
        self.widget = widget

    def atualiza(self, item, entrada):
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


class TabelaPlanejar:

    def __init__(self, widget_estoque, widget_planejamento, label_ultimo, label_primeiro, label_intervalo):
        self.estoque = widget_estoque
        self.planejamento = widget_planejamento
        self.colunas = ["nome", "prev", "quantia", "unidade", "sigla", "freq", "estoque"]
        self.tabela = pd.DataFrame(columns=self.colunas)
        self.ultimo = label_ultimo.setText
        self.primeiro = label_primeiro.setText
        self.invervalo = label_intervalo.setText

    def atualiza_estoque(self):
        self.estoque.clear()
        self.estoque.setRowCount(0)
        self.estoque.setColumnCount(5)
        header = ["Nome", "Quantia", "Unidade", "", "Estoque"]
        self.estoque.setHorizontalHeaderLabels(header)
        self.estoque.verticalHeader().setVisible(True)
        self.estoque.setRowCount(len(self.tabela))
        linha = 0
        header_linhas = []
        for index, row in self.tabela.iterrows():
            item = QTableWidgetItem(str(row["nome"]))
            item.setFlags(Qt.ItemIsEnabled)
            self.estoque.setItem(linha, 0, item)
            item = QTableWidgetItem(str(row["quantia"]))
            self.estoque.setItem(linha, 1, item)
            item = QTableWidgetItem(str(row["unidade"]))
            self.estoque.setItem(linha, 2, item)
            item = QTableWidgetItem(row["sigla"])
            item.setFlags(Qt.ItemIsEnabled)
            self.estoque.setItem(linha, 3, item)
            item = QTableWidgetItem(str(row["estoque"]))
            self.estoque.setItem(linha, 4, item)
            linha += 1
        self.estoque.resizeColumnsToContents()

    def atualiza_planejamento(self):
        self.tabela["quantia_planejamento"] = self.tabela["quantia"]
        self.tabela["unidade_planejamento"] = self.tabela["unidade"]
        self.tabela["compra"] = 0
        self.planejamento.clear()
        self.planejamento.setRowCount(0)
        self.planejamento.setColumnCount(6)
        header = ["Nome", "Quantia", "Unidade", "", "Comprar", "Previsao"]
        self.planejamento.setHorizontalHeaderLabels(header)
        self.planejamento.verticalHeader().setVisible(True)
        self.planejamento.setRowCount(len(self.tabela))
        linha = 0
        header_linhas = []
        for index, row in self.tabela.iterrows():
            item = QTableWidgetItem(str(row["nome"]))
            item.setFlags(Qt.ItemIsEnabled)
            self.planejamento.setItem(linha, 0, item)
            item = QTableWidgetItem(str(row["quantia_planejamento"]))
            self.planejamento.setItem(linha, 1, item)
            item = QTableWidgetItem(str(row["unidade_planejamento"]))
            self.planejamento.setItem(linha, 2, item)
            item = QTableWidgetItem(row["sigla"])
            item.setFlags(Qt.ItemIsEnabled)
            self.planejamento.setItem(linha, 3, item)
            item = QTableWidgetItem(str(row["compra"]))
            self.planejamento.setItem(linha, 4, item)
            item = QTableWidgetItem("xxx")
            item.setFlags(Qt.ItemIsEnabled)
            self.planejamento.setItem(linha, 5, item)
            linha += 1
        self.planejamento.resizeColumnsToContents()
        self.calcular()

    def limpa(self):
        self.estoque.clear()
        self.planejamento.clear()
        self.tabela = pd.DataFrame(columns=[
            "nome", "prev", "quantia", "unidade", "sigla", "freq", "estoque"
        ])

    def add(self, linha):
        indice = self.tabela.index.max() + 1
        if pd.isna(indice):
            indice = 0
        add = pd.DataFrame(
            [linha],
            columns=self.colunas,
            index=[indice]
        )
        self.tabela = self.tabela.append(add, ignore_index=False, sort=False)

    def sinal_estoque(self, linha, coluna):
        novo = self.estoque.item(linha, coluna).text()
        try:
            float(novo)
        except:
            try:
                novo = novo.replace(",", ".")
                float(novo)
                self.estoque.item(linha, coluna).setText(novo)
            except:
                self.estoque.item(linha, coluna).setText("1")
        self.tabela.loc[linha, "quantia"] = float(self.estoque.item(linha, 1).text())
        self.tabela.loc[linha, "unidade"] = float(self.estoque.item(linha, 2).text())
        self.tabela.loc[linha, "estoque"] = float(self.estoque.item(linha, 4).text())

    def sinal_planejamento(self, linha, coluna):
        novo = self.planejamento.item(linha, coluna).text()
        if coluna in [1, 2, 4]:
            try:
                float(novo)
            except:
                try:
                    novo = novo.replace(",", ".")
                    float(novo)
                    self.planejamento.item(linha, coluna).setText(novo)
                except:
                    self.planejamento.item(linha, coluna).setText("1")
            self.tabela.loc[linha, "quantia_planejamento"] = float(self.planejamento.item(linha, 1).text())
            self.tabela.loc[linha, "unidade_planejamento"] = float(self.planejamento.item(linha, 2).text())
            self.tabela.loc[linha, "compra"] = float(self.planejamento.item(linha, 4).text())
            self.calcular()

    def calcular(self):
        for coluna in [
            "quantia",
            "unidade",
            "estoque"
        ]:
            self.tabela[coluna] = self.tabela.apply(
                lambda row: float(row[coluna]), axis=1
            )
        self.tabela["vezes_estoque"] = self.tabela.apply(
            lambda row: row["quantia"] * row["unidade"] * row["estoque"], axis=1
        )
        self.tabela["dias_estoque"] = self.tabela.apply(
            lambda row: row["vezes_estoque"] * row["freq"], axis=1
        )
        self.tabela["prev_estoque"] = self.tabela.apply(
            lambda row: row["prev"] + timedelta(days=row["dias_estoque"]), axis=1
        )
        self.tabela["vezes_planejamento"] = self.tabela.apply(
            lambda row: row["quantia_planejamento"] * row["unidade_planejamento"] * row["compra"], axis=1
        )
        self.tabela["dias_planejamento"] = self.tabela.apply(
            lambda row: row["vezes_planejamento"] * row["freq"], axis=1
        )
        self.tabela["prev_planejamento"] = self.tabela.apply(
            lambda row: row["prev_estoque"] + timedelta(days=row["dias_planejamento"]), axis=1
        )
        linha = 0
        for index, row in self.tabela.iterrows():
            data = row["prev_planejamento"]
            data = datetime.strftime(data, "%d/%m/%y")
            item = QTableWidgetItem(data)
            item.setFlags(Qt.ItemIsEnabled)
            velho = self.planejamento.item(linha, 5).text()
            if data != velho:
                self.planejamento.setItem(linha, 5, item)
            linha += 1
        self.planejamento.resizeColumnsToContents()
        max = self.tabela["prev_planejamento"].max()
        min = self.tabela["prev_planejamento"].min()
        intervalo = max-min
        self.ultimo(datetime.strftime(max, "%d/%m/%y"))
        self.primeiro(datetime.strftime(min, "%d/%m/%y"))
        self.invervalo(str(intervalo.days) + " dias")
