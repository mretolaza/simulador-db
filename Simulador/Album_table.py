# /**************************************************************
# ** Universidad del Valle de Guatemala                        **
# ** Bases de Datos                                            **
# ** María MercedesRetolaza Reyna                              **
# ** Carne: 16339                                              **
# ** Fecha: 28/05/2018                                         **
# ***************************************************************/

import psycopg2
# Extraída de https://github.com/joke2k/faker
# Documentación encontrada en: http://faker.readthedocs.io/en/master/
from faker import Faker

# Inicialización
fake = Faker()

# retrieve - all 
def retrieve_All():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Album"'
    query = "SELECT *"+"from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nRows: \n")
    for row in rows:
        print ("   ", row[0],"   ",row[1],"   ",row[2])
    conn.commit()
    conn.close()
# retrieve - all 


# retrieve - id 
def retrieve_Id():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Album"'
    name = '"AlbumId"'
    query = "SELECT"+name+ "from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nMostrando Id:\n")
    for row in rows:
        print ("   ", row[0])
    conn.commit()
    conn.close()
# retrieve - id 

# retrieve - last - id 
def retrieve_Last_Id():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Album"'
    name = '"AlbumId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    conn.commit()
    conn.close()
    return clean
# retrieve - last - id 

# retrieve - last artist id 
def retrieve_Last_ArtistId():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Album"'
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
# retrieve - last artist id 

# retrieve title 
def retrieve_Title():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Album"'
    name = '"Title"'
    query = "SELECT"+name+ "from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nMostrando Id:\n")
    for row in rows:
        print ("   ", row[0])
    conn.commit()
    conn.close()
# retrieve title 

# retrieve artist id 
def retrieve_ArtistId():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Album"'
    name = '"ArtistId"'
    query = "SELECT"+name+ "from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nMostrando Id:\n")
    for row in rows:
        print ("   ", row[0])
    conn.commit()
    conn.close()
# retrieve artist id 

# insert - album 
def Insert_Album():
    album_id = retrieve_Last_Id()
    artist_id = retrieve_Last_ArtistId()
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Album"'
    field1 = '"AlbumId"'
    field2 = '"Title"'
    field3 = '"ArtistId"'
    artist = fake.name()
    artist = "'"+artist+"'"
    id_pos = int(album_id)+1
    id_pos = str(id_pos)
    id_pos2 = int(artist_id)+1
    id_pos2 = str(id_pos2)
    query = "INSERT INTO "+concat+"("+field1+","+field2+","+field3+")"+" values("+id_pos+","+artist+","+id_pos2+");"
    cur.execute(query)
    #print ("\nInsercion hecha con exito\n")
    conn.commit()
    conn.close()