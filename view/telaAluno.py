from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class TelaAluno(QMainWindow):
    """
    Classe que recebe como parametro a tela anterior na navegação, ou seja, a tela de login
    """
    def __init__(self, tela_login):
        super().__init__()

        from fachada.fachada import Fachada
        f = Fachada.get_instance()


        loadUi("../view/TelaAluno.ui", self)
        self.tela_anterior = tela_login  # Armazena a referência da tela_login

        self.lblNome.setText(f.pessoaLogada.nome)
        self.btnSair.clicked.connect(self.sair_do_sistema)

    def sair_do_sistema(self):

        from fachada.fachada import Fachada
        f = Fachada.get_instance()

        f.pessoaLogada = None

        self.abrir_tela_login()

    def abrir_tela_login(self):
        self.hide()  # Esconde a tela atual
        self.tela_anterior.limpar_tela()
        self.tela_anterior.show()