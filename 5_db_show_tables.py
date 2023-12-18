import mysql.connector

# Establecer la conexión con MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Contraseña vacía, cambiar según la configuración de tu base de datos
    database="clientes"
)

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Consulta para mostrar las tablas en la base de datos 'clientes'
consulta_tablas = "SHOW TABLES;"

# Ejecutar la consulta para obtener las tablas
cursor.execute(consulta_tablas)

# Obtener los resultados de la consulta
resultado = cursor.fetchall()

# Mostrar las tablas o el mensaje de base de datos sin tablas
if not resultado:
    print("La base de datos 'clientes' no tiene tablas.")
else:
    print("Tablas en la base de datos 'clientes':")
    for tabla in resultado:
        print(tabla[0])  # Imprimir el nombre de la tabla

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
