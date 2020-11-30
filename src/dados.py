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

        # abre a tabela, ou cria caso não exista
        try:
            self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
            self.tabela = self.tabela.drop_duplicates()
        except FileNotFoundError:
            self.tabela = pd.DataFrame(columns=self.colunas)
            self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')


    def atualizar(self):
        self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
        self.tabela = self.tabela.drop_duplicates()

    def adicionar(self, linha):
        indice = self.tabela.index.max()+1
        if pd.isna(indice):
            indice = 0
        add = pd.DataFrame(
            [linha],
            columns=self.colunas,
            index=[indice]
        )
        self.tabela = self.tabela.append(add, ignore_index=False, sort=False)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

    def reduz_estoque(self, id):
        if self.tabela.loc[id]["quantia"] > 1:
            self.tabela.loc[id]["quantia"] -= 1
            self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')
        else:
            self.excluir(id)

    def editar(self, id, linha):
        self.tabela.loc[id] = linha
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

    def excluir(self, id):
        self.tabela = self.tabela.drop(id)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

    # def add_coluna(self, nome):
    #     self.tabela[nome] = 0
    #     self.tabela = self.tabela[[nome]+self.colunas]
    #     self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')
