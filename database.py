import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


def connect():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
        # print("Conexión exitosa.")
        cursor = connection.cursor()
        return cursor
    except Exception as ex:
        print(f"Error durante la conexión: {ex}")
        exit(1)
