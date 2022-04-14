import mysql.connector

my_database = mysql.connector.connect(host="localhost", user="root", password="", database="padb")
my_cursor = my_database.cursor()

sql = "INSERT INTO atividade_um VALUES (%s, %s, %s)"
val = [(1, "Antônio", 20), (2, "José", 35), (3, "Lucas", 15)]
my_cursor.executemany(sql, val)
my_database.commit()

print(f'No total, {my_cursor.rowcount} linhas foram afetadas')
