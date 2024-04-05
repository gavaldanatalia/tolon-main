import psycopg2
import query_from_source_db

# Establecer la conexión a la base de datos
conn = psycopg2.connect(
    dbname="nombre_basedatos",
    user="usuario",
    password="contraseña",
    host="localhost"  # Puedes cambiar esto según tu configuración
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Ejecutar la consulta SQL
query = query_from_source_db.query_supplier()
cursor.execute(query)

# Obtener los resultados de la consulta
results = cursor.fetchall()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

# Guardar los resultados en un archivo local
with open('prueba_proveedor.csv', 'w') as f:
    for row in results:
        f.write(str(row) + ';')

print("Los resultados se han guardado en 'prueba_proveedor.csv'.")