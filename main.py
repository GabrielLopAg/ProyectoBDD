from database import connect

def main():
    
    try:
        cursor = connect()
        cursor.execute("SELECT * FROM testtable")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as ex:
        print(f"Error durante la conexión: {ex}")


if __name__ == '__main__':
    main()



