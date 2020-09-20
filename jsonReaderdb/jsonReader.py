import json
from jsonReaderdb.DbConnect import connection


def reader(path):
    with open(path, "r") as file:
        data = json.load(file)

    conn = connection()
    cur = conn.cursor()

    for item in data:
        cur.execute("insert into employee(id,name) values(%s, %s)", (item['id'], item['name']))

    conn.commit()
    cur.close()
    conn.close()
