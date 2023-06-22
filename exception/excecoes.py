
class ObjetoJaCadastradaException(Exception):
    def __init__(self, message="Objeto já cadastrado!"):
        super().__init__(message)


class ObjetoNaoCadastradaException(Exception):
    def __init__(self, message="Objeto não cadastrado!"):
        super().__init__(message)


class DataInvalidaException(Exception):
    def __init__(self, message="Data invalida!"):
        super().__init__(message)