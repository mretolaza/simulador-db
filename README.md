# Simulador de ventas

Es un simulador hecho en python que ejecuta las tablas de la db dada por @hectorh30 durante la elaboración del laboratorio 12 del curso. 

# Antes de empezar 

>> Se debe instalar lo siguiente: 

- installation via pip install psycopg2, psycopg2-binary, termcolor, Faker

>> Se utilizó *Python 2.7* 

- Revisar la línea #42  se debe de agregar la conexión a la base de datos agregando en esta linea las creedenciales de la misma. 

>> *conn = psycopg2.connect("dbname='mercedes' user='postgres' password='123'")* 

# Para ejecutar el simulador 

>> python simulator.py 500 (este es el número de opciones que sacará *es un parámetro requerido*) file.csv (*donde este es un parámetro opcional*) 

# Región de Faker 

>> Delimitada a 'es_ES'este parámetro se puede eliminar para que no se delimite a una sola región. 
