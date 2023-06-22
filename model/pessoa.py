from utilidades import uteis
from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome, cpf, email, nascimento, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__nascimento = nascimento
        self.__senha = senha


    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def email(self):
        return self.__email

    @property
    def nascimento(self):
        return uteis.data_para_string(self.__nascimento)

    @property
    def senha(self):
        return self.__senha

    @nome.setter
    def nome(self, outro):
        self.__nome = outro

    @cpf.setter
    def cpf(self, outro):
        self.__cpf = outro

    @email.setter
    def email(self, outro):
        self.__email = outro

    @nascimento.setter
    def nascimento(self, outro):
        self.__nascimento = outro

    @senha.setter
    def senha(self, outro):
        self.__senha = outro

    def __str__(self):
        return f'Nome: {self.__nome}\nEmail: {self.__email}' \
               f'\nNascimento: {uteis.data_para_string(self.__nascimento)}' \
               f'\nIdade: {uteis.calcular_idade(self.__nascimento)}'

    def __eq__(self, other):
        return self.__email == other.email or self.__cpf == other.cpf
