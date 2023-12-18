import mysql.connector

# Establecer la conexión con MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Contraseña vacía
    database="clientes"
)

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Leer los datos del archivo de texto
with open('datos.txt', 'r') as archivo:
    lineas = archivo.readlines()
    datos = [linea.strip().split(',') for linea in lineas]

# Insertar los datos en la tabla 'clientes'
insert_query = "INSERT INTO clientes (nombre, apellido, email) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, datos)
conn.commit()
print("Datos del archivo insertados en la tabla 'clientes'.")

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
