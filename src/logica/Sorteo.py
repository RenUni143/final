from src.modelo.asig import Asignatura
from src.modelo.declarative_base import engine, Base, session


def agregar_asignatura(idAsignatura):
    session.query(Asignatura).filter(Asignatura.id == idAsignatura).update({Asignatura.nombasig: 'construccion de '
                                                                                                 'software'})
    session.commit()
    session.close()


class Sorteo():

    def __init__(self):
        Base.metadata.create_all(engine)