import csv
import cx_Oracle

def get_year_count(cursor, olimpic_year):
    cursor.execute("SELECT * FROM Olimpiada WHERE olimp_year=:value", value=olimpic_year)
    records = cursor.fetchall()
    return len(records)

def add_year(cursor, olimpic_city, olimpic_year):
    if get_year_count(cursor, olimpic_year) == 0:
        cursor.execute("INSERT INTO Olimpiada(olimp_year) VALUES(:value)", value=olimpic_year)
        cursor.execute("INSERT INTO Cities(city_name, olimpiada_olimp_year) VALUES(:value1, :value2)", value1=olimpic_city, value2=olimpic_year)

def get_medal_count(cursor, medal_color):
    cursor.execute("SELECT * FROM Medal WHERE color=:value", value=medal_color)
    records = cursor.fetchall()
    return len(records)

def add_medal(cursor, medal_color):
    if get_medal_count(cursor, medal_color) == 0:
        cursor.execute("INSERT INTO Medal(color) VALUES(:value)", value=medal_color)

def get_sport_category_count(cursor, sport_category):
    cursor.execute("SELECT * FROM SportCategory WHERE category_name=:value", value=sport_category)
    records = cursor.fetchall()
    return len(records)

def add_sport_category(cursor, sport_category):
    if get_sport_category_count(cursor, sport_category) == 0:
        cursor.execute("INSERT INTO SportCategory(category_name) VALUES (:value)", value=sport_category)

def get_sport_disciplina_count(cursor, sport_disciplina):
    cursor.execute("SELECT * FROM Disciplina WHERE disc_name=:value", value=sport_disciplina)
    records = cursor.fetchall()
    return len(records)

def add_sport_disciplina(cursor, sport_disciplina):
    if get_sport_disciplina_count(cursor, sport_disciplina) == 0:
        cursor.execute("INSERT INTO Disciplina(disc_name) VALUES (:value)", value=sport_disciplina)

def get_sport_event_count(cursor, sport_event):
    cursor.execute("SELECT * FROM Event WHERE event_name=:value", value=sport_event)
    records = cursor.fetchall()
    return len(records)

def add_sport_event(cursor, sport_event):
    if get_sport_event_count(cursor, sport_event) == 0:
        cursor.execute("INSERT INTO Event(event_name) VALUES (:value)", value=sport_event)

def get_category_count(cursor, sport_category, sport_disciplina):
    cursor.execute("SELECT * FROM Category WHERE (sportcategory_category_name=:value1) AND (disciplina_disc_name=:value2)", value1=sport_category, value2=sport_disciplina)
    records = cursor.fetchall()
    return len(records)

def add_sport(cursor, sport_category, sport_disciplina, sport_event):
    add_sport_category(cursor, sport_category)
    add_sport_disciplina(cursor, sport_disciplina)
    add_sport_event(cursor, sport_event)
    if get_category_count(cursor, sport_category, sport_disciplina) == 0:
        cursor.execute(
            "INSERT INTO Category(sportcategory_category_name, disciplina_disc_name) VALUES (:value1, :value2)",
            value1=sport_category, value2=sport_disciplina)

def get_country_count(cursor, country_name):
    cursor.execute("SELECT * FROM Country WHERE (country_name=:value)", value=country_name)
    records = cursor.fetchall()
    return len(records)

def add_country(cursor, country_name):
    if get_country_count(cursor, country_name) == 0:
        cursor.execute("INSERT INTO Country(country_name) VALUES (:value)", value=country_name)

def get_athlete_count(cursor, athlete_name):
    cursor.execute("SELECT * FROM Athlete WHERE (athlete_name=:value)", value=athlete_name)
    records = cursor.fetchall()
    return len(records)

def add_athlete(cursor, athlete_name, athlete_gender, country_name):
    add_country(cursor, country_name)
    if get_athlete_count(cursor, athlete_name) == 0:
        cursor.execute("INSERT INTO Athlete(athlete_name, gender, country_name) VALUES (:value1, :value2, :value3)", value1=athlete_name, value2=athlete_gender, value3=country_name)

def get_grant_medal_count(cursor, olimp_year, sport_disciplina, sport_event, athlete_name, medal_color):
    cursor.execute('''SELECT * FROM GrantMedal WHERE (disciplina_name=:value1) AND (event_name=:value2) AND (athlete_name=:value3) AND (olimpiada_year=:value4) AND (medal_color=:value5)''', value1=sport_disciplina, value2=sport_event, value3=athlete_name, value4=olimp_year, value5=medal_color)
    records = cursor.fetchall()
    return len(records)

def grant_medal(cursor, olimp_year, sport_disciplina, sport_event, athlete_name, medal_color):
    if get_grant_medal_count(cursor, olimp_year, sport_disciplina, sport_event, athlete_name, medal_color) == 0:
        cursor.execute(
            '''INSERT INTO GrantMedal (disciplina_name, event_name, athlete_name, olimpiada_year, medal_color) VALUES (:value1, :value2, :value3, :value4, :value5)''',
            value1=sport_disciplina, value2=sport_event, value3=athlete_name, value4=olimp_year, value5=medal_color)

connection = cx_Oracle.connect("AristovaI", "AristovaI", "localhost/xe")
cursor = connection.cursor()
file = open("olimpiada.csv", errors='ignore',encoding='ascii')
read_csv = csv.reader(file, delimiter=",")
# City,Year,Sport,Discipline,Event,Athlete,Gender,Country_Code,Country,Event_gender,Medal
try:
    num = 0
    for r in read_csv:
        num += 1
        if num == 1:
            continue
        if r[0] == "":
            continue
        add_year(cursor, r[0], int(r[1])) # add olimp_year and city
        add_medal(cursor, r[10]) # add medal
        add_sport(cursor, r[2], r[3], r[4])  # add sport_category, disciplina, event
        add_athlete(cursor, r[5], r[6], r[8]) # add athlete, country
        grant_medal(cursor, int(r[1]), r[3], r[4], r[5], r[10])
except:
    print(f'Error of the row {num}')
    raise
file.close()
cursor.close()
connection.commit()
connection.close()