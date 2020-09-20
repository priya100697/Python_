import psycopg2


def get_connection():

    conn = psycopg2.connect("dbname=Pdb user=postgres password=toor")
    return conn
