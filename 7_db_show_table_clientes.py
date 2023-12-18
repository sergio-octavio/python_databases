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
    # Mostrar los datos de la tabla 'clientes'
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()

    if filas:
        print("Datos de la tabla 'clientes':")
        for fila in filas:
            print(f"{fila[0]} {fila[1]} {fila[2]} {fila[3]}")
    else:
        print("La tabla 'clientes' está vacía.")
        # Imprimir las columnas recién creadas
        cursor.execute("DESCRIBE clientes;")
        columnas_creadas = cursor.fetchall()
        print("Columnas de la tabla 'clientes':")
        for columna in columnas_creadas:
            print(columna[0])  # Imprimir el nombre de la columna
else:
    print("La tabla 'clientes' no existe.")

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
