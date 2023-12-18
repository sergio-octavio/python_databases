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

# Verificar si la tabla 'clientes' existe
cursor.execute("SHOW TABLES LIKE 'clientes';")
existe_tabla = cursor.fetchone()

if existe_tabla:
    print("La tabla 'clientes' ya existe.")

    # Verificar si la columna 'apellido' existe en la tabla 'clientes'
    cursor.execute("SHOW COLUMNS FROM clientes WHERE Field = 'apellido';")
    existe_apellido = cursor.fetchone()

    if existe_apellido:
        # Eliminar la columna 'apellido' si existe
        cursor.execute("ALTER TABLE clientes DROP COLUMN apellido;")
        print("La columna 'apellido' se ha eliminado de la tabla 'clientes'.")
    else:
        print("La columna 'apellido' no existe en la tabla 'clientes'.")
else:
    print("La tabla 'clientes' no existe en la base de datos.")

# Cerrar el cursor y la conexión con la base de datos
cursor.close()
conn.close()
