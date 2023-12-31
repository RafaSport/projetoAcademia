class PlanoTreino:
    def __init__(self, validade):
        self.__validade = validade
        self.__treinos = []

    @property
    def validade(self):
        return self.__validade

    @property
    def treinos(self):
        return self.__treinos

    @validade.setter
    def validade(self, other):
        self.__validade = other

    @treinos.setter
    def treinos(self, other):
        self.__treinos = other