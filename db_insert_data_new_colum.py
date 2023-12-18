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
        datos_archivo = [linea.strip().split(',') for linea in lineas if linea.strip()]  # Filtrar líneas vacías

    # Comprobar y añadir los apellidos faltantes a la tabla 'clientes'
    for dato in datos_archivo:
        if len(dato) == 3:  # Verificar si la línea tiene la cantidad esperada de elementos (nombre, apellido, email)
            nombre, apellido, correo = dato[0], dato[1], dato[2]

            # Verificar si el correo y el nombre coinciden con los datos en la base de datos
            cursor.execute("SELECT apellido FROM clientes WHERE nombre = %s AND email = %s", (nombre, correo))
            resultado = cursor.fetchone()

            if resultado:
                # Si coincide, actualizar el apellido en la base de datos
                cursor.execute("UPDATE clientes SET apellido = %s WHERE nombre = %s AND email = %s", (apellido, nombre, correo))
                conn.commit()
                print(f"El apellido para {nombre} ha sido actualizado en la tabla 'clientes'.")
            else:
                print(f"No se encontró coincidencia para {nombre} y {correo} en la base de datos.")
        else:
            print(f"La línea {dato} no tiene la cantidad esperada de elementos y fue omitida.")

else:
    print("La tabla 'clientes' no existe. Por favor, crea la tabla primero.")

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
