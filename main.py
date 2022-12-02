from database import connect


def switch(argument):
    match argument:
        case 'a':
            try:
                cursor = connect()
                cursor.execute("SELECT * FROM testtable")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

                return rows
            except Exception as ex:
                print(f"Error durante la conexión: {ex}")
                return None

        case 'b':
            try:
                cursor = connect()
                storedProc = "Exec [dbo].[sp_emailAct] @p_EmailAntes = ?, @p_EmailNuevo = ?"
                # storedProc = "Exec [dbo].[Consulta4]"
                # storedProc = "execute dbo.Consulta4"

                params = ('ken0@adventure-works.com', 'example@gmail.com')
                # params = ()

                # Execute Stored Procedure With Parameters
                cursor.execute(storedProc, params)
                rows = cursor.fetchall()

                # # Iterate the cursor
                # row = cursor.fetchone()
                # while row:
                #     # Print the row
                #     print(str(row[0]) + " : " + str(row[1] or ''))
                #     row = cursor.fetchone()

                return rows
            except Exception as ex:
                print(f"Error durante la conexión: {ex}")
                return None

        case 'c':
            return "two"
        case 'd':
            return "three"
        case 'e':
            return "four"
        case 'f':
            return "five"
        case 'g':
            return "six"
        case default:
            return "something"


def main():
    query = input('Selecciona una consulta: ')
    result = switch(query)
    print(result)


if __name__ == '__main__':
    main()
