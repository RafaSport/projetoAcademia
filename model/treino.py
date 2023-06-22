class Treino:
    def __init__(self):
        self.__exercicios = []

    @property
    def exercicios(self):
        return self.__exercicios

    @exercicios.setter
    def exercicios(self, other):
        self.__exercicios = other
