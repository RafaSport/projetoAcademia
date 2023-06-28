from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.uic import loadUi
from fachada.fachada import Fachada


f = Fachada.get_instance()


class TelaAluno(QMainWindow):
    """
    Classe que recebe como parametro a tela anterior na navegação, ou seja, a tela de login
    """
    def __init__(self, tela_login):
        super().__init__()

        loadUi("../view/TelaAluno.ui", self)
        self.tela_anterior = tela_login  # Armazena a referência da tela_login

        self.lblNome.setText(f.pessoaLogada.nome)
        self.btnSair.clicked.connect(self.sair_do_sistema)


        # Criar o modelo de dados da tabela
        self.modeloTabela = QStandardItemModel()
        self.modeloTabela.setColumnCount(3)
        self.modeloTabela.setHorizontalHeaderLabels(["Nome", "Série", "Duração"])

        treino = f.consultarTreinoDeHoje(f.pessoaLogada)

        self.preenche_tabela_exercicios(treino)



    def preenche_tabela_exercicios(self, treino):
        """
        Recebe o treino do dia do aluno e preenche a tabela
        :param treino:
        :return: a tabela preenchida com o treino no dia
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

        # Configurar a tabela com o modelo de dados
        self.tabelaExercicios.setModel(self.modeloTabela)

        # Ajustar o redimensionamento automático das colunas
        self.tabelaExercicios.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Ajustar o redimensionamento automático das linhas
        self.tabelaExercicios.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def sair_do_sistema(self):

        f.pessoaLogada = None

        self.abrir_tela_login()

    def abrir_tela_login(self):
        self.hide()  # Esconde a tela atual
        self.tela_anterior.limpar_tela()
        self.tela_anterior.show()
