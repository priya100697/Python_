from readSql_execute_in_DB.readScript import readfile
from readSql_execute_in_DB.Db_connection import connection

file_content = readfile("Script.sql")
#print(file_content)

conn = connection()
cur = conn.cursor()

for line in file_content:
    print("*****************************************************")
    print("executed command\n",line)
    cur.execute(line)
    print("*****************************************************")
conn.commit()
conn.close()
cur.close()


