import mysql.connector
my_database = mysql.connector.connect(host="localhost", user="root", password="", database="teste_aula_pyqt")
cursor = my_database.cursor()
