import traceback

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.uic import loadUi

from exception.excecoes import ObjetoNaoCadastradaException, ObjetoJaCadastradaException, DataInvalidaException
from fachada.fachada import Fachada
from model.treinoExecutado import TreinoExecutado
from datetime import datetime, date
from utilidades import uteis

f = Fachada.get_instance()

class TelaAluno(QMainWindow):
    """
    Classe que representa a tela do aluno.
    """

    def __init__(self, tela_login):
        super().__init__()

        loadUi("../view/TelaAluno.ui", self)
        self.tela_anterior = tela_login  # Armazena a referência da tela_login
        self.treino = None

        self.configurar_interface()
        self.carregar_treino_do_dia()

    def configurar_interface(self):
        """
        Configura a interface da tela.
        """
        # Informa a data, hora e dia do login
        uteis.obtem_datas_horas_dia(datetime.now(), self.lblData, self.lblHora, self.lblDia)
        self.lblNome.setText(f.pessoaLogada.nome)

        self.btnSair.clicked.connect(self.sair_do_sistema)
        self.btnSalvar.clicked.connect(self.salvar_treino)
        self.btnBuscar.clicked.connect(self.buscar_treino_executado)

        self.modeloTabela = QStandardItemModel()
        self.modeloTabela.setColumnCount(3)
        self.modeloTabela.setHorizontalHeaderLabels(["Nome", "Série", "Duração"])

        self.modeloTabelaTreinoExecutado = QStandardItemModel()
        self.modeloTabelaTreinoExecutado.setColumnCount(3)
        self.modeloTabelaTreinoExecutado.setHorizontalHeaderLabels(["Nome", "Série", "Duração"])

        # Obter a data atual
        data_atual = QDate.currentDate()

        # Definir a data atual no QDateEdit
        self.dateEdit.setDate(data_atual)

        # Definir o limite máximo da data como a data atual
        self.dateEdit.setMaximumDate(data_atual)

    def carregar_treino_do_dia(self):
        """
        Carrega o treino do dia do aluno e preenche a tabela.
        """
        try:
            self.treino = f.consultarTreinoDeHoje(f.pessoaLogada)
            self.preenche_tabela_exercicios(self.treino)
        except ObjetoNaoCadastradaException as e:
            self.exibir_mensagem_erro(str(e))

    def preenche_tabela_exercicios(self, treino):
        """
        Preenche a tabela com os exercícios do treino do dia.
        :param treino: O treino do dia do aluno.
        """
        for exercicio in treino.exercicios:
            nome_item = QStandardItem(exercicio.nome)
            serie_item = QStandardItem(str(exercicio.serie))
            repeticao_item = QStandardItem(str(exercicio.repeticao))

            # Definir o alinhamento dos dados como centralizado
            nome_item.setTextAlignment(Qt.AlignCenter)
            serie_item.setTextAlignment(Qt.AlignCenter)
            repeticao_item.setTextAlignment(Qt.AlignCenter)

            self.modeloTabela.appendRow([nome_item, serie_item, repeticao_item])

        self.configurar_tabela()

    def configurar_tabela(self):
        """
        Configura a tabela com o modelo de dados e ajusta o redimensionamento das colunas e linhas.
        """
        self.tabelaExercicios.setModel(self.modeloTabela)

        self.tabelaExercicios.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabelaExercicios.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def salvar_treino(self):
        if self.treino:
            treino_executado = TreinoExecutado(datetime.now(), self.treino)
            try:
                f.salvarTreinoExecutado(f.pessoaLogada, treino_executado)
                self.exibir_mensagem_sucesso('Treino cadastrado com sucesso!')

            except ObjetoJaCadastradaException:
                self.exibir_mensagem_erro('Treino já cadastrado!')
        else:
            self.exibir_mensagem_erro('Treino não cadastrado!')

    def sair_do_sistema(self):
        """
        Sai do sistema e retorna para a tela de login.
        """
        f.pessoaLogada = None
        self.abrir_tela_login()
        self.close()

    def abrir_tela_login(self):
        """
        Abre a tela de login e esconde a tela atual.
        """
        self.hide()
        self.tela_anterior.limpar_tela()
        self.tela_anterior.show()

    def exibir_mensagem_erro(self, mensagem):
        """
        Exibe uma mensagem de erro.
        :param mensagem: A mensagem de erro a ser exibida.
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("Erro de Treino")
        msg_box.setInformativeText(mensagem)
        msg_box.setWindowTitle("Erro")
        msg_box.exec()

    def exibir_mensagem_sucesso(self, mensagem):
        """
        Exibe uma mensagem de sucesso.
        :param mensagem: A mensagem de sucesso a ser exibida.
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Operação realizada!")
        msg_box.setInformativeText(mensagem)
        msg_box.setWindowTitle("Sucesso")
        msg_box.exec()

    def buscar_treino_executado(self):
        """
        Busca o treino executado na data selecionada e preenche a tabela correspondente.
        """
        print("1 buscar_treino_executado() executed")
        data_selecionada = self.dateEdit.dateTime().toPyDateTime()  # Obtém a data selecionada como um objeto datetime
        print("2 buscar_treino_executado() executed")
        try:
            treino_executado = f.listarTreinoExecutadoNaData(f.pessoaLogada, data_selecionada)
            print("3 buscar_treino_executado() executed")
            self.preenche_tabela_treino_executado(treino_executado)
            print("4 buscar_treino_executado() executed")
        except DataInvalidaException:
            self.exibir_mensagem_erro("Data inválida!")
        except ObjetoNaoCadastradaException as e:
            self.exibir_mensagem_erro(str(e))
        except Exception as e:
            print("Exception:", e)
            traceback.print_exc()
            self.exibir_mensagem_erro("Ocorreu um erro ao buscar o treino executado.")

    def preenche_tabela_treino_executado(self, treino_executado):
        """
        Preenche a tabela com os exercícios do treino executado.
        :param treino_executado: O treino executado a ser exibido na tabela.
        """
        self.modeloTabelaTreinoExecutado.clear()  # Limpa o modelo de dados atual

        if treino_executado:
            for exercicio in treino_executado.treino.exercicios:
                nome_item = QStandardItem(exercicio.nome)
                serie_item = QStandardItem(str(exercicio.serie))
                repeticao_item = QStandardItem(str(exercicio.repeticao))

                # Definir o alinhamento dos dados como centralizado
                nome_item.setTextAlignment(Qt.AlignCenter)
                serie_item.setTextAlignment(Qt.AlignCenter)
                repeticao_item.setTextAlignment(Qt.AlignCenter)

                self.modeloTabelaTreinoExecutado.appendRow([nome_item, serie_item, repeticao_item])

            self.configurar_tabela_treino_executado()

    def configurar_tabela_treino_executado(self):
        """
        Configura a tabela do treino executado com o modelo de dados e ajusta o redimensionamento das colunas e linhas.
        """
        self.tabelaTreinoExecutado.setModel(self.modeloTabelaTreinoExecutado)

        self.tabelaTreinoExecutado.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabelaTreinoExecutado.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
