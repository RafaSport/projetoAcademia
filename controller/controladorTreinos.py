from model.aluno import Aluno
from model.treino import Treino
from copy import deepcopy
from datetime import datetime
from utilidades import uteis
from exception.excecoes import ObjetoJaCadastradaException, ObjetoNaoCadastradaException


class ControladorTreinos:

    __instance = None

    @staticmethod
    def get_instance():
        if not ControladorTreinos.__instance:
            ControladorTreinos.__instance = ControladorTreinos()
        return ControladorTreinos.__instance

    def cadastraExerciciosNumTreino(self, listaExercicios):
        treino = Treino()
        treino.exercicios = deepcopy(listaExercicios)

        return treino


    def cadastrarTreinosParaAluno(self, aluno: Aluno, treino_A, treino_B, treino_C):
        aluno.planoTreino.treinos.clear()
        aluno.planoTreino.treinos.append(treino_A)
        aluno.planoTreino.treinos.append(treino_B)
        aluno.planoTreino.treinos.append(treino_C)



    def alterarTreino(self, aluno: Aluno, posicao, treinoNovo):
        aluno.planoTreino.treinos.pop(posicao)
        aluno.planoTreino.treinos.insert(posicao, treinoNovo)


    def consultarTreinos(self, aluno: Aluno):
        return aluno.planoTreino.treinos


    def consultarTreinoDeHoje(self, aluno: Aluno):
        """
        Consulta o treino de hoje do aluno retornando o treino do dia
        :param aluno:
        :return:
        """
        indice = uteis.diaDaSemanaParaIndice(datetime.now()) # retorna o indice corespondente de hoje

        if indice != -1:
            if len(aluno.planoTreino.treinos) > 0:
                return aluno.planoTreino.treinos[indice]
            else:
                raise ObjetoNaoCadastradaException('Treino não cadastrado!')
        else:
            raise ObjetoNaoCadastradaException('Hoje não tem treino cadastrado!')