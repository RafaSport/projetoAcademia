from controller.controladorPessoas import ControladorPessoa
from controller.controladorTreinos import ControladorTreinos
from controller.controladorTreinosExecutados import ControladorTreinosExecutados
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
        #self.__controladorTelas = ControladorTelas.get_instance()

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

    #@property
    #def controladorTelas(self):
    #    return self.__controladorTelas

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


    #Recebe uma pessoa e retorna o tipo da pessoa em forma de string
    def tipo_pessoa(self, pessoa):
        if isinstance(pessoa, Aluno):
            return 'aluno'
        elif isinstance(pessoa, Gerente):
            return 'gerente'
        elif isinstance(pessoa, Professor):
            return 'professor'


#------------------------------Controle de Treinos-------------------------------------
    def cadastraExerciciosNumTreino(self, listaExercicios):
        return self.__controladorTreino.cadastraExerciciosNumTreino(listaExercicios)

    def cadastrarTreinosParaAluno(self, aluno: Aluno, treino_A, treino_B, treino_C):
        self.__controladorTreino.cadastrarTreinosParaAluno(aluno, treino_A, treino_B, treino_C)

    def alterarTreino(self, aluno: Aluno, posicao, treinoNovo):
        self.__controladorTreino.alterarTreino(aluno, posicao, treinoNovo)

    def consultarTreinos(self, aluno: Aluno):
        return self.__controladorTreino.consultarTreinos(aluno)

    def consultarTreinoDeHoje(self, aluno: Aluno):
        return self.__controladorTreino.consultarTreinoDeHoje(aluno)



#--------------------------Controle de Treinos Executados------------------------------

