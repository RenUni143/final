from src.modelo.asig import Asignatura
from src.modelo.declarative_base import engine, Base, session


def agregar_asignatura(idAsignatura):
    busqueda = session.query(Asignatura).filter(Asignatura.id == idAsignatura).first()

    if busqueda:
        session.query(Asignatura).filter(Asignatura.id == idAsignatura).update({Asignatura.nombasig: 'construccion de '
                                                                                                     'software'})
        print("editado")
        session.commit()
        session.close()


class Sorteo():

    def __init__(self):
        Base.metadata.create_all(engine)