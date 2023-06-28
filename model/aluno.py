from datetime import datetime
from .pessoa import Pessoa
from .planoTreino import PlanoTreino


class Aluno(Pessoa):
    def __init__(self, nome=None, cpf=None, email=None, nascimento=None, senha=None, matricula=None):
        super().__init__(nome, cpf, email, nascimento, senha)
        self.__matricula = matricula
        self.__mesPago = datetime.now()
        self.__planoTreino = PlanoTreino()
        self.__treinosExecutados = []

    @property
    def planoTreino(self):
        return self.__planoTreino

    @property
    def treinosExecutados(self):
        return self.__treinosExecutados

    def adicinarTreinoExecutado(self, other):
        self.__treinosExecutados.append(other)

    @property
    def matricula(self):
        return self.__matricula

    @property
    def mesPago(self):
        return self.__mesPago

    @matricula.setter
    def matricula(self, outro):
        self.__matricula = outro

    @mesPago.setter
    def mesPago(self, outro):
        self.__mesPago = outro

    @planoTreino.setter
    def planoTreino(self, outro):
        self.__planoTreino = outro

    def __eq__(self, other):
        return super().__eq__(other)

    def __str__(self):
        return super().__str__() + f'\nMatricula: {self.__matricula}'
