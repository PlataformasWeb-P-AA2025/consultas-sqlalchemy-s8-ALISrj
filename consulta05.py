from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from clases import *
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos todos los cursos
cursos = session.query(Curso).all()

for curso in cursos:
    # Creamos una variable llamada promedio con valor igual a 0
    promedio = 0
    # Obtenemos todas las entregas de cada curso, para eso mediante JOIN's viajamos hasta la tabla de Curso
    # una entrega pertenece a una Tarea, una tarea fue mandada en un Curso
    entregas = session.query(Entrega).join(Tarea).join(Curso).filter(Curso.id==curso.id).all()
    # Si tenemos más de 0 entregas, calculamos el promedio de las existentes
    if len(entregas) > 0:
        for entrega in entregas:
            promedio += entrega.calificacion
        promedio = promedio / len(entregas)
    # Si no tenemos ninguna entrega, el promedio lo asignamos a 0
    else:
        promedio = 0
    print(f"Curso: f{curso.id} - {curso.titulo}\nPromedio de calificaciones del curso: {format(promedio, '.2f')}")