from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def get_db_connection():
    """
    Crea y retorna una conexión a la base de datos de SQL Server usando SQLAlchemy.
    """
    try:
        # Reemplaza los siguientes valores con los de tu configuración
        server = 'sql-back-p.database.windows.net'
        database = 'sql-back-dwh'
        username = 'pgn_ms_analitica_bd'
        password = 'j/V3XwWXNP+a$6.4'
        
        # Cadena de conexión para SQL Server
        conn_str = (
            f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
        )
        engine = create_engine(conn_str)
                        
        # engine.connect() es la forma correcta de obtener una conexión del pool
        conn = engine.connect()
        print("Conexión a la base de datos exitosa.")
        return conn
    except SQLAlchemyError as ex:
        print(f"Error de conexión a la base de datos: {ex}")
        return None

if __name__ == '__main__':
    # Ejemplo de uso
    connection = get_db_connection()
    if connection:
        # Con SQLAlchemy, un cursor no es usualmente necesario.
        # Puedes ejecutar consultas directamente.
        # from sqlalchemy import text
        # result = connection.execute(text("SELECT @@VERSION;"))
        # for row in result:
        #     print(row[0])
        connection.close()
        print("Conexión cerrada.")