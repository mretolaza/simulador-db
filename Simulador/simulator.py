
# installation via pip install psycopg2, psycopg2-binary, termcolor, Faker

import sys, csv, psycopg2
from termcolor import cprint
from random import randint, uniform
from faker import Faker
from datetime import datetime
import psycopg2.extras
# Faker
fake = Faker('es_ES')

# csv generator
activity_logs = {}

# script params
print(len(sys.argv))
csv_name = './log_' + format(datetime.now()) if len(sys.argv) <= 2 else sys.argv[2]
action_times = int(sys.argv[1])

def increment_log(action):
    if action in activity_logs.keys():
        activity_logs[action] = activity_logs[action] + 1
    else:
        activity_logs[action] = 1

# csv generator
def csv_gen():
    with open(csv_name, 'w') as csvfile:
        fieldnames = ['action', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for key in activity_logs.keys():
            writer.writerow({'action': key, 'count': activity_logs[key]})

# psycopg2

def get_connection():
    try:
        conn = psycopg2.connect("dbname='mercedes' user='postgres' password=''")
        conn.autocommit=True
        return conn
    except:
        cprint ("Bad Connection Params.", 'red')
        sys.exit(1)

def select_rows(conn, fields, table, where, extra):
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    query = ""
    try:
        query = "SELECT " + fields + " FROM " + table
        if where is not None:
            query = query + " WHERE " + ' '.join(where)
        if extra is not None:
            query = query + " " + extra

        cprint(query, 'blue')
        cur.execute(query)
    except:
        cprint("Error: " + query, 'red')

    rows = cur.fetchall()
    cur.close()
    return rows

def insert(conn, table, fields, values):
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        placeholders = []
        for i in fields.split(","): placeholders.append("%s")
        query = 'INSERT INTO ' + table + ' (' + fields + ') VALUES ( ' + ','.join(placeholders) + ') RETURNING *'
        cur.execute(query, values)
        cprint(cur.query, "blue")
        return (cur.query, cur.fetchone())
    except Exception, e:
        cprint("Error: " + str(e), 'red')

# activities
connection = get_connection()

def new_client():
    cprint('new customer', 'green')
    supportId = select_rows(connection, '"EmployeeId"', '"Employee"', None, "ORDER BY random() LIMIT 1")[0]['EmployeeId']
    (query, item) = insert(connection, '"Customer"', ' "FirstName", "LastName", "Company", "Address", "City", "State", "Country", "PostalCode", "Phone", "Fax", "Email", "SupportRepId" ',
           [fake.first_name(),fake.last_name(), fake.company(),  fake.address(), fake.city(), fake.state() ,fake.country(), fake.postcode(), fake.phone_number(), fake.phone_number(), fake.email(), int(supportId) ])
    increment_log('new customer')


def new_track(album_default = None, genre_default = None):
    cprint('new track', 'green')
    album = album_default if album_default is not None else select_rows(connection, '"AlbumId"', '"Album"', None, "ORDER BY random() LIMIT 1")[0]['AlbumId']
    mediaType = select_rows(connection, '"MediaTypeId"', '"MediaType"', None, "ORDER BY random() LIMIT 1")[0]['MediaTypeId']
    genre = genre_default if genre_default is not None else select_rows(connection, '"GenreId"', '"Genre"', None, "ORDER BY random() LIMIT 1")[0]['GenreId']
    milis = long(uniform(1.5, 5) * 1000 * 60)
    byte = int(milis / 1024)
    insert(connection, '"Track"', ' "Name", "AlbumId", "MediaTypeId", "GenreId", "Composer", "Milliseconds", "Bytes", "UnitPrice" ',
           [fake.sentence(nb_words=randint(1,4)), album, mediaType, genre, fake.name(), milis, byte, round(uniform(.5,3), 2)])
    increment_log('new track')

def new_album(artistId_default = None):
    cprint('new album', 'green')
    artist = artistId_default if artistId_default is not None else select_rows(connection, '"ArtistId"', '"Artist"', None, 'ORDER BY random() LIMIT 1')[0]['ArtistId']
    (query , item) = insert(connection, '"Album"', ' "Title", "ArtistId" ', [fake.sentence(nb_words=randint(1,4)), artist])
    for i in range(2, 10):
        new_track(item['AlbumId'])
    increment_log('new album')

def new_order():
    cprint('new invoice', 'green')
    # get customer
    customer = select_rows(connection, '*', '"Customer"', None, "ORDER BY random() LIMIT 1")[0]
    tracks = select_rows(connection, '*', '"Track"', None, "ORDER BY random() LIMIT " + str(randint(1,10)))
    total = 0

    for t in tracks:
        t['Quantity'] = randint(1,5)
        total = total + float(t['UnitPrice']) * t['Quantity']

    state = customer['State'] if customer['State'] is not None else ''
    customer_id = customer['CustomerId'] if customer['CustomerId']is not None else ''
    address = customer['Address'] if customer['Address']is not None else ''
    city = customer['City'] if customer['City'] is not None else ''
    country = customer['Country'] if customer['Country']is not None else ''
    post_code = customer['PostalCode'] if customer['PostalCode'] is not None else ''

    (query, item) = insert(connection, '"Invoice"', ' "CustomerId", "InvoiceDate", "BillingAddress", "BillingCity", "BillingState", "BillingCountry", "BillingPostalCode", "Total" ',
               [customer_id, datetime.now(), address, city, state, country, post_code, total ])
    for t in tracks:
        insert(connection, '"InvoiceLine"', ' "InvoiceId", "TrackId", "UnitPrice", "Quantity" ',
               [item['InvoiceId'], t['TrackId'], t['UnitPrice'], t['Quantity']])
    increment_log('new invoice')

def new_artist():
    (query, item) = insert(connection, '"Artist"', '"Name"', [fake.name()])
    new_album(item['ArtistId'])
    increment_log('new artist')

def new_playlist():
    (query, item) = insert(connection, '"Playlist"', '"Name"', [fake.sentence(nb_words=randint(1,4))])
    tracks = select_rows(connection, '"TrackId"', '"Track"', None, "ORDER BY random() LIMIT " + str(randint(1,10)))
    for t in tracks:
        insert(connection, '"PlaylistTrack"', '"PlaylistId", "TrackId"', [item['PlaylistId'], t['TrackId']])
    increment_log('new playlist')

def new_genre():
    (query, item) = insert(connection, '"Genre"', '"Name"', [fake.sentence(nb_words=1)])
    new_track(genre_default=item['GenreId'])
    increment_log('new genre')

def random_activity_parser(activity):
    if activity == 0:
        new_track()
    elif activity == 1:
        new_client()
    elif activity == 2:
        new_album()
    elif activity == 3:
        new_artist()
    elif activity == 4:
        new_playlist()
    elif activity == 5:
        new_genre()
    else:
        new_order()



for action in range(0, action_times):
    random_activity_parser(randint(0, 7))

connection.close()
csv_gen()