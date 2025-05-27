from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from clases import *
from config import cadena_base_datos
from clases import Entrega, Departamento

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtener todas las tareas asignadas a los siguientes estudiantes
#
# Jennifer Bolton
# Elaine Perez
# Heather Henderson
# Charles Harris
#
# En función de cada tarea, presentar el número de entregas que tiene

# Para poder filtrar por los nombres de los estudiantes, armamos el camino mediante JOIN's, hasta la tabla de estudiantes
# una vez ahí, mediante un or_, escribimos todas las sentencias, a evaluar, que serián los nombres específicos de los estudiantes
# solicitados
tareas = session.query(Tarea).join(Entrega).join(Estudiante).filter(or_(
    Estudiante.nombre == "Jennifer Bolton",
    Estudiante.nombre == "Elaine Perez",
    Estudiante.nombre == "Heather Henderson",
    Estudiante.nombre == "Charles Harris"
))

for t in tareas:
    print(f"""
Tarea: {t.id} - {t.titulo}
Número de entregas: {len(t.entregas)}
""")
