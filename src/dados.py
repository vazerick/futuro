import os

import pandas as pd


class Dados:

    colunas = []

    def __init__(self, nome, colunas):

        self.colunas = colunas
        self.nome = nome

        if not os.path.exists('data'):
            os.makedirs('data')

        self.endereco = 'data/' + self.nome + ".csv"

        print("Abrindo o arquivo ", self.endereco)

        # abre a tabela, ou cria caso não exista
        try:
            self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
        except FileNotFoundError:
            self.tabela = pd.DataFrame(columns=self.colunas)
            self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

    def adicionar(self, linha):
        add = pd.DataFrame(
            [linha],
            columns=self.colunas,
            index=[self.tabela.index.max()+1]
        )
        self.tabela = self.tabela.append(add, ignore_index=False, sort=False)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

    def editar(self, id, linha):
        self.tabela.loc[id] = linha
        print(id, linha)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

    def excluir(self, id):
        self.tabela = self.tabela.drop(id)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')
