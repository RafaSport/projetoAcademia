from .pessoa import Pessoa


class Gerente(Pessoa):
    def __init__(self, nome, cpf, email, nascimento, senha, pin):
        super().__init__(nome, cpf, email, nascimento, senha)
        self.__pin = pin

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, other):
        self.__pin = other

    def __eq__(self, other):
        return super().__eq__(other)

    def __str__(self):
        return super().__str__()