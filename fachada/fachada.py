from controller.controladorPessoas import ControladorPessoa
from controller.controladorTreinos import ControladorTreinos
from controller.controladorTreinosExecutados import ControladorTreinosExecutados
from controller.controladorTelas import ControladorTelas
from model.aluno import Aluno
from model.professor import Professor
from model.gerente import Gerente


class Fachada:
    __instance = None

    @staticmethod
    def get_instance():
        if not Fachada.__instance:
            Fachada.__instance = Fachada()
        return Fachada.__instance

    def __init__(self):
        self.__controladorPessoa = ControladorPessoa.get_instance()
        self.__controladorTreino = ControladorTreinos.get_instance()
        self.__controladorTreinoExecutado = ControladorTreinosExecutados.get_instance()
        self.__controladorTelas = ControladorTelas.get_instance()

        self.__pessoaLogada = None

    @property
    def pessoaLogada(self):
        return self.__pessoaLogada

    @pessoaLogada.setter
    def pessoaLogada(self, pessoa):
        self.__pessoaLogada = pessoa

    @property
    def controladorPessoa(self):
        return self.__controladorPessoa

    @property
    def controladorTreino(self):
        return self.__controladorTreino

    @property
    def controladorTreinoExecutado(self):
        return self.__controladorTreinoExecutado

    @property
    def controladorTelas(self):
        return self.__controladorTelas

#------------------------------Controle de Pessoas-------------------------------------

    def cadastrarPessoa(self, pessoa):
        self.__controladorPessoa.adicionar(pessoa)

    def removerPessoa(self, pessoa):
        self.__controladorPessoa.remover(pessoa)

    def consultarPessoa(self, cpf):
        return self.__controladorPessoa.consultar(cpf)

    def atualizarPessoa(self, atual, novo):
        self.__controladorPessoa.alterar(atual, novo)

    def listarAlunos(self):
        return self.__controladorPessoa.listarAlunos()

    def listarProfessores(self):
        return self.__controladorPessoa.listarProfessores()

    def listarTodos(self):
        return self.__controladorPessoa.listarTodos()

    def fazerLogin(self, email, senha):
        return self.__controladorPessoa.fazerLogin(email, senha)


#------------------------------Controle de Treinos-------------------------------------



#--------------------------Controle de Treinos Executados------------------------------



#--------------------------------Controle de Telas-------------------------------------

    def abrir_tela_aluno(self, tela_anterior):
        self.__controladorTelas.abrir_tela_aluno(tela_anterior)

    def abrir_tela_professor(self, tela_anterior):
        self.__controladorTelas.abrir_tela_professor(tela_anterior)

    def abrir_tela_gerente(self, tela_anterior):
        self.__controladorTelas.abrir_tela_gerente(tela_anterior)

    def abrir_tela_inicial(self, tela_anterior):
        if isinstance(self.__pessoaLogada, Aluno):
            self.abrir_tela_aluno(tela_anterior)
        elif isinstance(self.__pessoaLogada, Gerente):
            self.abrir_tela_gerente(tela_anterior)
        elif isinstance(self.__pessoaLogada, Professor):
            self.abrir_tela_professor(tela_anterior)
