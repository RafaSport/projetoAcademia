from model.aluno import Aluno
from model.treino import Treino
from copy import deepcopy
from datetime import datetime
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
