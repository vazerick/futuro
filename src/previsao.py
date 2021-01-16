from datetime import datetime

import pandas as pd


class Previsao:

    modo = 0

    def __init__(self, item, entrada, ferias, modo):
        self.modo = modo
        self.colunas = ["id_item", "freq"]
        self.tabela = pd.DataFrame(columns=self.colunas)
        self.previsao = pd.DataFrame(columns=["item", "dias"])
        self.atualizar(entrada, item, ferias)

    def atualizar(self, entrada, item, ferias):
        self.tabela = self.tabela.iloc[0:0]
        self.previsao = self.previsao.iloc[0:0]
        ferias = ferias.copy()
        if len(ferias) > 0:
            ferias["inicio"] = ferias["inicio"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
            ferias["fim"] = ferias["fim"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
            ferias["dias"] = ferias.apply(lambda row: row["fim"] - row["inicio"], axis=1)
            ferias["dias"] = ferias.apply(lambda row: row["dias"].days, axis=1)
        # lê cada item
        for index, row in item.iterrows():
            # cria uma cópia das entradas do item
            entradas = entrada[entrada["item"] == index].copy()
            if len(entradas):
                # converte a data para datetime
                entradas["data"] = entradas["data"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
                # calcula a diferença das datas e limpa os dados
                entradas = entradas.sort_values(by=["data"], ascending=True)
                entradas["dias"] = -entradas["data"].diff(periods=-1)
                entradas["dias"] = entradas["dias"].fillna(pd.Timedelta(seconds=0))
                entradas["dias"] = entradas.apply(lambda row: row["dias"].days, axis=1)
                entradas["ferias"] = 0
                if len(ferias) > 0 and bool(int(row["pausa"])):
                    for ferias_index, ferias_row in ferias.iterrows():
                        for i in range(0, len(entradas)-1):
                            ferias_inicio = ferias.loc[ferias_index]["inicio"]
                            ferias_fim = ferias.loc[ferias_index]["fim"]
                            entrada_inicio = entradas.iloc[i]["data"]
                            entrada_fim = entradas.iloc[i+1]["data"]
                            entrada_periodo = pd.Interval(entrada_inicio,
                                                          entrada_fim)
                            if ferias_inicio in entrada_periodo and ferias_fim in entrada_periodo:
                                entradas.iloc[i, entradas.columns.get_loc('ferias')] = ferias.iloc[ferias_index]["dias"]
                # calcula o fator entre dias/(quantia*unidade) e corta os valores nulos
                entradas["dias"] = entradas.apply(lambda row: row["dias"] - row["ferias"], axis=1)
                entradas["vezes"] = entradas.apply(lambda row: row["quantia"] * row["unidade"], axis=1)
                entradas["fator"] = entradas.apply(lambda row: row["dias"] / row["vezes"] if row["vezes"] > 0 else 0, axis=1)
                entradas = entradas.sort_values(by=["data"], ascending=True)
                previsao = entradas.copy()
                previsao = previsao[previsao["dias"] > 0]
                previsao = previsao[previsao["fator"] > 0]
                self.previsao = self.previsao.append(previsao[["item", "dias"]])
                if self.modo == 3 and len(entradas) > 0:
                    entradas = entradas[entradas["vezes"] > 0]
                    entradas["peso"] = list(range(1, len(entradas)))+[0]
                    total = entradas["peso"].sum()
                    # entradas["peso"] = entradas.apply(lambda : int(bool(row["vezes"])) * row["peso"])
                    entradas["fator"] = entradas.apply(lambda row: row["peso"] * row["fator"], axis=1)
                    entradas = entradas[entradas["fator"] > 0]["fator"]
                    if total > 0:
                        linha = pd.DataFrame(
                            [[index, entradas.sum()/total]],
                            columns=self.colunas
                        )
                    else:
                        linha = pd.DataFrame(
                            [[index, None]],
                            columns=self.colunas
                        )
                else:
                    entradas = entradas[entradas["fator"] > 0]["fator"]

                    if self.modo == 1 and len(entradas) > 4:
                        i = int(len(entradas)/6)+1
                        entradas = entradas.drop(entradas.nlargest(i, keep='first').index)
                        entradas = entradas.drop(entradas.nsmallest(i, keep='first').index)

                    # adiciona na tabela a frequência média

                    if self.modo == 2:
                        linha = pd.DataFrame(
                            [[index, entradas.median(axis=0)]],
                            columns=self.colunas
                        )
                    else:
                        linha = pd.DataFrame(
                            [[index, entradas.mean()]],
                            columns=self.colunas
                        )

            else:
                linha = pd.DataFrame(
                    [[index, None]],
                    columns=self.colunas
                )
            self.tabela = self.tabela.append(linha, ignore_index=True, sort=False)
