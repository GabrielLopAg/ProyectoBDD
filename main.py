from database import connect


def switch(argument):
    match argument:
        case 'a':
            try:
                cursor = connect()
                storedProc = "Exec [dbo].[sp_emailAct] @p_EmailAntes = ?, @p_EmailNuevo = ?"
                storedProc = "Exec [dbo].[sp_queryA] @cat = ?"
                cat = input('Ingresa una categoria: ')
                params = (int(cat))
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

        case 'b':
            try:
                cursor = connect()
                storedProc = "Exec [dbo].[sp_queryB]"
                params = ()
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
            try:
                cursor = connect()
                storedProc = "Exec [dbo].[sp_queryC] @producto = ?, @localidad = ?"
                producto = input('Ingresa un producto: ')
                localidad = input('Ingresa una localidad: ')
                params = (producto, localidad)
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
        case 'd':
            try:
                cursor = connect()
                storedProc = "Exec [dbo].[sp_queryD]"
                params = ()
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
        case 'e':
            try:
                cursor = connect()
                storedProc = "Exec [dbo].[sp_queryE] @qty = ?, @salesID = ?, @productID = ?"
                qty = input('Ingresa una cantidad: ')
                salesID = input('Ingresa un ID de venta: ')
                productID = input('Ingresa un ID de producto: ')
                params = (int(qty), int(salesID), int(productID))
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
        case 'f':
            try:
                cursor = connect()
                storedProc = "Exec [dbo].[sp_queryF] @p_SalesOrderID = ?, @p_MethodEnvioID = ?"
                salesOrderID = input('Ingresa un ID de venta: ')
                methodEnvioID = input('Ingresa un ID de metodo de envio: ')
                params = (int(salesOrderID), int(methodEnvioID))
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
        case 'g':
            try:
                cursor = connect()
                storedProc = "Exec [dbo].[sp_queryG] @p_EmailAntes = ?, @p_EmailNuevo = ?"
                emailAntes = input('Ingresa un email: ')
                emailNuevo = input('Ingresa un nuevo email: ')
                params = (str(emailAntes), str(emailNuevo))
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
        case default:
            return "something"


def main():
    query = input('Selecciona una consulta: ')
    result = switch(query)
    print(result)


if __name__ == '__main__':
    main()
