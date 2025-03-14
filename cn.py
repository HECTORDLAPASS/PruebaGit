import psycopg2

query = "SELECT * FROM empleados;"

try:
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="admin",
        database="Narad",
        port="5432"
    )
    print("Conectado a la base de datos")

    cur = conn.cursor()
    cur.execute(query)
    resultados = cur.fetchall()

    for fila in resultados:
        print(fila)

    cur.close()

except (Exception, psycopg2.Error) as error:
    print("Error al conectar a PostgreSQL", error)
finally:
    conn.close()
    print("conexion cerrada")

