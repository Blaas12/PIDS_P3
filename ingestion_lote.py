import csv
import psycopg2
from psycopg2 import sql
import time

# Configuración de la conexión a la base de datos PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    database="patinetes",
    user="postgres",
    password="aaa"
)

# Nombre del archivo CSV
archivo_csv = 'rome_u_journeys.csv'

# Nombre de la tabla en la base de datos
nombre_tabla = 'lote_inicial'

# Abrir el archivo CSV y leer los datos
with open(archivo_csv, 'r') as csv_file:
    lector_csv = csv.reader(csv_file)
    encabezados = next(lector_csv)  # Lee la primera fila como encabezados

    # Crear una sentencia SQL para crear la tabla si no existe
    with conexion.cursor() as cursor:
        try:
            crear_tabla = sql.SQL("""
                CREATE TABLE IF NOT EXISTS {} (
                    {}
                )
            """).format(
                sql.Identifier(nombre_tabla),
                sql.SQL(', ').join(
                    sql.Identifier(columna.replace(' ', '_')) + sql.SQL(' TEXT') for columna in encabezados
                )
            )
            cursor.execute(crear_tabla)
            conexion.commit()

        except Exception as e:
            print(f"Error al crear la tabla: {e}")
            conexion.rollback()

    # Insertar datos en la tabla
    with conexion.cursor() as cursor:
        try:
            # Agregamos una pausa para asegurarnos de que la tabla esté creada antes de intentar insertar datos
            time.sleep(1)

            for fila in lector_csv:
                # Crear la sentencia SQL de inserción
                insertar_fila = sql.SQL("""
                    INSERT INTO {} ({})
                    VALUES ({})
                """).format(
                    sql.Identifier(nombre_tabla),
                    sql.SQL(', ').join(sql.Identifier(columna.replace(' ', '_')) for columna in encabezados),
                    sql.SQL(', ').join(sql.Placeholder() for _ in fila)
                )

                # Ejecutar la sentencia de inserción
                cursor.execute(insertar_fila, fila)

            # Commit para aplicar los cambios
            conexion.commit()

        except Exception as e:
            print(f"Error al insertar datos: {e}")
            conexion.rollback()

# Cerrar la conexión a la base de datos
conexion.close()
