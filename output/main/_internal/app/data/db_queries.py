from app.data.db_connection import DatabaseConnection
import sqlite3

class DatabaseQueries:
    @staticmethod
    def insertar_nuevo_ingreso(numero_guia, nombre_empresa, cantidad_productos, fecha, ruta_guia, ruta_factura):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        cursor = connection.cursor()
        query = """
            INSERT INTO NuevoIngreso (nombre_guia, nombre_empresa, cantidad_productos, fecha_guia, path_guia, path_factura, save_data)
            VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
        """
        try:
            cursor.execute(query, (numero_guia, nombre_empresa, cantidad_productos, fecha, ruta_guia, ruta_factura))
            connection.commit()
            cursor.execute("SELECT last_insert_rowid()")
            id_nuevo_ingreso = cursor.fetchone()[0]
        except sqlite3.Error as e:
            print(f"Error al insertar nuevo ingreso: {e}")
            connection.rollback()
            id_nuevo_ingreso = None
        finally:
            db_connection.close_connection()
        
        return id_nuevo_ingreso

    @staticmethod
    def insertar_productos(id_nuevo_ingreso, productos):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        cursor = connection.cursor()
        try:
            for producto in productos:
                nombre_producto = producto['nombre']
                series_producto = producto['series']
                series_str = ', '.join(series_producto)
                query = """
                    INSERT INTO Productos (id_nuevoingreso, nombre_producto, series_producto)
                    VALUES (?, ?, ?)
                """
                cursor.execute(query, (id_nuevo_ingreso, nombre_producto, series_str))
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error al insertar productos: {e}")
            connection.rollback()
        finally:
            db_connection.close_connection()

    def obtener_resumen_nuevo_ingreso(self):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        try:
            consulta = """
            SELECT id_nuevoingreso, nombre_guia, nombre_empresa, cantidad_productos, fecha_guia
            FROM NuevoIngreso;
            """
            cursor = connection.cursor()
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except sqlite3.Error as e:
            print(f"Error al obtener resumen de nuevo ingreso: {e}")
            return []
        finally:
            db_connection.close_connection()

    def obtener_productos_por_id_nuevo_ingreso(self, id_nuevo_ingreso):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        consulta = """
        SELECT nombre_producto, series_producto
        FROM Productos
        WHERE id_nuevoingreso = ?;
        """
        cursor = connection.cursor()
        cursor.execute(consulta, (id_nuevo_ingreso,))
        resultados = cursor.fetchall()
        cursor.close()
        db_connection.close_connection()
        return resultados

    def obtener_numero_guia_por_id(self, id_nuevo_ingreso):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        query = """
        SELECT nombre_guia
        FROM NuevoIngreso
        WHERE id_nuevoingreso = ?;
        """
        cursor = connection.cursor()
        cursor.execute(query, (id_nuevo_ingreso,))
        resultado = cursor.fetchone()
        cursor.close()
        db_connection.close_connection()
        if resultado:
            return resultado[0]
        else:
            print(f"No se encontró número de guía para el ID de nuevo ingreso {id_nuevo_ingreso}.")
            return None

    def obtener_nombre_empresa_por_id(self, id_nuevo_ingreso):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        query = """
        SELECT nombre_empresa
        FROM NuevoIngreso
        WHERE id_nuevoingreso = ?;
        """
        cursor = connection.cursor()
        cursor.execute(query, (id_nuevo_ingreso,))
        resultado = cursor.fetchone()
        cursor.close()
        db_connection.close_connection()
        if resultado:
            return resultado[0]
        else:
            print(f"No se encontró nombre de empresa para el ID de nuevo ingreso {id_nuevo_ingreso}.")
            return None

    def obtener_ruta_guia_por_id(self, id_nuevo_ingreso):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        query = """
        SELECT path_guia
        FROM NuevoIngreso
        WHERE id_nuevoingreso = ?;
        """
        cursor = connection.cursor()
        cursor.execute(query, (id_nuevo_ingreso,))
        resultado = cursor.fetchone()
        cursor.close()
        db_connection.close_connection()
        if resultado:
            return resultado[0]
        else:
            print(f"No se encontró ruta de la guía para el ID de nuevo ingreso {id_nuevo_ingreso}.")
            return None

    def obtener_ruta_factura_por_id(self, id_nuevo_ingreso):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        query = """
        SELECT path_factura
        FROM NuevoIngreso
        WHERE id_nuevoingreso = ?;
        """
        cursor = connection.cursor()
        cursor.execute(query, (id_nuevo_ingreso,))
        resultado = cursor.fetchone()
        cursor.close()
        db_connection.close_connection()
        if resultado:
            return resultado[0]
        else:
            print(f"No se encontró ruta de la factura para el ID de nuevo ingreso {id_nuevo_ingreso}.")
            return None

    def buscar_por_numero_guia(self, termino_busqueda):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        query = """
        SELECT id_nuevoingreso
        FROM NuevoIngreso
        WHERE nombre_guia LIKE ?;
        """
        cursor = connection.cursor()
        cursor.execute(query, (f'%{termino_busqueda}%',))
        resultados = cursor.fetchall()
        cursor.close()
        db_connection.close_connection()
        return [resultado[0] for resultado in resultados]

    def buscar_por_nombre_empresa(self, termino_busqueda):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        query = """
        SELECT id_nuevoingreso
        FROM NuevoIngreso
        WHERE nombre_empresa LIKE ?;
        """
        cursor = connection.cursor()
        cursor.execute(query, (f'%{termino_busqueda}%',))
        resultados = cursor.fetchall()
        cursor.close()
        db_connection.close_connection()
        return [resultado[0] for resultado in resultados]

    def buscar_por_nombre_producto(self, termino_busqueda):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        query = """
        SELECT id_nuevoingreso
        FROM Productos
        WHERE nombre_producto LIKE ?;
        """
        cursor = connection.cursor()
        cursor.execute(query, (f'%{termino_busqueda}%',))
        resultados = cursor.fetchall()
        cursor.close()
        db_connection.close_connection()
        return [resultado[0] for resultado in resultados]

    def buscar_por_serie_producto(self, termino_busqueda):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        query = """
        SELECT id_nuevoingreso
        FROM Productos
        WHERE series_producto LIKE ?;
        """
        cursor = connection.cursor()
        cursor.execute(query, (f'%{termino_busqueda}%',))
        resultados = cursor.fetchall()
        cursor.close()
        db_connection.close_connection()
        return [resultado[0] for resultado in resultados]
    
    def obtener_nuevo_ingreso_por_id(self, id_nuevoingreso):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        query = """
        SELECT *
        FROM NuevoIngreso
        WHERE id_nuevoingreso = ?;
        """
        cursor = connection.cursor()
        cursor.execute(query, (id_nuevoingreso,))
        resultado = cursor.fetchone()
        cursor.close()
        db_connection.close_connection()
        return resultado