from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from clases import *
from config import cadena_base_datos

from clases import Entrega, Departamento

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

entregas = session.query(Entrega).join(Tarea).join(Curso).join(Departamento).filter(Departamento.nombre.like("Arte")).all()

for e in entregas:
    print(f"Nombre de la Tarea: {e.tarea.titulo}\n"
          f"Nombre del estudiante: {e.estudiante.nombre}\n"
          f"Calificacion: {e.calificacion}\n"
          f"Nombre del instructor: {e.tarea.curso.instructor.nombre}\n"
          f"Nombre del departamento: {e.tarea.curso.departamento.nombre}\n"
          f"_____________________________________________________________________\n\n")