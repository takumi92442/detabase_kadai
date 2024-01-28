import psycopg

connection = psycopg.connect(
    host='localhost',
    dbname='students',
    user='postgres',
    password='password',
)