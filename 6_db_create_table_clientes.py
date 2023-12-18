import mysql.connector

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
    column_names = [columna[0] for columna in columnas]
    for columna in columnas:
        print(columna[0])  # Imprimir el nombre de la columna

    # Verificar si la columna 'apellido' existe en las columnas de la tabla 'clientes'
    if 'apellido' not in column_names:
        # La columna 'apellido' no existe, agregarla a la tabla 'clientes'
        cursor.execute("ALTER TABLE clientes ADD COLUMN apellido VARCHAR(50);")
        conn.commit()
        print("Se ha agregado la columna 'apellido' a la tabla 'clientes'.")

    # Si es necesario, reorganizar las columnas
    if column_names != ['id', 'nombre', 'apellido', 'email']:
        # Crear una nueva tabla con el orden de columnas deseado
        cursor.execute('''CREATE TABLE clientes_nueva (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(50),
                            apellido VARCHAR(50),
                            email VARCHAR(100)
                         );''')
        conn.commit()
        print("Se ha creado una nueva tabla 'clientes_nueva' con el orden de columnas deseado.")

        # Copiar los datos desde la tabla original a la nueva tabla en el orden deseado
        cursor.execute('''INSERT INTO clientes_nueva (id, nombre, apellido, email)
                          SELECT id, nombre, apellido, email FROM clientes;''')
        conn.commit()
        print("Los datos se han copiado a la nueva tabla 'clientes_nueva' con el orden de columnas deseado.")

        # Eliminar la tabla original 'clientes'
        cursor.execute("DROP TABLE clientes;")
        conn.commit()
        print("La tabla 'clientes' original se ha eliminado.")

        # Renombrar la nueva tabla como 'clientes'
        cursor.execute("ALTER TABLE clientes_nueva RENAME TO clientes;")
        conn.commit()
        print("La nueva tabla 'clientes_nueva' se ha renombrado a 'clientes'.")
else:
    # Crear la tabla 'clientes' si no existe
    cursor.execute('''CREATE TABLE clientes (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(50),
                        apellido VARCHAR(50),
                        email VARCHAR(100)
                     );''')
    print("La tabla 'clientes' se ha creado exitosamente.")

    # Imprimir las columnas recién creadas
    cursor.execute("DESCRIBE clientes;")
    columnas_creadas = cursor.fetchall()
    print("Columnas de la tabla 'clientes':")
    for columna in columnas_creadas:
        print(columna[0])  # Imprimir el nombre de la columna

# Cerrar el cursor y la conexión con la base de datos
cursor.close()
conn.close()
