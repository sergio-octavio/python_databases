import mysql.connector
import re

# Establecer la conexión con MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Contraseña vacía
    database="clientes"
)

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

    # Función para validar el formato del correo electrónico
    def validar_correo(correo):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, correo) is not None

    # Pedir al usuario que ingrese los datos hasta que se proporcionen valores válidos
    nombre, apellido, email = "", "", ""

    while not nombre.strip():
        nombre = input("Ingresa el nombre: ")
        if not nombre.strip():
            print("El nombre no puede estar vacío.")

    while not apellido.strip():
        apellido = input("Ingresa el apellido: ")
        if not apellido.strip():
            print("El apellido no puede estar vacío.")

    while not email.strip() or not validar_correo(email):
        email = input("Ingresa el correo electrónico: ")
        if not email.strip():
            print("El correo electrónico no puede estar vacío.")
        elif not validar_correo(email):
            print("Por favor, ingresa un correo electrónico válido.")

    datos = [nombre, apellido, email]

    # Comprobar si el correo ya existe en la base de datos
    cursor.execute("SELECT email FROM clientes WHERE email = %s", (email,))
    resultado = cursor.fetchall()

    if not resultado:
        # Si el correo no existe, insertar el dato en la tabla
        cursor.execute("INSERT INTO clientes (nombre, apellido, email) VALUES (%s, %s, %s)", datos)
        conn.commit()
        print(f"Datos insertados en la tabla 'clientes'.")
    else:
        print(f"El correo electrónico ya existe en la base de datos y no se insertó.")

else:
    print("La tabla 'clientes' no existe. Por favor, crea la tabla primero.")

# Cerrar el cursor y la conexión con MySQL
cursor.close()
conn.close()
