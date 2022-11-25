import pyodbc
import os

# server = 'tcp:myserver.database.windows.net' 
# database = 'mydb' 
# username = 'myusername' 
# password = 'mypassword' 

dbuser = os.getenv('DBUSER'),
dbpass = os.getenv('DBPASS'),
dbhost = os.getenv('DBHOST'),
dbname = os.getenv('DBNAME')


def connect():
    try:
        string_conn = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={dbhost};DATABASE={dbname};PWD={dbpass};ENCRYPT=yes'
        connection = pyodbc.connect(string_conn)
        
        print("Conexión exitosa.")
        cursor = connection.cursor()

        return cursor

        # cursor.execute("SELECT @@version;")
        # row = cursor.fetchone()
        # print(f"Versión del servidor de SQL Server: {row}")
        # cursor.execute("SELECT * FROM tarea")
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)

    except Exception as ex:
        print(f"Error durante la conexión: {ex}")


