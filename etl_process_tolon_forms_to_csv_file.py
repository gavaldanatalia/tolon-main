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

array_query = [query_from_source_db.query_articulos(), query_from_source_db.query_supplier()]
array_file_name = ["prueba_articulos.csv", "prueba_supplier.csv"]

for query in array_query:
    for file in array_file_name:
        # Ejecutar la consulta SQL
        cursor.execute(query)

        # Obtener los resultados de la consulta
        results = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Guardar los resultados en un archivo local
        with open(f'{file}', 'w') as f:
            for row in results:
                f.write(str(row) + ';')

        print(f"Los resultados se han guardado en {file}.")