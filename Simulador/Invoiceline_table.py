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
from random import randint, uniform
import random

count = 5


def retrieve_InvoiceLineIds():
    conn = psycopg2.connect("dbname="" user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"InvoiceLine"'
    name = '"InvoiceLineId"'
    query = "SELECT" + name + "from" + concat + "ORDER BY" + name + " desc;"
    cur.execute(query)
    rows = cur.fetchall()
    ids = []
    for i in range(0, len(rows)):
        clean = str(rows[i]).replace('(', '')
        clean = clean.replace(',', '')
        clean = clean.replace(')', '')
        ids.append(int(clean))
    conn.commit()
    conn.close()
    return ids


def retrieve_InvoiceIds():
    conn = psycopg2.connect("dbname="" user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Invoice"'
    name = '"InvoiceId"'
    query = "SELECT" + name + "from" + concat + "ORDER BY" + name + " desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    ids = []
    for i in range(0, len(rows)):
        clean = str(rows[i]).replace('(', '')
        clean = clean.replace(',', '')
        clean = clean.replace(')', '')
        ids.append(int(clean))
    conn.commit()
    conn.close()
    return ids


def retrieve_TrackIds():
    conn = psycopg2.connect("dbname="" user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Track"'
    name = '"TrackId"'
    query = "SELECT" + name + "from" + concat + "ORDER BY" + name + " desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    ids = []
    for i in range(0, len(rows)):
        clean = str(rows[i]).replace('(', '')
        clean = clean.replace(',', '')
        clean = clean.replace(')', '')
        ids.append(int(clean))
    conn.commit()
    conn.close()
    return ids


def Insert_saleLine():
    conn = psycopg2.connect("dbname="" user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"InvoiceLine"'
    fields = ['"InvoiceLineId"', '"InvoiceId"', '"TrackId"', '"UnitPrice"', '"Quantity"']

    # get ultimo id
    id_invoiceline_last = retrieve_InvoiceLineIds()[0]
    # get array con los ids existentes de Invoice
    ids_invoice = retrieve_InvoiceIds()
    # get array con los ids existentes de Track
    ids_track = retrieve_TrackIds()

    # generar datos
    # invoice line id
    invoiceline_id = str(id_invoiceline_last + 1)
    # invoice id
    invoice_id = str(ids_invoice[randint(0, len(ids_invoice) - 1)])
    # track id
    track_id = str(ids_track[randint(0, len(ids_track) - 1)])
    # unit price
    unit_price = str(float(randint(0, 2)) + 0.99)
    # Quantity
    quantity = str(randint(1, 2))

    query = "INSERT INTO " + concat + "("
    for field in fields:
        query = query + field + ","
    # eliminar ultima coma
    query = query[:-1]
    query = query + ") VALUES ( " + invoiceline_id + ", " + invoice_id + ", " + track_id + ", " + unit_price + "," + quantity + ");"

    # hacer el query
    try:
        cur.execute(query)
        print("\nInsercion hecha con exito\n")
    except psycopg2.Error as e:
        print("\nERROR")

    conn.commit()
    conn.close()


def multi_insert(veces):
    i = 0
    alDia = randint(2, 4)
    invoiceLine_totales = veces * alDia
    while (i < invoiceLine_totales):
        Insert_saleLine()
        i = i + 1


multi_insert(100)
