class TreinoExecutado:
    def __init__(self, data, treino):
        self.__data = data.date()
        self.__treino = treino

    @property
    def data(self):
        return self.__data

    @property
    def treino(self):
        return self.__treino

    def __eq__(self, other):
        return self.__data == other.data