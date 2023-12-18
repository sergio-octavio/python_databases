import mysql.connector

# Establecer la conexión con MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Contraseña vacía
)

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Verificar si la base de datos 'clientes' existe
cursor.execute("SHOW DATABASES LIKE 'clientes';")
existe_db = cursor.fetchone()

if existe_db:
    print("La base de datos 'clientes' ya existe.")
else:
    # Crear la base de datos 'clientes' si no existe
    cursor.execute("CREATE DATABASE clientes;")
    print("La base de datos 'clientes' se ha creado exitosamente.")

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
