import mysql.connector
import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('/Users/ngavalda/PycharmProjects/tolon-main/data/articulos.csv', delimiter=";")

print(df.columns)
print(df.head())

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

# Iterar sobre las filas del DataFrame y realizar la inserción en la base de datos
for index, row in df.iterrows():
    query = "INSERT INTO articulo_prueba (id_articulo, des_articulo) VALUES (%s, %s)"
    datos = (row['ite_id'], row['ite_name'])
    print(datos)
    cursor.execute(query, datos)

# Confirmar la transacción
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

print("Datos insertados correctamente.")

