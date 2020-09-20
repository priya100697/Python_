import psycopg2


def connection():
    conn = psycopg2.connect("dbname=Pdb user=postgres password=toor")
    return conn
