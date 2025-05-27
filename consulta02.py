from sqlalchemy.orm import sessionmaker
from clases import *
from config import cadena_base_datos
from clases import Entrega, Departamento

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 . En función de los departamentos,
# presentar el nombre del departamento y el número de cursos que tiene cada departamento

# Para encontrar los departamentos que tienen entregas menores o iguales a 0.3, armamos el camino mediante JOIN's,
# hasta llegar a la tabla de entregas y filtrar por la calificación.
# Un departamento tiene cursos, en un curso manda tareas, las tareas tienen entregas.
departamentos = session.query(Departamento).join(Curso).join(Tarea).join(Entrega).filter(Entrega.calificacion <= 0.3).all()

for d in departamentos:
    print(f"""
        Nombre del departamento: {d.nombre}
        Número de cursos del departamento: {len(d.cursos)}
""")