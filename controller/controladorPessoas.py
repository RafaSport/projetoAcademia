from dados.repositorio import RepositorioPessoa
from exception.excecoes import ObjetoJaCadastradaException, ObjetoNaoCadastradaException
from datetime import datetime

class ControladorPessoa:
    """
        classe que usa o padrão Singleton e cria uma instancia do repositorio e faz
        as operações de CRUD do repositorio e demais regras do negocio
    """
    __instance = None

    @staticmethod
    def get_instance():
        if not ControladorPessoa.__instance:
            ControladorPessoa._instance = ControladorPessoa()
        return ControladorPessoa._instance

    def __init__(self):
        self.__repositorio = RepositorioPessoa().get_instance()


    def adicionar(self, pessoa):
        if not pessoa in self.__repositorio.listarTodos():
            self.__repositorio.adicionar(pessoa)
        else:
            raise ObjetoJaCadastradaException('Pessoa já cadastrada!')

    def remover(self, pessoa):
        if pessoa in self.__repositorio.listarTodos():
            self.__repositorio.remover(pessoa)
        else:
            raise ObjetoNaoCadastradaException('Pessoa não cadastrada!')

    def consultar(self, cpf):
        pessoaNaLista = False
        for p in self.__repositorio.listarTodos():
            if p.cpf == cpf:
                pessoaNaLista = True
                break

        if pessoaNaLista:
            return self.__repositorio.consultar(cpf)
        else:
            raise ObjetoNaoCadastradaException('Pessoa não cadastrada!')

    def alterar(self, atual, novo):
        if atual in self.__repositorio.listarTodos():
            self.__repositorio.alterar(atual, novo)
        else:
            raise ObjetoNaoCadastradaException('Pessoa não cadastrada!')

    def listarAlunos(self):
        return self.__repositorio.listarAlunos()

    def listarProfessores(self):
        return self.__repositorio.listarProfessor()

    def listarTodos(self):
        return self.__repositorio.listarTodos()

    def fazerLogin(self, email, senha):
        pessoaLogada = None
        for p in self.__repositorio.listarTodos():
            if p.email == email and p.senha == senha:
                pessoaLogada = p
                break

        if pessoaLogada is not None:
            return pessoaLogada
        else:
            raise ObjetoNaoCadastradaException('Pessoa não cadastrada!')

    
