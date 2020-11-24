import sys
from datetime import datetime
from os import path, mkdir

from pandas import isna

from src.dados import Dados
from src.gui import Gui
from src.previsao import Previsao
from src.tabela import Tabela, TabelaHistorico

selecionado = -1


def atualizar():
    gui.ui.tableWidget.currentItemChanged.disconnect()
    gui.ui.graficoBarra_2.limpa()
    Entrada.atualizar()
    Item.atualizar()
    Previsao.atualizar(Entrada.tabela, Item.tabela)
    Tabela.atualiza(Item.tabela, Entrada.tabela, Previsao.tabela)
    gui.ui.tableWidget.currentItemChanged.connect(tabela_seleciona)
    # gui.ui.tableWidget.setCurrentCell(selecionado+1, 0)
    gui.ui.tableWidget.setCurrentCell(0, 0)


def limpar_texto(*arg):
    for i in arg:
        i.clear()


def limpar_check(*arg):
    for i in arg:
        i.setCheckState(0)

def botao_add():
    limpar_texto(
        gui.uiAdd.nomeLineEdit,
        gui.uiAdd.valorDoubleSpinBox,
        gui.uiAdd.unidadeLineEdit
    )
    limpar_check(
        gui.uiAdd.contCheckBox,
        gui.uiAdd.mensCheckBox,
    )
    gui.wAdd.show()


def botao_editar():
    global selecionado
    if selecionado >= 0:
        item = gui.ui.tableWidget.item(selecionado, 0).text()
        item = Item.tabela[Item.tabela["nome"] == item]

        nome = item["nome"].item()
        valor = item["valor"].item()
        unidade = str(item["unidade"].item())
        mensuravel = item["mensuravel"].item()
        contavel = item["contavel"].item()
        if unidade == "nan":
            unidade = ""

        gui.uiEditar.nomeLineEdit.setText(nome)
        gui.uiEditar.unidadeLineEdit.setText(unidade)
        gui.uiEditar.valorDoubleSpinBox.setValue(valor)
        if int(mensuravel):
            gui.uiEditar.mensCheckBox.setCheckState(2)
        else:
            gui.uiEditar.mensCheckBox.setCheckState(0)
        if int(contavel):
            gui.uiEditar.contCheckBox.setCheckState(2)
        else:
            gui.uiEditar.contCheckBox.setCheckState(0)

        gui.wEditar.show()


def editar_aceitar():
    global selecionado
    item = gui.ui.tableWidget.item(selecionado, 0).text()
    item = Item.tabela[Item.tabela["nome"] == item]

    nome = gui.uiEditar.nomeLineEdit.text()
    nome = nome.capitalize()

    if len(nome) > 1:

        valor = gui.uiEditar.valorDoubleSpinBox.value()
        unidade = gui.uiEditar.unidadeLineEdit.text()
        contavel = int(bool(gui.uiEditar.contCheckBox.checkState()))
        mensuravel = int(bool(gui.uiEditar.mensCheckBox.checkState()))
        Item.editar(item.index.item(), [nome, valor, contavel, mensuravel, unidade])
        atualizar()


def botao_excluir():
    global selecionado
    if selecionado >= 0:
        item = gui.ui.tableWidget.item(selecionado, 0).text()
        item = Item.tabela[Item.tabela["nome"] == item]
        nome = item["nome"].item()
        gui.uiExcluir.nomeLabel.setText(nome)
        gui.wExcluir.show()


def botao_historico():
    global selecionado, Historico
    if selecionado >= 0:
        gui.uiHistorico.tableWidget.cellChanged.connect(tabela_edita)
        item = gui.ui.tableWidget.item(selecionado, 0).text()
        item = Item.tabela[Item.tabela["nome"] == item]
        id_selecionado = item.index.item()
        entradas = Entrada.tabela[Entrada.tabela["item"] == id_selecionado]
        nome = item["nome"].item()
        gui.uiHistorico.label.setText("Editar " + nome)
        Historico.atualiza(item, entradas)
        gui.wHistorico.show()


def tabela_edita(linha, coluna):
    Historico.sinal(linha, coluna)


def historico_aceitar():
    global Entrada
    itens = []
    for i in range(0, gui.uiHistorico.tableWidget.rowCount()):
        id_item = int(gui.uiHistorico.tableWidget.verticalHeaderItem(i).text())
        data = gui.uiHistorico.tableWidget.item(i, 0).text()
        quantia = gui.uiHistorico.tableWidget.item(i, 1).text()
        unidade = gui.uiHistorico.tableWidget.item(i, 2).text()
        # print(Entrada.tabela.loc[id_item])
        # print(data, quantia, unidade)
        # item = gui.ui.tableWidget.item(selecionado, 0).text()
        # item = Item.tabela[Item.tabela["nome"] == item]
        # id_selecionado = item.index.item()
        print(
            Entrada.tabela.loc[id_item]["item"],
            [
                id_item,
                quantia,
                unidade,
                data,
            ]
        )
        Entrada.editar(
            id_item,
            [
                Entrada.tabela.loc[id_item]["item"],
                quantia,
                unidade,
                data,
            ]
        )
    Entrada = Dados("entrada",
                    ['item', 'quantia', 'unidade', 'data']
                    )
    atualizar()


def excluir_aceitar():
    global selecionado
    item = gui.ui.tableWidget.item(selecionado, 0).text()
    item = Item.tabela[Item.tabela["nome"] == item]
    id_selecionado = item.index.item()
    entradas = Entrada.tabela[Entrada.tabela["item"] == id_selecionado]
    entradas = list(entradas.index)
    for i in entradas:
        Entrada.excluir(i)
    Item.excluir(id_selecionado)
    atualizar()


def botao_feito():
    global selecionado
    limpar_texto(
        gui.uiEntrada.labelNome,
        gui.uiEntrada.valorDoubleSpinBox,
        gui.uiEntrada.label
    )
    if selecionado >= 0:
        item = gui.ui.tableWidget.item(selecionado, 0).text()
        item = Item.tabela[Item.tabela["nome"] == item]

        nome = item["nome"].item()
        valor = item["valor"].item()
        unidade = str(item["unidade"].item())
        mensuravel = item["mensuravel"].item()
        contavel = item["contavel"].item()
        if unidade == "nan":
            unidade = ""

        gui.uiEntrada.labelNome.setText(nome)
        gui.uiEntrada.valorDoubleSpinBox.setValue(valor)
        gui.uiEntrada.unidadeDoubleSpinBox.setValue(1)
        gui.uiEntrada.quantiaSpinBox.setValue(1)
        if int(mensuravel):
            gui.uiEntrada.label.setEnabled(True)
            gui.uiEntrada.unidadeLabel.setEnabled(True)
            gui.uiEntrada.unidadeDoubleSpinBox.setEnabled(True)
            gui.uiEntrada.label.setText(unidade)
        else:
            gui.uiEntrada.label.setEnabled(False)
            gui.uiEntrada.unidadeLabel.setEnabled(False)
            gui.uiEntrada.unidadeDoubleSpinBox.setEnabled(False)
        if int(contavel):
            gui.uiEntrada.quantiaLabel.setEnabled(True)
            gui.uiEntrada.quantiaSpinBox.setEnabled(True)
        else:
            gui.uiEntrada.quantiaLabel.setEnabled(False)
            gui.uiEntrada.quantiaSpinBox.setEnabled(False)
        gui.uiEntrada.dataDateEdit.setDate(datetime.now())
        gui.wEntrada.show()


def entrada_aceitar():
    global selecionado
    item = gui.ui.tableWidget.item(selecionado, 0).text()
    linha = Item.tabela[Item.tabela["nome"] == item]
    valor_antigo = linha["valor"].values[0]
    item = linha.index.values[0]

    valor = gui.uiEntrada.valorDoubleSpinBox.value()
    unidade = gui.uiEntrada.unidadeDoubleSpinBox.value()
    quantia = gui.uiEntrada.quantiaSpinBox.value()
    data = gui.uiEntrada.dataDateEdit.date().toString("dd/MM/yy")
    # ['id', 'item', 'quantia', 'unidade', 'data']

    if valor_antigo != valor:
        # ['nome', 'valor', 'contavel', 'mensuravel', 'unidade']
        Item.editar(
            item,
            [
                linha["nome"].item(),
                valor,
                linha["contavel"].item(),
                linha["mensuravel"].item(),
                linha["unidade"].item(),
            ]
        )

    Entrada.adicionar([
        item,
        quantia,
        unidade,
        data
    ])
    atualizar()


def add_aceitar():
    nome = gui.uiAdd.nomeLineEdit.text()
    nome = nome.capitalize()
    if len(nome) > 1:
        valor = gui.uiAdd.valorDoubleSpinBox.value()
        unidade = gui.uiAdd.unidadeLineEdit.text()
        contavel = int(bool(gui.uiAdd.contCheckBox.checkState()))
        mensuravel = int(bool(gui.uiAdd.mensCheckBox.checkState()))
        Item.adicionar([nome, valor, contavel, mensuravel, unidade])
        atualizar()
        gui.wAdd.hide()
    else:
        print("Nome vazio")


def tabela_seleciona(item):
    global selecionado
    linha = item.row()
    if selecionado != linha:
        # gui.ui.graficoBarra_2.hide()
        selecionado = linha
        texto = gui.ui.tableWidget.item(linha, 0).text()
        gui.ui.labelNome.setText(texto)

        item = Item.tabela[Item.tabela["nome"] == texto]
        unidade = item["unidade"].item()

        item = item.index.values[0]

        ultimo = gui.ui.tableWidget.item(linha, 1).text()

        print("ID:\n", item)
        print("UNIDADE:\n", unidade)
        info = Entrada.tabela[Entrada.tabela["item"] == item]
        if len(info):
            info = info[info["data"] == ultimo]

            vezes = info["quantia"].item()
            unidades = info["unidade"].item()

            if vezes > 1:
                vezes = " " + str(vezes) + " x"
            else:
                vezes = ""

            if isna(unidade):
                unidades = ""
            else:
                unidades = str(unidades)
                unidades = unidades.replace(".", ",")
                unidades = unidades.replace(",0", "")
                unidades = " " + unidades + unidade

        prox = gui.ui.tableWidget.item(linha, 2).text()

        if prox != "Sem previsão":
            data_ultimo = datetime.strptime(ultimo, "%d/%m/%y")
            ultimo = ultimo + "\t" + vezes + unidades
            gui.ui.labelUltimo.setText(ultimo)
            entradas = Previsao.previsao[Previsao.previsao["item"] == item]
            print("Selecionado:\n",  entradas)
            entradas = list(entradas["dias"])
            gui.ui.graficoBarra_2.limpa()
            hoje = datetime.now()

            data_prox = datetime.strptime(prox, "%d/%m/%y")
            entradas = entradas + [(hoje-data_ultimo).days]
            dias = (data_prox-data_ultimo).days
            print("Tempo:\n",  dias)
            gui.ui.graficoBarra_2.plot(dias, entradas)
        else:
            gui.ui.labelUltimo.setText(ultimo)
            gui.ui.graficoBarra_2.limpa()
        gui.ui.graficoBarra_2.show()


def seleciona_modo():
    global modo
    print("Seleciona Modo")
    modo = gui.ui.modoComboBox.currentIndex()
    print(modo)
    with open("data/config.ini", "w") as arquivo:
        arquivo.write(str(modo))
        arquivo.close()
    Previsao.modo = modo
    atualizar()

gui = Gui()

gui.uiHistorico.botaoExcluir.hide()

modo = 0

if not path.exists("data"):
    mkdir("data")

try:
    with open("data/config.ini", "r") as arquivo:
        modo = int(arquivo.read())
        arquivo.close()
except FileNotFoundError:
    with open("data/config.ini", "w") as arquivo:
        arquivo.write("0")
        arquivo.close()

gui.ui.modoComboBox.setCurrentIndex(modo)

Item = Dados("item",
             ['nome', 'valor', 'contavel', 'mensuravel', 'unidade']
             )
Entrada = Dados("entrada",
                ['item', 'quantia', 'unidade', 'data']
                )

Previsao = Previsao(Item.tabela, Entrada.tabela, modo)

Tabela = Tabela(gui.ui.tableWidget, Item.tabela, Entrada.tabela, Previsao.tabela, gui.ui.labelFundo, gui.ui.labelMes)

Historico = TabelaHistorico(gui.uiHistorico.tableWidget)

gui.ui.tableWidget.resizeColumnsToContents()
#definições dos botões
gui.ui.botaoAdicionar.clicked.connect(botao_add)
gui.ui.botaoEditar.clicked.connect(botao_editar)
gui.ui.botaoFeito.clicked.connect(botao_feito)
gui.ui.botaoExcluir.clicked.connect(botao_excluir)
gui.ui.botaoHistorico.clicked.connect(botao_historico)
gui.uiAdd.buttonBox.accepted.connect(add_aceitar)
gui.uiEntrada.buttonBox.accepted.connect(entrada_aceitar)
gui.uiEditar.buttonBox.accepted.connect(editar_aceitar)
gui.uiExcluir.buttonBox.accepted.connect(excluir_aceitar)
gui.uiHistorico.buttonBox.accepted.connect(historico_aceitar)

#definições dos sinais
gui.ui.tableWidget.currentItemChanged.connect(tabela_seleciona)
gui.ui.modoComboBox.currentIndexChanged.connect(seleciona_modo)

sys.exit(gui.app.exec_())
