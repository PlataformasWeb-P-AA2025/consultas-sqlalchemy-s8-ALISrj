from sqlalchemy.orm import sessionmaker
from clases import *
from config import cadena_base_datos
from clases import Entrega, Departamento

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. En función de la entrega,
# presentar, nombre del tarea, nombre del estudiante, calificación, nombre de instructor y nombre del departamento

# Para poder filtrar de acuerdo al nombre del departamento y obtener las entregas, viajamos con JOIN's, hasta la tabla de departamento
# , para armar el camino, debemos conocer las relaciones entre las tablas, para finalmente poder filtrar por el nombre del departamento.
# Una entrega pertenece a una tarea, una tarea fue solicitada en un curso, un curso pertenece a un departamento.
entregas = session.query(Entrega).join(Tarea).join(Curso).join(Departamento).filter(Departamento.nombre.like("Arte")).all()

for e in entregas:
    print(f"Nombre de la Tarea: {e.tarea.titulo}\n"
          f"Nombre del estudiante: {e.estudiante.nombre}\n"
          f"Calificacion: {e.calificacion}\n"
          f"Nombre del instructor: {e.tarea.curso.instructor.nombre}\n"
          f"Nombre del departamento: {e.tarea.curso.departamento.nombre}\n"
          f"_____________________________________________________________________\n\n")