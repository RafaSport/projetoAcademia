from model.aluno import Aluno
from model.professor import Professor


class RepositorioPessoa:
    """
    classe que usa opadrão Singleton e cria uma lista de pessoas e faz as operações de CRUD
    """
    __instance = None

    @staticmethod
    def get_instance():
        if not RepositorioPessoa.__instance:
            RepositorioPessoa.__instance = RepositorioPessoa()
        return RepositorioPessoa.__instance

    def __init__(self):
        self.__listaPessoas = []


    def adicionar(self, objeto):
        self.__listaPessoas.append(objeto)


    def remover(self, objeto):
        self.__listaPessoas.remove(objeto)

    def alterar(self, atual, novo):
        self.__listaPessoas.remove(atual)
        self.__listaPessoas.append(novo)

    def consultar(self, cpf):
        pessoaConsultada = None
        for p in self.__listaPessoas:
            if p.cpf == cpf:
                pessoaConsultada = p
                break
        return pessoaConsultada

    def listarAlunos(self):
        lista = []
        for p in self.__listaPessoas:
            if isinstance(p, Aluno):
                lista.append(p)
        return lista

    def listarProfessor(self):
        lista = []
        for p in self.__listaPessoas:
            if isinstance(p, Professor):
                lista.append(p)
        return lista

    def listarTodos(self):
        return self.__listaPessoas