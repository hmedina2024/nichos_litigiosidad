from sqlalchemy.orm import sessionmaker
from sqlalchemy import text, func
from conexion.db import get_db_connection
from conexion.modelos import DailyConciliacionExtrajudicial

def buscar_conciliacion_por_iuc(iuc):
    """
    Busca un proceso de conciliación por su IUC en la base de datos.
    """
    connection = get_db_connection()
    if not connection:
        return None

    Session = sessionmaker(bind=connection.engine)
    session = Session()
    
    try:
        # Realiza la consulta para encontrar el primer registro que coincida con el IUC
        # Compara el IUC ignorando espacios en blanco al inicio y al final
        # Compara el IUC ignorando espacios y mayúsculas/minúsculas
        proceso = session.query(DailyConciliacionExtrajudicial).filter(func.lower(func.trim(DailyConciliacionExtrajudicial.IUC)) == iuc.lower().strip()).first()
        return proceso
    except Exception as e:
        print(f"Error durante la consulta: {e}")
        return None
    finally:
        session.close()
        connection.close()

def obtener_intervinientes_por_iuc(iuc):
    """
    Ejecuta una consulta SQL para obtener y procesar los intervinientes de un caso.
    """
    connection = get_db_connection()
    if not connection:
        return []

    # La consulta SQL proporcionada por el usuario
    sql_query = text("""
        WITH INTERV AS (
            SELECT *,
                LTRIM(RTRIM(value)) AS DataColumn
            FROM [EXT].[DAILY_INTERVENCION] AS sub
            CROSS APPLY STRING_SPLIT(sub.INTERVINIENTES_CASO, '*')
            WHERE value <> ''
                AND INTERVINIENTES_NRO > 1
                AND LOWER(TRIM(IUC)) = LOWER(:iuc_param)
        )
        SELECT
            CASE
                WHEN CHARINDEX(':', V.value) > 0
                THEN TRIM(SUBSTRING(V.value, 1, CHARINDEX(':', V.value)-1))
                ELSE NULL
            END AS Tipo,
            CASE
                WHEN CHARINDEX(':', V.value) > 0
                     AND CHARINDEX(' ', V.value, CHARINDEX(':', V.value)) > CHARINDEX(':', V.value)
                THEN TRIM(SUBSTRING(V.value,
                                    CHARINDEX(':', V.value) + 2,
                                    CHARINDEX(' ', V.value, CHARINDEX(':', V.value)) - CHARINDEX(':', V.value)+2))
                ELSE NULL
            END AS Tipo_Identificacion,
            CASE
                WHEN CHARINDEX(' ', V.value, CHARINDEX(':', V.value)) > 0
                     AND CHARINDEX('-', V.value) > CHARINDEX(' ', V.value, CHARINDEX(':', V.value))
                THEN TRIM(SUBSTRING(V.value,
                                    CHARINDEX(' ', V.value, CHARINDEX(':', V.value)) + 4,
                                    CHARINDEX('-', V.value) - CHARINDEX(' ', V.value, CHARINDEX(':', V.value)) - 4))
                ELSE NULL
            END AS Identificacion,
            CASE
                WHEN CHARINDEX('-', V.value) > 0
                THEN TRIM(SUBSTRING(V.value, CHARINDEX('-', V.value) + 1, LEN(V.value)))
                ELSE NULL
            END AS Nombre
        FROM INTERV
        CROSS APPLY STRING_SPLIT(REPLACE(DataColumn, CHAR(10), '|'), '|') AS V
        WHERE TRIM(V.value) <> '';
    """)

    try:
        result = connection.execute(sql_query, {'iuc_param': iuc})
        # Convertimos el resultado a una lista de diccionarios para que sea más fácil de usar
        intervinientes = [dict(row) for row in result.mappings()]
        return intervinientes
    except Exception as e:
        print(f"Error durante la consulta de intervinientes: {e}")
        return []
    finally:
        connection.close()