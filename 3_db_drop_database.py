import mysql.connector

# Conectarse al servidor de MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Contraseña vacía
    database=""  # No necesitas seleccionar una base de datos para borrarla
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Nombre de la base de datos que deseas eliminar
database_name = "clientes"

# Consulta para eliminar la base de datos
drop_database_query = f"DROP DATABASE {database_name}"

try:
    # Ejecutar la consulta para eliminar la base de datos
    cursor.execute(drop_database_query)
    print(f"La base de datos '{database_name}' ha sido eliminada exitosamente.")
except mysql.connector.Error as err:
    print(f"No se pudo eliminar la base de datos: {err}")
finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()