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

    # Consulta para eliminar duplicados basados en nombre, apellido y email
    delete_query = '''
    DELETE c1 FROM clientes c1
    JOIN clientes c2 ON 
        c1.nombre = c2.nombre AND
        c1.apellido = c2.apellido AND
        c1.email = c2.email
    WHERE c1.id > c2.id
    '''
    cursor.execute(delete_query)
    print("Duplicados eliminados")
    conn.commit()

    # Consulta para obtener los elementos que se eliminaron y contarlos
    select_deleted_query = '''
    SELECT nombre, apellido, email, COUNT(*) AS cantidad_eliminados 
    FROM clientes GROUP BY nombre, apellido, email
    '''
    cursor.execute(select_deleted_query)
    duplicados_eliminados = cursor.fetchall()

else:
    print("La tabla 'clientes' no existe. Por favor, crea la tabla primero.")

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
