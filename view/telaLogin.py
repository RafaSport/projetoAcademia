from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from fachada.fachada import Fachada
from exception.excecoes import ObjetoNaoCadastradaException


"""
A classe Fachada está implementada com façade e singleton e coordena as ações dos controladores
Além de ter um atributo pessoaLogada que recebe a pessoa que efetuou o login no sistema
"""
fachada = Fachada.get_instance()


class TelaLogin(QMainWindow):
    """
    A classe login é responsável por receber o email e senha do usuario e atraves do metodo fazerLogin
    da fachada dar acesso as telas correspondentes de cada usuario a saber: aluno, professor e gerente,
    caso as informações estejam corretas e caso contrario lança um alerta de erro
    """
    def __init__(self):
        super().__init__()
        loadUi("../view/TelaLogin.ui", self)
        self.btnEntrar.clicked.connect(self.efetuar_login) # evento quando clica no botão entrar
        self.lineEmail.returnPressed.connect(self.efetuar_login)#evento quando aperta a tecla enter do teclado
        self.lineSenha.returnPressed.connect(self.efetuar_login)#evento quando aperta a tecla enter do teclado
        self.tela_aluno = None
        self.tela_gerente = None
        self.tela_professor = None

    def efetuar_login(self):
        """
        Metodo que recebe as informações do usuario e tenta fazer o login e quado tem sucesso atribui
        ao atributo pessoaLogada da Fachada e abre a tela conforme o usuario
        :return: a tela correspondente do usuario logado ou alerta de erro
        """
        email = self.lineEmail.text()
        senha = self.lineSenha.text()

        try:
            # Metodo fazerLogin busca no repositorio uma pessoa com o email e senha fornecidos e uma vez
            # encontrando retorna a pessoa que apos é atribuida ao atributo pessoaLogada da fachada
            pessoa_logada = fachada.fazerLogin(email, senha)
            fachada.pessoaLogada = pessoa_logada

            # Metodo abre a tela inicial de cada tipo de pessoa verificando internamente
            # atraves do atributo pessoaLogada qual o tipo de pessoa (aluno, professor ou gerente)
            fachada.abrir_tela_inicial(self)

        except ObjetoNaoCadastradaException as e:
            self.limpar_tela()
            self.exibir_mensagem_erro(str(e))


    def limpar_tela(self):
        self.lineEmail.setText('')  # Limpa o campo de e-mail
        self.lineSenha.setText('')  # Limpa o campo de senha

    def exibir_mensagem_erro(self, mensagem):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("Erro de Login")
        msg_box.setInformativeText(mensagem)
        msg_box.setWindowTitle("Erro")
        msg_box.exec()