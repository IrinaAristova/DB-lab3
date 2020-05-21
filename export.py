import csv
import cx_Oracle

def export_to_file(cursor, table):
    csv_file = open(table+'.csv', 'w', newline='')
    writer = csv.writer(csv_file, delimiter=',')
    query = 'SELECT * FROM ' + table
    cursor.execute(query)
    writer.writerow(tuple(map(lambda x: x[0], cursor.description)))
    row = cursor.fetchone()
    while row:
        writer.writerow(row)
        row = cursor.fetchone()
    csv_file.close()


connection = cx_Oracle.connect("AristovaI", "AristovaI", "localhost/xe")
cursor = connection.cursor()

export_to_file(cursor, 'Medal')
export_to_file(cursor, 'Event')
export_to_file(cursor, 'SportCategory')
export_to_file(cursor, 'Category')
export_to_file(cursor, 'Disciplina')
export_to_file(cursor, 'Country')
export_to_file(cursor, 'Athlete')
export_to_file(cursor, 'Olimpiada')
export_to_file(cursor, 'Cities')
export_to_file(cursor, 'GrantMedal')
cursor.close()
connection.close()
