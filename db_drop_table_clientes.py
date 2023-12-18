import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Contraseña vacía
    database="clientes"
)

cursor = conn.cursor()

# Consulta para verificar si existe la tabla 'clientes'
show_table_query = "SHOW TABLES LIKE 'clientes'"

# Ejecutar la consulta
cursor.execute(show_table_query)

# Obtener los resultados
result = cursor.fetchone()

if result:
    # Si la tabla 'clientes' existe, eliminarla
    drop_table_query = "DROP TABLE clientes"
    cursor.execute(drop_table_query)
    print("La tabla 'clientes' ha sido eliminada.")
    conn.commit()
else:
    # Si la tabla 'clientes' no existe, mostrar un mensaje
    print("La tabla 'clientes' no existe. ")

# Cerrar la conexión
cursor.close()
conn.close()
