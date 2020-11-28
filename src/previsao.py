from datetime import datetime

import pandas as pd


class Previsao:

    modo = 0

    def __init__(self, item, entrada, modo):
        self.modo = modo
        self.colunas = ["id_item", "freq"]
        self.tabela = pd.DataFrame(columns=self.colunas)
        self.previsao = pd.DataFrame(columns=["item", "dias"])
        self.atualizar(entrada, item)

    def atualizar(self, entrada, item):
        self.tabela = self.tabela.iloc[0:0]
        self.previsao = self.previsao.iloc[0:0]
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
                # calcula o fator entre dias/(quantia*unidade) e corta os valores nulos
                entradas["vezes"] = entradas.apply(lambda row: row["quantia"] * row["unidade"], axis=1)
                entradas["fator"] = entradas.apply(lambda row: row["dias"] / row["vezes"], axis=1)
                entradas = entradas.sort_values(by=["data"], ascending=True)
                self.previsao = self.previsao.append(entradas[entradas["dias"] > 0][["item", "dias"]])

                if self.modo == 3 and len(entradas) > 0:
                    entradas["peso"] = list(range(1, len(entradas)))+[0]
                    total = entradas["peso"].sum()
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

