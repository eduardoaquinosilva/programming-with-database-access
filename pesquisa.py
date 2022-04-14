import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets

database = mysql.connector.connect(host="localhost", user="root", password="", database="empresa")
cursor = database.cursor()


class Ui_Pesquisa(object):
    def setupUi(self, Pesquisa):
        Pesquisa.setObjectName("Pesquisa")
        Pesquisa.resize(465, 539)

        self.centralwidget = QtWidgets.QWidget(Pesquisa)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.lb_nome = QtWidgets.QLabel(self.centralwidget)
        self.lb_nome.setObjectName("lb_nome")

        self.gridLayout.addWidget(self.lb_nome, 0, 0, 1, 1)

        self.le_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.le_nome.setObjectName("le_nome")

        self.gridLayout.addWidget(self.le_nome, 0, 1, 1, 1)

        self.btn_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pesquisar.setObjectName("btn_pesquisar")
        self.btn_pesquisar.clicked.connect(self.pesquisar)

        self.gridLayout.addWidget(self.btn_pesquisar, 1, 1, 1, 1)

        self.te_listagem = QtWidgets.QTextEdit(self.centralwidget)
        self.te_listagem.setObjectName("te_listagem")

        self.gridLayout.addWidget(self.te_listagem, 2, 1, 1, 1)
        Pesquisa.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pesquisa)
        QtCore.QMetaObject.connectSlotsByName(Pesquisa)

    def retranslateUi(self, Pesquisa):
        _translate = QtCore.QCoreApplication.translate
        Pesquisa.setWindowTitle(_translate("Pesquisa", "Pesquisa de Clientes"))
        self.lb_nome.setText(_translate("Pesquisa", "Nome:"))
        self.btn_pesquisar.setText(_translate("Pesquisa", "Pesquisar"))

    def pesquisar(self):
        nome = self.le_nome.text()
        sql = f"SELECT * FROM cliente WHERE nome LIKE %s"
        cursor.execute(sql, (f"%{nome}%", ) )
        dados = cursor.fetchall()
        qtd = len(dados)
        resultado = ''

        if qtd > 0:
            for a in dados:
                resultado += f"Código: {str(a[0])}\n"
                resultado += "Nome: " + a[1] + "\n"
                resultado += "E-mail: " + a[2] + "\n"
                resultado += "Telefone: " + str(a[3]) + "\n"
                resultado += "========================================\n"
        resultado += f'{str(qtd)} registros encontrados.'
        self.te_listagem.setPlainText(resultado)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela = QtWidgets.QMainWindow()
    ui = Ui_Pesquisa()
    ui.setupUi(janela)
    janela.show()
    sys.exit(app.exec_())
