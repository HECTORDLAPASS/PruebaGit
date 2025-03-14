import psycopg2
try:
    conn = psycopg2.connect(
        host="localhost",
        user="admin",
        password="admin",
        database="Narad",
        port="5432"
    )
    print("conectado a la base de datos")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)