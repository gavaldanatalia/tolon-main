import mysql.connector
import query_from_source_db
import datetime

# Establecer la conexión a la base de datos
conn = mysql.connector.connect(
    host="tolon.spaindev.com",
    user="tolon_db_adm",
    password="Jpk47~84n",
    port="3306",
    database="tolon_forms2"
)

print("Conexion establecida")

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Query
query = query_from_source_db.query_registros_chofer()

# Ejecutar la consulta SQL
cursor.execute(query)

# Obtener los resultados de la consulta
results = cursor.fetchall()

print(results)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

# Dónde queremos guardar la información de los registros
file = "/Users/ngavalda/PycharmProjects/tolon-main/data/prueba_registros"

# Guardar los resultados en un archivo local
with open(f'{file}.txt', 'w') as f:
    for row in results:
        # Convertir la fecha a string en el formato deseado 'YYYY-MM-DD'
        formatted_row = [str(val.strftime('%Y/%m/%d')) if isinstance(val, datetime.date) else str(val) for val in row]
        f.write(', '.join(formatted_row) + '\n')

print(f"Los resultados se han guardado en {file}.")