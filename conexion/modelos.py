from sqlalchemy import (
    create_engine,
    Column,
    String,
    DateTime,
    Numeric,
    Float,
    Text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crea una base declarativa
Base = declarative_base()

# Define el modelo para la tabla DAILY_DISCIPLINARIO_PROCESO
class DailyDisciplinarioProceso(Base):
    __tablename__ = 'DAILY_DISCIPLINARIO_PROCESO'
    __table_args__ = {'schema': 'EXT'}

    ID_CASO = Column(Text, primary_key=True) # Asumiendo ID_CASO como clave primaria para el modelo
    IUS = Column(String(50))
    IUC = Column(String(50))
    FECHA_SIM = Column(DateTime)
    FECHA_PGN = Column(DateTime)
    ESTADO_CASO = Column(String(8))
    OBJETO_EVALUACION = Column(String(100))
    IND_DUPLICIDAD = Column(String(15))
    IND_OFICIO = Column(String(2))
    MUNICIPIO_HECHOS = Column(String(100))
    DEPARTAMENTO_HECHOS = Column(String(50))
    FECHA_HECHOS = Column(DateTime)
    COD_DEPENDENCIA_TITULAR = Column(String(15))
    DEPENDENCIA_TITULAR = Column(String(200))
    COD_DEPENDENCIA_SUPERIOR = Column(String(15))
    DEPENDENCIA_SUPERIOR = Column(String(200))
    EXTERNO_IDENTIFICACION = Column(String(100))
    EXTERNO_ASUNTO = Column(String(100))
    EXTERNO_TRAMITE = Column(String(100))
    ETAPA_ACTUAL = Column(String(303))
    ETAPA_DECISION = Column(String(200))
    ETAPA_FECHA = Column(DateTime)
    DECISION_FECHA = Column(DateTime)
    DECISION_INSTANCIA = Column(String(200))
    DECISION_TIPO = Column(String(200))
    TAREA_PROCESO = Column(String(100))
    TAREA_ACTIVIDAD = Column(String(100))
    TAREA_ESTADO = Column(String(50))
    TAREA_FECHA = Column(DateTime)
    TAREA_DEPENDENCIA = Column(String(200))
    DESC_SOLICITUD = Column(String(4000))
    DESC_HECHOS = Column(String(4000))
    DESC_SITIOHECHOS = Column(String(500))
    JUST_CIERRE = Column(String(4000))
    ENTIDADES_CASO = Column(String(4000))
    CONDUCTAS_CASO = Column(String(4000))
    INTERVINIENTES_CASO = Column(String(4000))
    INTERVINIENTES_NRO = Column(Numeric(5, 0))
    IMPLICADOS_CASO = Column(String(4000))
    IMPLICADOS_NRO = Column(Numeric(5, 0))
    ID_TIPO_CASO = Column(Text)
    TIPO_TRASLADO = Column(String(16))
    REMITE_ENTIDAD = Column(String(200))
    REGIMEN = Column(String(100))
    FECHA_PRESCRIPCION = Column(DateTime)
    FECHA_APERTURA_INVESTIGACION = Column(DateTime)
    COD_DEPENDENCIA_DECISION = Column(String(15))
    DEPENDENCIA_DECISION = Column(String(200))
    COD_DEP_SEGUNDA_INSTANCIA = Column(String(15))
    DEP_SEGUNDA_INSTANCIA = Column(String(200))
    RIESGO = Column(String(100))
    TERMINO = Column(String(4))
    ESTADO_CASO_CT = Column(String(7))
    FECHA_FIN = Column(DateTime)
    DIAS_FIN = Column(Float)


# Define el modelo para la tabla DAILY_CONCILIACION_EXTRAJUDICIAL
class DailyConciliacionExtrajudicial(Base):
    __tablename__ = 'DAILY_CONCILIACION_EXTRAJUDICIAL'
    __table_args__ = {'schema': 'EXT'}

    ID_CASO = Column(Text, primary_key=True) # Asumiendo ID_CASO como clave primaria
    IUS = Column(String(50))
    IUC = Column(String(50))
    FECHA_SIM = Column(DateTime)
    FECHA_PGN = Column(DateTime)
    ESTADO_CASO = Column(String(100))
    COD_DEPENDENCIA_CASO = Column(String(50))
    DEPENDENCIA_CASO = Column(String(200))
    COD_DEPENDENCIA_SUP_CASO = Column(String(50))
    DEPENDENCIA_SUP_CASO = Column(String(200))
    FUNC_CASO = Column(Text)
    TIPO_PROCESO = Column(String(100))
    CLASE_PROCESO = Column(String(100))
    NOMBRE_PROCESO = Column(String(200))
    CONVOCANTES = Column(Text)
    CONVOCADOS = Column(Text)
    ID_CONCILIACION = Column(String(100))
    TEMA_AUDIENCIA = Column(Text)
    FEC_EXPEDICION = Column(DateTime)
    NRO_CONCILIACION = Column(String(50))
    DECISION = Column(Text)
    FEC_AUDIENCIA = Column(DateTime)
    RESULTADO_AUDIENCIA = Column(Text)
    VR_PRETENDIDO = Column(Numeric(18, 2))
    VR_CONCILIADO = Column(Numeric(18, 2))
    SALDO = Column(Numeric(18, 2))
    COD_DEPENDENCIA_CONCILIA = Column(String(50))
    DEPENDENCIA_CONCILIA = Column(String(200))
    COD_DEPENDENCIA_SUP_CONCILIA = Column(String(50))
    DEPENDENCIA_SUP_CONCILIA = Column(String(200))
    SERV_CONCILIADOR = Column(String(200))
    CJ_FECHAJURISDICCION = Column(DateTime)
    CJ_DESPACHO = Column(String(200))
    CJ_DECISION = Column(Text)
    CJ_FECHADECISION = Column(DateTime)
    ID_TAREA = Column(String(100))
    PROCESO = Column(String(200))
    ACTIVIDAD = Column(String(200))
    FEC_TAREA = Column(DateTime)
    EST_TAREA = Column(String(100))
    DESC_SOLICITUD = Column(Text)
    DESC_HECHOS = Column(Text)
    ID_RESULTADOAUDIENCIA = Column(String(100))


# Ejemplo de cómo usarlo (opcional, para pruebas)
if __name__ == '__main__':
    from db import get_db_connection

    connection = get_db_connection()
    if connection:
        # Crea una sesión
        Session = sessionmaker(bind=connection.engine)
        session = Session()

        # Ejemplo de consulta
        # primer_proceso = session.query(DailyDisciplinarioProceso).first()
        # if primer_proceso:
        #     print(f"ID_CASO: {primer_proceso.ID_CASO}, IUS: {primer_proceso.IUS}")

        session.close()
        connection.close()