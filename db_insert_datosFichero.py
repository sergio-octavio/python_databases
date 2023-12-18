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

    # Leer los datos del archivo de texto y evitar líneas vacías
    with open('datos.txt', 'r') as archivo:
        lineas = archivo.readlines()
        datos = []
        for linea in lineas:
            # Verificar si la línea no está vacía
            if linea.strip():
                datos.append(linea.strip().split(','))

    # Verificar duplicados antes de la inserción
    duplicados = []
    for dato in datos:
        select_query = "SELECT * FROM clientes WHERE nombre = %s AND apellido = %s AND email = %s"
        cursor.execute(select_query, (dato[0], dato[1], dato[2]))
        result = cursor.fetchone()
        if result:
            # Si el cliente ya existe, añadirlo a la lista de duplicados
            duplicados.append(result)
        else:
            # Insertar el cliente si no existe
            insert_query = "INSERT INTO clientes (nombre, apellido, email) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, dato)
            conn.commit()

    if duplicados:
        print("Clientes duplicados:")
        for duplicado in duplicados:
            print(duplicado)
    else:
        print("No se encontraron clientes duplicados.")

    print("Datos del archivo insertados en la tabla 'clientes'.")
else:
    print("La tabla 'clientes' no existe. Por favor, crea la tabla primero.")

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
