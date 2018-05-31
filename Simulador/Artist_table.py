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
pos_artist = "277"

# retrieve artist 
def retrieve_Artists():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Artist"'
    name = '"Name"'
    query = "SELECT"+name+ "from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nMostrando artistas:\n")
    for row in rows:
        print ("   ", row[0])
    conn.commit()
    conn.close()
# retrieve artist 

# retrieve artist and id 
def retrieve_Artists_and_Id():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Artist"'
    name = '"Name"'
    query = "SELECT *"+"from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nRows: \n")
    for row in rows:
        print ("   ", row[0],"   ",row[1])
    conn.commit()
    conn.close()
# retrieve artist and id 

# retrieve artist last id 
def retrieve_last_Artists_id():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Artist"'
    name = '"ArtistId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    conn.commit()
    conn.close()
    return clean
# retrieve artist last id 

# insert artist 
def insert_Artist():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Artist"'
    field1 = '"ArtistId"'
    field2 = '"Name"'
    artist = fake.name()
    artist = "'"+artist+"'"
    id_pos = int(retrieve_last_Artists_id())+1
    id_pos = str(id_pos)
    query = "INSERT INTO "+concat+"("+field1+","+field2+")"+" values("+id_pos+","+artist+");"
    cur.execute(query)
    conn.commit()
    conn.close()
# insert artist 

# insert several artist 
def insert_several_Artists(quantity):
    i = 0
    while(i<quantity):
        insert_Artist()
        i=i+1
# insert several artist 