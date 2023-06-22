class Exercicio:
    def __init__(self, nome, serie, repeticao):
        self.__nome = nome
        self.__serie = serie
        self.__repeticao = repeticao

    @property
    def nome(self):
        return self.__nome

    @property
    def serie(self):
        return self.__serie

    @property
    def repeticao(self):
        return self.__repeticao

    @nome.setter
    def nome(self, other):
        self.__nome = other

    @serie.setter
    def serie(self, other):
        self.__serie = other

    @repeticao.setter
    def repeticao(self, other):
        self.__repeticao = other
