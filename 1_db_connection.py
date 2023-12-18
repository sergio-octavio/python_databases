import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Contraseña vacía
    database="usuarios"  # Reemplaza con el nombre de tu base de datos
)

cursor = conn.cursor()
