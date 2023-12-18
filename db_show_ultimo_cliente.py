import mysql.connector
import re

# Establecer la conexión con MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Contraseña vacía
    database="clientes"
)

cursor = conn.cursor()

# Obtener el último registro insertado
cursor.execute("SELECT * FROM clientes ORDER BY id DESC LIMIT 1")
ultimo_registro = cursor.fetchone()

if ultimo_registro:
    print("Último registro insertado:")
    print(f"ID: {ultimo_registro[0]}")
    print(f"Nombre: {ultimo_registro[1]}")
    print(f"Apellido: {ultimo_registro[2]}")
    print(f"Correo electrónico: {ultimo_registro[3]}")
else:
    print("No se encontraron registros en la base de datos.")

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
