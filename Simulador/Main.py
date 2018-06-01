# /**************************************************************
# ** Universidad del Valle de Guatemala                        **
# ** Bases de Datos                                            **
# ** María MercedesRetolaza Reyna                              **
# ** Carne: 16339                                              **
# ** Fecha: 1/06/2018                                         **
# ***************************************************************/

import Playlistrack_track as ptrack
import Invoice_table as inv
import Customer_table as cust
import Customer_employee as emp
import Artist_table as arts
import Album_table as alb
from random import randint
import Invoiceline_table as invline

while(True):
    
    print("Presione 1 para simular dias")
    print("Presione 2 para salir")

    opcion = input("A continuación ingrese su opcion: ")
    if(int(opcion) ==2):
        break
    if(int(opcion)==1):

        opcio= int(input("Ingrese la cantidad de dias que desea simular: "))
        inv.multi_insert(opcio)
        invline.multi_insert((opcio))
        P_track = randint(0,9)
        for i in range(opcio):
            if(P_track ==1 or P_track ==2 or P_track ==3):
                ptrack.Insert_Ptrack()
            cus = randint(0,9)
            if(cus ==4 or cus ==5 or cus ==6 or cus ==1):
                cust.insert_customers()
            emplo = randint(0,9)
            if(emplo ==4 or emplo ==5 or emplo ==6):
                emp.insert_employees()
            artist = randint(0,9)
            if(artist ==1 or artist ==2 or artist ==3 or artist ==4 or artist==5 or artist ==6 or artist == 7 or artist ==8):
                arts.insert_Artist()

            artist1 = randint(0,9)
            if(artist1 ==1 or artist1 ==2 or artist1 ==3 or artist1 ==4 or artist1==5 or artist1 ==6 or artist1 == 7 or artist ==8 ):
                alb.Insert_Album()