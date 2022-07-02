from src.modelo.asig import Asignatura
from src.modelo.declarative_base import engine, Base, session


def agregar_asignatura(idAsignatura):
    busqueda = session.query(Asignatura).filter(Asignatura.id == idAsignatura).first()
    if len(busqueda) == 1:
        session.query(Asignatura).filter(Asignatura.id == idAsignatura).update({Asignatura.nombasig: 'construccion de '
                                                                                                     'software'})
        print("editado")
        session.commit()
        session.close()

        return True
    elif len(busqueda) == 0:
        print("la asignatura con el id ", idAsignatura, "no existe")


class Sorteo():

    def __init__(self):
        Base.metadata.create_all(engine)