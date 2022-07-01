from src.modelo.asig import Asignatura
from src.modelo.declarative_base import Base, engine, Session
from src.logica.Sorteo import Sorteo
from src.logica.Sorteo import agregar_asignatura

def añadeRegistos():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()

    asignatura1 = Asignatura(nombasig="Análisis y diseño de sistemas")
    asignatura2 = Asignatura(nombasig="Pruebas  de software")
    session.add(asignatura1)
    session.add(asignatura2)
    session.commit()
    session.close()


def eliminarRegistros():
    session = Session()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session.commit()
    session.close()


if __name__ == '__main__':
    edit = Sorteo()

    while True:
        print("0 Salir")
        print("1 Añadir registros")
        print("2 Eliminar registros")
        print("3 Editar registros")
        opcion = int(input("Opción: "))
        if opcion == 0:
            print("Fin...")
            break
        elif opcion == 1:
            añadeRegistos()

            print("Registros añadidos")
        elif opcion == 2:
            eliminarRegistros()

            print("Registros eliminados")
        elif opcion == 3:
            agregar_asignatura(2)
            print("editado")
        else:
            print("Opción incorrecta")
        print("\n\n\n")

