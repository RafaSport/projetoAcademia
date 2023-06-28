from PyQt5.QtWidgets import QApplication
from view.telaLogin import TelaLogin
from model.aluno import Aluno
from model.gerente import Gerente
from model.professor import Professor
from model.exercicio import Exercicio
from model.treino import Treino
from model.planoTreino import PlanoTreino
from datetime import datetime
from fachada.fachada import Fachada


f = Fachada.get_instance()


a1 = Aluno('Rafa', '1111', 'rafa@gmail.com', datetime(1985, 10, 10),'1234', '0001')

ex1 = Exercicio('barra', 3, 8)
ex2 = Exercicio('esteira', 1, 1)
ex3 = Exercicio('abdominal', 3, 20)
ex4 = Exercicio('bicicleta', 1, 1)
ex5 = Exercicio('agachamento', 3, 15)

treinoA = Treino()
lista1 = []
lista1.append(ex1)
lista1.append(ex2)
lista1.append(ex3)

treinoA = f.cadastraExerciciosNumTreino(lista1)

treinoB = Treino()
lista2 = []
lista2.append(ex4)
lista2.append(ex5)
lista2.append(ex2)

treinoB = f.cadastraExerciciosNumTreino(lista2)

treinoC = Treino()
lista3 = []
lista3.append(ex3)
lista3.append(ex1)
lista3.append(ex5)

treinoC = f.cadastraExerciciosNumTreino(lista3)

f.cadastrarTreinosParaAluno(a1, treinoA, treinoB, treinoC)


g1 = Gerente('Bob', '2222', 'bob@gmail.com', datetime(1995, 5, 15), '0000', '0002')
p1 = Professor('Poli', '3333', 'poli@gmail.com', datetime(2004, 6, 14), '9999', '007', 2555.50)

f.cadastrarPessoa(a1)
f.cadastrarPessoa(g1)
f.cadastrarPessoa(p1)


if __name__ == "__main__":

    app = QApplication([])
    tela_login = TelaLogin()
    tela_login.show()
    app.exec_()

