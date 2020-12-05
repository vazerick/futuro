import sys
from datetime import datetime
from os import path, mkdir

from pandas import isna

from src.arvore import Arvore
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
    Estoque.atualizar()
    Ferias.atualizar()
    Previsao.atualizar(Entrada.tabela, Item.tabela, Ferias.tabela)
    Tabela.atualiza(Item.tabela, Entrada.tabela, Previsao.tabela, Estoque.tabela, Ferias.tabela)
    Arvore.atualiza(Ferias.tabela)
    gui.ui.tableWidget.currentItemChanged.connect(tabela_seleciona)
    temp = selecionado
    if temp >= 0:
        gui.ui.tableWidget.setCurrentCell(0, 0)
        gui.ui.tableWidget.setCurrentCell(temp, 0)


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
        pausa = item["pausa"].item()
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
        if int(pausa):
            gui.uiEditar.pausaCheckBox.setCheckState(2)
        else:
            gui.uiEditar.pausaCheckBox.setCheckState(0)

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
        pausa = int(bool(gui.uiEditar.pausaCheckBox.checkState()))
        Item.editar(item.index.item(), [nome, pausa, valor, contavel, mensuravel, unidade])
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
    selecionado = 0
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

        id_item = item.index.item()
        entrada = Entrada.tabela[Entrada.tabela["item"] == id_item].copy()
        if len(entrada):
            entrada["data"] = entrada["data"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))
            ultimo = entrada["data"].max()
            entrada = entrada[entrada["data"] == ultimo]
            ultimo_unidade = entrada["unidade"].item()
            ultimo_quantia = entrada["quantia"].item()
        else:
            ultimo_unidade = 1
            ultimo_quantia = 1

        gui.uiEntrada.labelNome.setText(nome)
        gui.uiEntrada.valorDoubleSpinBox.setValue(valor)
        gui.uiEntrada.unidadeDoubleSpinBox.setValue(ultimo_unidade)
        gui.uiEntrada.quantiaSpinBox.setValue(ultimo_quantia)
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
                linha["pausa"].item(),
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

    estoque = Estoque.tabela[Estoque.tabela["item"] == item]
    if len(estoque) > 0:
        id_estoque = (estoque.index.item())
        Estoque.reduz_estoque(id_estoque)

    atualizar()


def add_aceitar():
    nome = gui.uiAdd.nomeLineEdit.text()
    nome = nome.capitalize()
    if len(nome) > 1:
        valor = gui.uiAdd.valorDoubleSpinBox.value()
        unidade = gui.uiAdd.unidadeLineEdit.text()
        contavel = int(bool(gui.uiAdd.contCheckBox.checkState()))
        mensuravel = int(bool(gui.uiAdd.mensCheckBox.checkState()))
        pausa = int(bool(gui.uiAdd.pausaCheckBox.checkState()))
        Item.adicionar([nome, pausa, valor, contavel, mensuravel, unidade])
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

        info = Entrada.tabela[Entrada.tabela["item"] == item]

        estoque = Estoque.tabela[Estoque.tabela["item"] == item]
        if len(estoque):
            estoque = estoque["quantia"].item()
        else:
            estoque = 0
        gui.ui.spinBox.setValue(estoque)

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
            entradas = list(entradas["dias"])
            gui.ui.graficoBarra_2.limpa()
            hoje = datetime.now()

            data_prox = datetime.strptime(prox, "%d/%m/%y")
            entradas = entradas + [(hoje-data_ultimo).days]
            dias = (data_prox-data_ultimo).days
            gui.ui.graficoBarra_2.plot(dias, entradas)
        else:
            gui.ui.labelUltimo.setText(ultimo)
            gui.ui.graficoBarra_2.limpa()
        gui.ui.graficoBarra_2.show()


def botao_estoque():
    global selecionado
    if selecionado >= 0:
        item = gui.ui.tableWidget.item(selecionado, 0).text()
        item = Item.tabela[Item.tabela["nome"] == item]
        id_item = (item.index.item())
        estoque = Estoque.tabela[Estoque.tabela["item"] == id_item]
        quantia_nova = gui.ui.spinBox.value()
        if len(estoque) > 0:
            id_estoque = (estoque.index.item())
            quantia = estoque["quantia"].item()
            if quantia_nova != quantia:
                if quantia_nova > 0:
                    Estoque.editar(
                        id_estoque,
                        [
                            id_item,
                            quantia_nova
                        ]
                    )
                    atualizar()
                else:
                    Estoque.excluir(id_estoque)
                    atualizar()
        else:
            quantia = 0
            if quantia_nova > 0:
                Estoque.adicionar(
                    [
                        id_item,
                        quantia_nova
                    ]
                )
                atualizar()


def seleciona_modo():
    global modo
    modo = gui.ui.modoComboBox.currentIndex()
    with open("data/config.ini", "w") as arquivo:
        arquivo.write(str(modo))
        arquivo.close()
    Previsao.modo = modo
    atualizar()


def botao_comparar():
    global selecionado
    limpar_texto(
        gui.uiComparar.valorDoubleSpinBox,
        gui.uiComparar.label,
        gui.uiComparar.labelMensalNovo,
        gui.uiComparar.labelMensalVelho,
        gui.uiComparar.labelDiferenca
    )
    if selecionado >= 0:
        if gui.ui.tableWidget.item(selecionado, 2).text() != "Sem previsão" and gui.ui.tableWidget.item(selecionado, 4).text() != "R$0":
            item = gui.ui.tableWidget.item(selecionado, 0).text()
            item = Item.tabela[Item.tabela["nome"] == item]
            id_item = item.index.item()
            entrada = Entrada.tabela[Entrada.tabela["item"] == id_item].copy()
            entrada["data"] = entrada["data"].apply(lambda row: datetime.strptime(row, "%d/%m/%y"))

            ultimo = entrada["data"].max()
            entrada = entrada[entrada["data"] == ultimo]
            ultimo_unidade = entrada["unidade"].item()
            ultimo_quantia = entrada["quantia"].item()
            print(ultimo_unidade, ultimo_quantia)

            nome = item["nome"].item()
            valor = item["valor"].item()
            unidade = str(item["unidade"].item())
            mensuravel = item["mensuravel"].item()
            contavel = item["contavel"].item()
            if unidade == "nan":
                unidade = ""

            gui.uiComparar.label.setText(nome)
            gui.uiComparar.label_5.setText(unidade)
            gui.uiComparar.label_6.setText(unidade)
            gui.uiComparar.valorDoubleSpinBox.setValue(valor)
            gui.uiComparar.valorNovoDoubleSpinBox.setValue(valor)
            gui.uiComparar.unidadeDoubleSpinBox.setValue(ultimo_unidade)
            gui.uiComparar.unidadeNovoDoubleSpinBox.setValue(ultimo_unidade)
            gui.uiComparar.quantiaSpinBox.setValue(ultimo_quantia)
            gui.uiComparar.quantiaNovoSpinBox.setValue(ultimo_quantia)
            if int(mensuravel):
                gui.uiComparar.unidadeLabel.setEnabled(True)
                gui.uiComparar.unidadeLabel_2.setEnabled(True)
                gui.uiComparar.unidadeDoubleSpinBox.setEnabled(True)
                gui.uiComparar.unidadeNovoDoubleSpinBox.setEnabled(True)
            else:
                gui.uiComparar.unidadeLabel.setEnabled(False)
                gui.uiComparar.unidadeDoubleSpinBox.setEnabled(False)
                gui.uiComparar.unidadeLabel_2.setEnabled(False)
                gui.uiComparar.unidadeNovoDoubleSpinBox.setEnabled(False)
            if int(contavel):
                gui.uiComparar.quantiaLabel.setEnabled(True)
                gui.uiComparar.quantiaSpinBox.setEnabled(True)
                gui.uiComparar.quantiaLabel_2.setEnabled(True)
                gui.uiComparar.quantiaNovoSpinBox.setEnabled(True)
            else:
                gui.uiComparar.quantiaLabel.setEnabled(False)
                gui.uiComparar.quantiaSpinBox.setEnabled(False)
                gui.uiComparar.quantiaLabel_2.setEnabled(False)
                gui.uiComparar.quantiaNovoSpinBox.setEnabled(False)
            for i in [
                gui.uiComparar.unidadeDoubleSpinBox,
                gui.uiComparar.quantiaSpinBox,
                gui.uiComparar.valorDoubleSpinBox
            ]:
                i.setReadOnly(True)
            gui.wComparar.show()
            calculo_comparar()


def calculo_comparar():
    global selecionado
    if selecionado >= 0:
        valor = gui.uiComparar.valorDoubleSpinBox.value()
        mensal = gui.ui.tableWidget.item(selecionado, 4).text()
        gui.uiComparar.labelMensalVelho.setText("Atual: " + mensal +"/mês")
        mensal = valor_to_int(mensal)
        fator_mensal = mensal/valor
        unidade = gui.uiComparar.unidadeDoubleSpinBox.value()
        quantia = gui.uiComparar.quantiaSpinBox.value()
        if unidade > 0 and quantia > 0:

            vezes = unidade*quantia
            fator_valor = valor/vezes
            unidade_novo = gui.uiComparar.unidadeNovoDoubleSpinBox.value()
            quantia_novo = gui.uiComparar.quantiaNovoSpinBox.value()
            valor_novo = gui.uiComparar.valorNovoDoubleSpinBox.value()
            vezes_novo = unidade_novo*quantia_novo
            fator_mensal_novo = (fator_mensal*vezes_novo)/vezes
            fator_valor_novo = valor_novo/vezes_novo

            mensal_novo = (fator_valor_novo/fator_valor)*mensal
            diff = mensal_novo - mensal

            gui.uiComparar.labelMensalNovo.setText("Novo: " + int_to_valor(mensal_novo) +"/mês")
            gui.uiComparar.labelDiferenca.setText("Diferença: " + int_to_valor(diff) +"/mês")
        # print(valor_to_int(valor), valor_to_int(mensal))
        # item = Item.tabela[Item.tabela["nome"] == item]
        # id_item = item.index.item()
        # print(Previsao.tabela[Previsao.tabela["item"] == id_item])


def valor_to_int(valor):
    valor = valor.replace("R$", "")
    valor = valor.replace(",", ".")
    valor = float(valor)
    return valor


def int_to_valor(valor):
    valor = "R${:.0f}".format(valor)
    return valor


def botao_ferias():
    gui.uiFerias.inicioDateEdit.setDate(datetime.now())
    gui.uiFerias.fimDateEdit.setDate(datetime.now())
    gui.wFerias.show()


def ferias_adicionar():
    inicio = gui.uiFerias.inicioDateEdit.date()
    fim = gui.uiFerias.fimDateEdit.date()
    if fim > inicio:
        inicio = inicio.toString("dd/MM/yy")
        fim = fim.toString("dd/MM/yy")
        Ferias.adicionar([inicio, fim])
        atualizar()
    else:
        print("não ok")


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
             ['nome', 'pausa', 'valor', 'contavel', 'mensuravel', 'unidade']
             )
Entrada = Dados("entrada",
                ['item', 'quantia', 'unidade', 'data']
                )
Estoque = Dados("estoque",
                ['item', 'quantia']
                )
Ferias = Dados("ferias",
               ['inicio', 'fim']
               )

Previsao = Previsao(Item.tabela, Entrada.tabela, Ferias.tabela, modo)

Tabela = Tabela(gui.ui.tableWidget, Item.tabela, Entrada.tabela, Previsao.tabela, Estoque.tabela, Ferias.tabela,
                gui.ui.labelFundo, gui.ui.labelMes, gui.ui.labelDif)

Arvore = Arvore(gui.uiFerias.treeWidget, Ferias.tabela)

Historico = TabelaHistorico(gui.uiHistorico.tableWidget)

gui.ajusta()
#definições dos botões
gui.ui.botaoAdicionar.clicked.connect(botao_add)
gui.ui.botaoEditar.clicked.connect(botao_editar)
gui.ui.botaoFeito.clicked.connect(botao_feito)
gui.ui.botaoExcluir.clicked.connect(botao_excluir)
gui.ui.botaoHistorico.clicked.connect(botao_historico)
gui.ui.botaoEstoque.clicked.connect(botao_estoque)
gui.ui.botaoFerias.clicked.connect(botao_ferias)
gui.ui.botaoComparar.clicked.connect(botao_comparar)
gui.uiAdd.buttonBox.accepted.connect(add_aceitar)
gui.uiEntrada.buttonBox.accepted.connect(entrada_aceitar)
gui.uiEditar.buttonBox.accepted.connect(editar_aceitar)
gui.uiExcluir.buttonBox.accepted.connect(excluir_aceitar)
gui.uiHistorico.buttonBox.accepted.connect(historico_aceitar)
gui.uiFerias.botaoAdd.clicked.connect(ferias_adicionar)
gui.uiFerias.pushButton.clicked.connect(gui.wFerias.hide)
gui.uiComparar.buttonBox.accepted.connect(gui.wComparar.hide)
#definições dos sinais
gui.ui.tableWidget.currentItemChanged.connect(tabela_seleciona)
gui.ui.modoComboBox.currentIndexChanged.connect(seleciona_modo)
gui.uiComparar.quantiaNovoSpinBox.valueChanged.connect(calculo_comparar)
gui.uiComparar.unidadeNovoDoubleSpinBox.valueChanged.connect(calculo_comparar)
gui.uiComparar.valorNovoDoubleSpinBox.valueChanged.connect(calculo_comparar)

sys.exit(gui.app.exec_())
