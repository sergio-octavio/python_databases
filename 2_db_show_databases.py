import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Contraseña vacía
    # database="clientes"  # Reemplaza con el nombre de tu base de datos
)

#Establecemos la conexión con la base de datos
cursor = conn.cursor()

#Para visualizar las tablas
sql = "SHOW DATABASES"

# Ejecutar la consulta
cursor.execute(sql)

# Obtener los resultados de la consulta
tablas = cursor.fetchall()

# Mostrar por pantalla los nombres de las tablas
print("Tablas disponibles en la base de datos:")
for tabla in tablas:
    print(tabla[0])
conn.close()