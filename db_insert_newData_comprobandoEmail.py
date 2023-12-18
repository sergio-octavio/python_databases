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

    # Obtener información de las columnas si la tabla existe
    cursor.execute("DESCRIBE clientes;")
    columnas = cursor.fetchall()
    print("Columnas de la tabla 'clientes':")
    for columna in columnas:
        print(columna[0])  # Imprimir el nombre de la columna

    # Leer los datos del archivo de texto
    with open('datos.txt', 'r') as archivo:
        lineas = archivo.readlines()
        datos = [linea.strip().split(',') for linea in lineas]

    # Insertar los datos en la tabla 'clientes'
    insert_query = "INSERT INTO clientes (nombre, apellido, email) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, datos)
    conn.commit()
    print("Datos del archivo insertados en la tabla 'clientes'.")
else:
    print("La tabla 'clientes' no existe. Por favor, crea la tabla primero.")

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
