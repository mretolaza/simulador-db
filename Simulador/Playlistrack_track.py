# /**************************************************************
# ** Universidad del Valle de Guatemala                        **
# ** Bases de Datos                                            **
# ** María MercedesRetolaza Reyna                              **
# ** Carne: 16339                                              **
# ** Fecha: 1/06/2018                                         **
# ***************************************************************/


#track y playlisttrack
#playlisttrack usa id de track
import psycopg2
from random import randint

# retrieve last track id 
def retrieve_Last_TrackId():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Track"'
    name = '"TrackId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    conn.commit()
    conn.close()
    return clean
# retrieve last track id 

# retrieve last playlist track id 
def retrieve_Last_PlaylistTrackId():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Playlist"'
    name = '"PlaylistId"'
    query = "SELECT "+name+ "from "+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    try:
        clean = str(rows[0]).replace('(','')
        clean = clean.replace(',','')
        clean = clean.replace(')','')
    except:
        clean = str(1)
    conn.commit()
    conn.close()
    return clean
# retrieve last playlist track id 

# insert p track 
def Insert_Ptrack():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"PlaylistTrack"'
    field1 = '"PlaylistId"'
    field2 = '"TrackId"'
    id1_range = retrieve_Last_PlaylistTrackId()
    id2_range = retrieve_Last_TrackId()
    id1 = str(randint(1,int(id1_range)-1))
    id2= str(randint(1,int(id2_range)-1))
    query = "INSERT INTO "+concat+"("+field1+","+field2+")"+"VALUES("+id1+","+id2+") ;"
    cur.execute(query)
    conn.commit()
    conn.close()
# insert p track 