from model.aluno import Aluno
from model.treino import Treino
from copy import deepcopy
from datetime import datetime

from model.treinoExecutado import TreinoExecutado
from utilidades import uteis
from exception.excecoes import ObjetoJaCadastradaException, ObjetoNaoCadastradaException, DataInvalidaException

class ControladorTreinosExecutados:
    __instance = None

    @staticmethod
    def get_instance():
        if not ControladorTreinosExecutados.__instance:
            ControladorTreinosExecutados.__instance = ControladorTreinosExecutados()
        return ControladorTreinosExecutados.__instance

    def listarTreinoExecutadoNaData(self, aluno: Aluno, data):
        """
        Lista o treino executado pelo aluno em uma data específica.

        :param aluno: objeto Aluno do qual será listado o treino executado
        :param data: objeto datetime contendo a data desejada
        :return: objeto Treino executado na data especificada
        :raises DataInvalidaException: se a data fornecida for inválida (posterior à data atual)
        :raises ObjetoNaoCadastradaException: se não houver treino executado na data especificada
        """
        treinoExecutado = None
        if uteis.verificar_data_valida(data) and data <= datetime.now():
            for t in aluno.treinosExecutados:
                if t.data == data:
                    treinoExecutado = t
                    break
            if treinoExecutado:
                return treinoExecutado
            else:
                raise ObjetoNaoCadastradaException('Treino não cadastrado!')
        else:
            raise DataInvalidaException()

    def salvarTreinoExecutado(self, aluno: Aluno, treino_executado: TreinoExecutado):
        """
        Salva o treino do aluno.
        Args:
            aluno (Aluno): O objeto Aluno.
            treino_executado (TreinoExecutado): O objeto TreinoExecutado a ser salvo.
        Raises:
            ObjetoJaCadastradaException: Se o treino_executado já estiver cadastrado para o aluno.
        """
        if treino_executado in aluno.treinosExecutados:
            raise ObjetoJaCadastradaException('Treino já cadastrado!')

        aluno.treinosExecutados.append(treino_executado)