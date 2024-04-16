from app.data.db_connection import DatabaseConnection
import sqlite3

class DatabaseQueries:
<<<<<<< HEAD
    @staticmethod
    def insertar_nuevo_ingreso(numero_guia, nombre_empresa, cantidad_productos, fecha, ruta_guia, ruta_factura):
        db_connection = DatabaseConnection()
        connection = db_connection.connection
        cursor = connection.cursor()
        query = """
            INSERT INTO NuevoIngreso (nombre_guia, nombre_empresa, cantidad_productos, fecha_guia, path_guia, path_factura, save_data)
            VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
=======

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def _execute_query(self, query, parameters=None):
        cursor = self.db_connection.connection.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        self.db_connection.commit()
        return cursor.fetchall()

    def insert_nuevo_registro(self, data):
        query = """
        INSERT INTO NuevoIngreso
        (nombre_guia, nombre_empresa, cantidad_productos, fecha_guia, save_data, path_guia, path_factura,
        nombre_producto, descripcion_producto, series_producto)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3
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

<<<<<<< HEAD
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
=======
    def list_resumen_nuevoingreso(self, id_nuevoingreso=None):
        query = """
        SELECT id_NuevoIngreso AS id, nombre_guia AS guia, nombre_empresa AS empresa,
        cantidad_productos AS cantidadproductos, fecha_guia AS fecha
        FROM NuevoIngreso
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3
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

<<<<<<< HEAD
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
=======
    def search_products_by_id_nombre(self, id_nuevoingreso):
        query = """
        SELECT nombre_producto
        FROM NuevoIngreso
        WHERE id_NuevoIngreso = ?
        """
        parameters = [id_nuevoingreso]
        return self._execute_query(query, parameters)[0][0]

    def search_products_by_id_descripcion(self, id_nuevoingreso):
        query = """
        SELECT descripcion_producto
        FROM NuevoIngreso
        WHERE id_NuevoIngreso = ?
        """
        parameters = [id_nuevoingreso]
        return self._execute_query(query, parameters)[0][0]

    def search_products_by_id_serie(self, id_nuevoingreso):
        query = """
        SELECT series_producto
        FROM NuevoIngreso
        WHERE id_NuevoIngreso = ?
        """
        parameters = [id_nuevoingreso]
        return self._execute_query(query, parameters)[0][0]

    def search_by_guia(self, texto_busqueda):
        query = """
        SELECT id_NuevoIngreso
        FROM NuevoIngreso
        WHERE nombre_guia LIKE ?
        """
        parameters = [texto_busqueda + '%']
        return self._execute_query(query, parameters)

    def search_by_empresa(self, texto_busqueda):
        query = """
        SELECT id_NuevoIngreso
        FROM NuevoIngreso
        WHERE nombre_empresa LIKE ?
        """
        parameters = [texto_busqueda + '%']
        return self._execute_query(query, parameters)

    def search_by_nombre_producto(self, texto_busqueda):
        query = """
        SELECT id_NuevoIngreso
        FROM NuevoIngreso
        WHERE nombre_producto LIKE ?
        """
        parameters = ['%' + texto_busqueda + '%']
        return self._execute_query(query, parameters)
    
    def search_by_serie(self, serie):
        query = """
        SELECT id_NuevoIngreso
        FROM NuevoIngreso
        WHERE series_producto LIKE ?
        """
        parameters = ['%' + serie + '%']
        return self._execute_query(query, parameters)

    def obtener_datos_completos(self, id_nuevoingreso):
        query = """
        SELECT nombre_guia AS guia, nombre_empresa AS empresa, cantidad_productos AS cantidadproductos, fecha_guia AS fecha
        FROM NuevoIngreso
        WHERE id_NuevoIngreso = ?
        """
        parameters = [id_nuevoingreso]
        return self._execute_query(query, parameters)
>>>>>>> fff2bea02c1bbc8789861e2a41313d6c3710e4d3
