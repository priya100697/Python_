import psycopg2
from Database.DbConnect import get_connection


# Ref: https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
if __name__ == "__main__":
    conn = get_connection()
    #conn = psycopg2.connect("dbname=Pdb user=postgres password=toor")
    cur = conn.cursor()

    cur.execute("select * from employee")
    data = cur.fetchall()
    print("Number of records before insertion = ", data)

    cur.execute("insert into employee(id, name) values(%s, %s)", (1, "anand"))

    cur.execute("select count(*) from employee")
    data = cur.fetchall()
    print("Number of records after insertion = ", data)

    conn.commit()

    cur.close()
    conn.close()
