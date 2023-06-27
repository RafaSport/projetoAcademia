from PyQt5.QtWidgets import QApplication
from view.telaLogin import TelaLogin
from model.aluno import Aluno
from model.gerente import Gerente
from model.professor import Professor
from datetime import datetime
import fachada.fachada


a1 = Aluno('Rafa', '1111', 'rafa@gmail.com', datetime(1985, 10, 10),'1234', '0001')
g1 = Gerente('Bob', '2222', 'bob@gmail.com', datetime(1995, 5, 15), '0000', '0002')
p1 = Professor('Poli', '3333', 'poli@gmail.com', datetime(2004, 6, 14), '9999', '007', 2555.50)

f = fachada.fachada.Fachada.get_instance()

f.cadastrarPessoa(a1)
f.cadastrarPessoa(g1)
f.cadastrarPessoa(p1)


if __name__ == "__main__":

    app = QApplication([])
    tela_login = TelaLogin()
    tela_login.show()
    app.exec_()

