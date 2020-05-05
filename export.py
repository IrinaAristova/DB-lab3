import csv
import cx_Oracle

connection = cx_Oracle.connect("AristovaI", "AristovaI", "localhost/xe")
cursor = connection.cursor()
cursor.execute("DROP View ExportView")

cursor.execute('''CREATE VIEW ExportView AS

SELECT Cities.city_name, Olimpiada.olimp_year, Disciplina.disc_name, SportCategory.category_name, Event.event_name, Athlete.athlete_name, Athlete.gender, Country.country_name, Medal.color 
FROM GrantMedal gm

INNER JOIN Olimpiada ON Olimpiada.olimp_year=gm.Olimpiada_year
INNER JOIN Cities ON Cities.Olimpiada_olimp_year=Olimpiada.olimp_year
INNER JOIN Disciplina ON Disciplina.disc_name=gm.Disciplina_name
INNER JOIN Category ON Category.Disciplina_disc_name=Disciplina.disc_name
INNER JOIN SportCategory ON SportCategory.category_name=Category.SportCategory_category_name
INNER JOIN Event ON Event.event_name=gm.event_name
INNER JOIN Athlete ON Athlete.athlete_name=gm.athlete_name
INNER JOIN Country ON Country.country_name=Athlete.country_name
INNER JOIN Medal ON Medal.color=gm.medal_color
ORDER BY olimp_year''')


with open( + '.csv', 'w', newline='') as csv_file:
    file = open('export.csv', 'w', newline = '')
    writer = csv.writer(csv_file, delimiter=',')

    cursor.execute('SELECT * FROM ExportView')
    row = cursor.fetchone()
    while row:
        writer.writerow(row)
        row = cursor.fetchone()

writer.close()
file.close()
cursor.execute("DROP View ExportView")
cursor.close()
connection.close()
