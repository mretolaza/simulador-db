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

count = 5

# retrieve last invoice id 
def retrieve_Last_InvoiceId():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Invoice"'
    name = '"InvoiceId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    conn.commit()
    conn.close()
    return clean
# retrieve last invoice id 


# retrieve last customer id 
def retrieve_Last_CustomerId():
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Customer"'
    name = '"CustomerId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    #print(clean)
    conn.commit()
    conn.close()
    return clean
# retrieve last customer id 

# insert sale 
def Insert_sale(count):
    conn = psycopg2.connect("dbname=nombreAqui user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Invoice"'
    field1 = '"InvoiceId"'
    field2 = '"CustomerId"'
    field3 = '"InvoiceDate"'
    field4 = '"BillingAddress"'
    field5 = '"BillingCity"'
    field6 = '"BillingState"'
    field7 = '"BillingCountry"'
    field8 = '"BillingPostalCode"'
    field9 = '"Total"'
    id_invoice = retrieve_Last_InvoiceId()
    customer_id = int(retrieve_Last_CustomerId())
    cus_pos = str(randint(1,customer_id ))
    dia = count
    dia = str(count)
    date = '2018/06/'+dia
    adress = fake.address()
    adress = "'"+adress+"'"
    date = "'"+date+"'"
    id_pos = int(id_invoice)+1
    id_pos = str(id_pos)
    artist = fake.name()
    artist = "'"+artist+"'"
    cities = ['Stuttgart','Palooza','Guatemala City']
    city_pick = randint(0,len(cities)-1)
    city_pos = "'"+cities[city_pick]+"'"
    Bill1 = str(randint(1111,9998))
    Bill2 = str(randint(111,998))
    Bill4 = ['AZ','NW','CA','SSR']
    bill_pick = randint(0,len(Bill4)-1)
    Bill3 = 'ST '+Bill4[bill_pick]
    string_of_bill1 = "'"+Bill1+"'"
    string_of_bill2 = "'"+Bill2+"'"
    string_of_bill3 = "'"+Bill3+"'"
    final_bill = string_of_bill1+string_of_bill2+string_of_bill3
    country_list = ['Germany','Guatemala','France','England','USA']
    country_pick = randint(0,len(country_list)-1)
    country = "'"+country_list[country_pick]+"'"
    postal_code = "'"+str(randint(11111,99998))+"'"
    total = "'"+str(random.uniform(1,20))+"'"
    query = "INSERT INTO "+concat+"("+field1+","+field2+","+field3+","+field4+","+field5+","+field6+","+field7+","+field8+","+field9+")"+" values("+id_pos+","+cus_pos+","+date+","+adress+","+city_pos+","+final_bill+","+country+","+postal_code+","+total+");"
    cur.execute(query)
    conn.commit()
    conn.close()
# insert sale 

# multi insert 
def multi_insert(veces):
    i = 0
    cambio_dia = randint(2,8)
    contador_dia = 0
    count =5
    while(i<veces):
        Insert_sale(count)
        contador_dia = contador_dia+1
        if(contador_dia == cambio_dia):
            count = count+1
            contador_dia = 0
            cambio_dia = randint(2,8)
        if(count>=31):
            count = 1
        i = i+1
    print ("\nInsercion hecha con exito\n")
#multi_insert --> 100