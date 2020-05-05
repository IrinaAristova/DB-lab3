import csv
import cx_Oracle

connection = cx_Oracle.connect("AristovaI", "AristovaI", "localhost/xe")
cursor = connection.cursor()

tables = ["GrantMedal", "Athlete", "Olimpiada", "Cities", "Event", "Disciplina", "SportCategory", "Country", "Medal"]
for table in tables:
    with open(table + '.csv', 'w', newline = '') as csvfile:
        cursor.execute('SELECT * FROM ' + table)
        row = cursor.fetchone()
        writeCSV = csv.writer(csvfile, delimiter=',')

        while row:
            writeCSV.writerow(row)
            row = cursor.fetchone()

cursor.close()
connection.close()