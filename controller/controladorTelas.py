"""
from view.telaAluno import TelaAluno
from view.telaGerenteInicial import TelaGerenteInicial
from view.telaProfessorInicial import TelaProfessorInicial


class ControladorTelas:
    __instance = None

    @staticmethod
    def get_instance():
        if not ControladorTelas.__instance:
            ControladorTelas.__instance = ControladorTelas()
        return ControladorTelas.__instance

    def __init__(self):
        self.__tela_aluno = None
        self.__tela_gerente = None
        self.__tela_professor = None

    def abrir_tela_aluno(self, tela_anterior):
        self.__tela_aluno = TelaAluno(tela_anterior)
        tela_anterior.hide()
        self.__tela_aluno.show()

    def abrir_tela_gerente(self, tela_anterior):
        self.__tela_gerente = TelaGerenteInicial(tela_anterior)
        tela_anterior.hide()
        self.__tela_gerente.show()

    def abrir_tela_professor(self, tela_anterior):
        self.__tela_professor = TelaProfessorInicial(tela_anterior)
        tela_anterior.hide()
        self.__tela_professor.show()


# Exemplo de uso:
#controlador_telas = ControladorTelas()
#controlador_telas.iniciar()
"""