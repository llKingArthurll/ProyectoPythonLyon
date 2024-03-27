class DatabaseQueries:

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
        """
        self._execute_query(query, data)

    def list_resumen_nuevoingreso(self, id_nuevoingreso=None):
        query = """
        SELECT id_NuevoIngreso AS id, nombre_guia AS guia, nombre_empresa AS empresa,
        cantidad_productos AS cantidadproductos, fecha_guia AS fecha
        FROM NuevoIngreso
        """
        return self._execute_query(query)

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