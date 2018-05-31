# /**************************************************************
# ** Universidad del Valle de Guatemala                        **
# ** Bases de Datos                                            **
# ** María MercedesRetolaza Reyna                              **
# ** Carne: 16339                                              **
# ** Fecha: 28/05/2018                                         **
# ***************************************************************/

# Nota importante: Customer debe tener una referencia obtenida de Employee para support id

import psycopg2
from faker import Faker
fake = Faker()
from random import randint
import random
import string


def retrieve_last_employee():
    conn = psycopg2.connect("dbname="" user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Employee"'
    name = '"EmployeeId"'
    query = "SELECT" + name + "from" + concat + "ORDER BY" + name + " desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(', '')
    clean = clean.replace(',', '')
    clean = clean.replace(')', '')
    conn.commit()
    conn.close()
    return clean


def insert_employees():
    conn = psycopg2.connect("dbname="" user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Employee"'
    field1 = '"EmployeeId"'
    field2 = '"LastName"'
    field3 = '"FirstName"'
    field4 = '"Title"'

    # Del diagrama ER parece que ReportsTo es sobre EmployeeId
    field5 = '"ReportsTo"'
    field6 = '"BirthDate"'
    field7 = '"HireDate"'
    field8 = '"Address"'
    field9 = '"City"'
    field10 = '"State"'
    field11 = '"Country"'
    field12 = '"PostalCode"'
    field13 = '"Phone"'
    field14 = '"Fax"'
    field15 = '"Email"'

    firstlastname = str.split(fake.name())
    first_name = "'" + str(firstlastname[0]) + "'"
    last_name = "'" + str(firstlastname[1]) + "'"
    employee_pos = int(retrieve_last_employee()) + 1
    employee_pos = str(employee_pos)
    title_list = ['Sales Support Agent', 'IT Staff']
    title_pick = randint(0, len(title_list) - 1)
    final_title = "'" + title_list[title_pick] + "'"
    if (title_pick == 0):
        reports_to = 2
    else:
        reports_to = 6
    reports_to = "'" + str(reports_to) + "'"
    birth_year = str(randint(1960, 1990))
    birth_month = str(randint(1, 12))
    birth_day = str(randint(1, 31))
    whole_birth = "'" + birth_year + "-" + birth_month + "-" + birth_day + "'"
    employed_year = str(randint(2008, 2017))
    employed_month = str(randint(1, 11))
    employed_day = str(randint(1, 30))
    whole_employed = "'" + employed_year + "-" + employed_month + "-" + employed_day + "'"
    adress = fake.address()
    adress = "'" + adress + "'"
    cities = ['Stuttgart', 'Palooza', 'Guatemala City']
    city_pick = randint(0, len(cities) - 1)
    city_pos = "'" + cities[city_pick] + "'"
    states = ['az', 'ar', 'kl', 'ta']
    state_pick = randint(0, len(states) - 1)
    state_pos = "'" + states[state_pick] + "'"
    country_list = ['Germany', 'Guatemala', 'France', 'England', 'USA']
    country_pick = randint(0, len(country_list) - 1)
    country = "'" + country_list[country_pick] + "'"
    postal_letter1 = str(random.choice(string.ascii_letters))
    postal_letter2 = str(randint(1, 8))
    postal_letter3 = str(random.choice(string.ascii_letters))
    postal_letter4 = str(random.choice(string.ascii_letters))
    postal_letter5 = str(randint(1, 8))
    postal_letter6 = str(random.choice(string.ascii_letters))
    postal_code = "'" + postal_letter1 + postal_letter2 + postal_letter3 + " " + postal_letter4 + postal_letter5 + postal_letter6 + "'"
    phone_field1 = "+502 "
    phone_field2 = str(randint(11111111, 99999998))
    phone = "'" + phone_field1 + phone_field2 + "'"
    fax_field1 = "1(780)"
    fax_field2 = str(randint(100, 998))
    fax_field3 = str(randint(1000, 9998))
    fax = "'" + fax_field1 + fax_field2 + "-" + fax_field3 + "'"
    name = fake.name().replace(" ", "")
    email = "'" + name + "@gmail.com" + "'"
    query = "INSERT INTO " + concat + "(" + field1 + "," + field2 + "," + field3 + "," + field4 + "," + field5 + "," + field6 + "," + field7 + "," + field8 + "," + field9 + "," + field10 + "," + field11 + "," + field12 + "," + field13 + "," + field14 + "," + field15 + ")" + " values(" + employee_pos + "," + last_name + "," + first_name + "," + final_title + "," + reports_to + "," + whole_birth + "," + whole_employed + "," + adress + "," + city_pos + "," + state_pos + "," + country + "," + postal_code + "," + phone + "," + fax + "," + email + ");"
    cur.execute(query)
    print("\nInsercion hecha con exito\n")
    conn.commit()
    conn.close()


insert_employees()
