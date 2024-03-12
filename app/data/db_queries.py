class DatabaseQueries:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def _execute_query(self, query, parameters=None):
        cursor = self.db_connection.connection.cursor()
        cursor.execute(query, parameters)
        self.db_connection.commit()
        return cursor.fetchall()  # Retorna los resultados para su recuperación

    def insert_nuevo_registro(self, data):
        query = """
            INSERT INTO NuevoIngreso
            (nombre_guia, nombre_empresa, cantidad_productos, fecha_guia, save_data, path_guia, path_factura,
             nombre_producto, descripcion_producto, series_producto)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self._execute_query(query, data)

    # def select_last_nuevo_registro_id(self):
    #     query = "SELECT id_NuevoIngreso FROM NuevoIngreso ORDER BY id_NuevoIngreso DESC LIMIT 1"
    #     result = self._execute_query(query)
    #     return result[0][0] if result else None  # Accede al primer elemento de la primera fila

    def list_resumen_nuevoingreso(self):
        query = """
            SELECT id_NuevoIngreso AS id, nombre_guia AS guia, nombre_empresa AS empresa,
                   cantidad_productos AS cantidadproductos, fecha_guia AS fecha
            FROM NuevoIngreso
        """
        return self._execute_query(query)

