# /**************************************************************
# ** Universidad del Valle de Guatemala                        **
# ** Bases de Datos                                            **
# ** María MercedesRetolaza Reyna                              **
# ** Carne: 16339                                              **
# ** Fecha: 28/05/2018                                         **
# ***************************************************************/

import psycopg2
from faker import Faker

fake = Faker()
from random import randint
import random
import string


def retrieve_last_customer():
    conn = psycopg2.connect("dbname="" user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Customer"'
    name = '"CustomerId"'
    query = "SELECT" + name + "from" + concat + "ORDER BY" + name + " desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(', '')
    clean = clean.replace(',', '')
    clean = clean.replace(')', '')
    # print(clean)
    conn.commit()
    conn.close()
    return clean


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
    # print(clean)
    conn.commit()
    conn.close()
    return clean


def insert_customers():
    conn = psycopg2.connect("dbname="" user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Customer"'
    field1 = '"CustomerId"'
    field2 = '"FirstName"'
    field3 = '"LastName"'
    field4 = '"Company"'
    field5 = '"Address"'
    field6 = '"City"'
    field7 = '"State"'
    field8 = '"Country"'
    field9 = '"PostalCode"'
    field10 = '"Phone"'
    field11 = '"Fax"'
    field12 = '"Email"'
    field13 = '"SupportRepId"'
    firstlastname = str.split(fake.name())
    first_name = "'" + str(firstlastname[0]) + "'"
    last_name = "'" + str(firstlastname[1]) + "'"
    customer_pos = int(retrieve_last_customer()) + 1
    customer_pos = str(customer_pos)
    company_list = ['Google', 'Microsoft', 'Apple', 'Blizzard']
    company_pick = randint(0, len(company_list) - 1)
    final_company = "'" + company_list[company_pick] + "'"
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
    employee = int(retrieve_last_employee())
    supp = str(randint(0, employee))
    query = "INSERT INTO " + concat + "(" + field1 + "," + field2 + "," + field3 + "," + field4 + "," + field5 + "," + field6 + "," + field7 + "," + field8 + "," + field9 + "," + field10 + "," + field11 + "," + field12 + "," + field13 + ")" + " values(" + customer_pos + "," + first_name + "," + last_name + "," + final_company + "," + adress + "," + city_pos + "," + state_pos + "," + country + "," + postal_code + "," + phone + "," + fax + "," + email + "," + supp + ");"
    cur.execute(query)
    print("\nInsercion hecha con exito\n")
    conn.commit()
    conn.close()


insert_customers()
