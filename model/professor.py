from .pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, cpf, email, nascimento, senha, id, salario):
        super().__init__(nome, cpf, email, nascimento, senha)
        self.__id = id
        self.__salario = salario

    @property
    def id(self):
        return self.__id

    @property
    def salario(self):
        return self.__salario

    @id.setter
    def id(self, other):
        self.__id = other

    @salario.setter
    def salario(self, other):
        self.__salario = other

    def __eq__(self, other):
        return super().__eq__(other)

    def __str__(self):
        return super().__str__() + f'\nID: {self.__id}\nSalario: {self.__salario}'
