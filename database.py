import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

server = os.getenv('SERVER')
database = os.getenv('DATABASE') 
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
print(server)


def connect():
    try:
        # string_conn = f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={dbhost};DATABASE={dbname};PWD={dbpass};ENCRYPT=yes'
        # connection = pyodbc.connect(string_conn)
        #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password+'Trusted_Connection=yes;')
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
        
        print("Conexión exitosa.")
        # cursor = connection.cursor()

        # cursor.execute("SELECT * FROM testtable")
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)

        # return cursor

        # cursor.execute("SELECT @@version;")
        # row = cursor.fetchone()
        # print(f"Versión del servidor de SQL Server: {row}")
        # cursor.execute("SELECT * FROM tarea")
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)

    except Exception as ex:
        print(f"Error durante la conexión: {ex}")

if __name__ == '__main__':
    connect()


