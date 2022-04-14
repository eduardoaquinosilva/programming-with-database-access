import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets

database = mysql.connector.connect(host="localhost", user="root", password="", database="empresa")
cursor = database.cursor()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.btn_listar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_listar.setObjectName("btn_listar")
        self.btn_listar.clicked.connect(self.listar)

        self.verticalLayout.addWidget(self.btn_listar)

        self.te_listagem = QtWidgets.QTextEdit(self.centralwidget)
        self.te_listagem.setObjectName("te_listagem")

        self.verticalLayout.addWidget(self.te_listagem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listagem de Clientes"))
        self.btn_listar.setText(_translate("MainWindow", "Listar"))

    def listar(self):
        sql = "SELECT * FROM cliente"
        cursor.execute(sql)

        dados = cursor.fetchall()
        resultado = ""
        qtd = len(dados)
        for a in dados:
            resultado += "Código: " + str(a[0]) + "\n"
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
    ui = Ui_MainWindow()
    ui.setupUi(janela)
    janela.show()
    sys.exit(app.exec_())
