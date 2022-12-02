from database import connect


def switch(argument):
    match argument:
        case 'a':
            try:
                return sp1()
            except Exception as ex:
                print(f"Error durante la conexión: {ex}")
                return None
        case 'b':
            try:
                return sp2_4("Exec [dbo].[sp_queryB]")
            except Exception as ex:
                print(f"Error durante la conexión: {ex}")
                return None
        case 'c':
            try:
                return sp3()
            except Exception as ex:
                print(f"Error durante la conexión: {ex}")
                return None
        case 'd':
            try:
                return sp2_4("Exec [dbo].[sp_queryD]")
            except Exception as ex:
                print(f"Error durante la conexión: {ex}")
                return None
        case 'e':
            try:
                return sp5()
            except Exception as ex:
                print(f"Error durante la conexión: {ex}")
                return None
        case 'f':
            try:
                return sp6()
            except Exception as ex:
                print(f"Error durante la conexión: {ex}")
                return None
        case 'g':
            try:
                return sp7()
            except Exception as ex:
                print(f"Error durante la conexión: {ex}")
                return None
        case default:
            return "Ingresa otra opcion"


def sp7():
    cursor = connect()
    storedProc = "Exec [dbo].[sp_queryG] @p_EmailAntes = ?, @p_EmailNuevo = ?"
    emailAntes = input('Ingresa un email: ')
    emailNuevo = input('Ingresa un nuevo email: ')
    params = (str(emailAntes), str(emailNuevo))
    cursor.execute(storedProc, params)
    return cursor.fetchall()


def sp6():
    cursor = connect()
    storedProc = "Exec [dbo].[sp_queryF] @p_SalesOrderID = ?, @p_MethodEnvioID = ?"
    salesOrderID = input('Ingresa un ID de venta: ')
    methodEnvioID = input('Ingresa un ID de metodo de envio: ')
    params = (int(salesOrderID), int(methodEnvioID))
    cursor.execute(storedProc, params)
    return cursor.fetchall()


def sp5():
    cursor = connect()
    storedProc = "Exec [dbo].[sp_queryE] @qty = ?, @salesID = ?, @productID = ?"
    qty = input('Ingresa una cantidad: ')
    salesID = input('Ingresa un ID de venta: ')
    productID = input('Ingresa un ID de producto: ')
    params = (int(qty), int(salesID), int(productID))
    cursor.execute(storedProc, params)
    return cursor.fetchall()


def sp3():
    cursor = connect()
    storedProc = "Exec [dbo].[sp_queryC] @producto = ?, @localidad = ?"
    producto = input('Ingresa un producto: ')
    localidad = input('Ingresa una localidad: ')
    params = (producto, localidad)
    cursor.execute(storedProc, params)
    return cursor.fetchall()


def sp1():
    cursor = connect()
    storedProc = "Exec [dbo].[sp_queryA] @cat = ?"
    cat = input('Ingresa una categoria: ')
    params = (int(cat))
    cursor.execute(storedProc, params)
    return cursor.fetchall()


def sp2_4(arg0):
    cursor = connect()
    storedProc = arg0
    params = ()
    cursor.execute(storedProc, params)
    return cursor.fetchall()


def main():
    while (1):
        query = input('Selecciona una consulta: ')
        result = switch(query)
        print(result)


if __name__ == '__main__':
    main()
