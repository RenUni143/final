import unittest
from datetime import datetime
from src.modelo.asig import Asignatura
from src.logica.Sorteo import Sorteo
from src.modelo.declarative_base import Session
from src.logica.Sorteo import agregar_asignatura


class AsignaturaTestCase(unittest.TestCase):
    def setUp(self):
        session = Session()

        self.sorteo = Sorteo()

        self.session = Session()

        asignatura1 = Asignatura(nombasig="Análisis y diseño de sistemas")
        asignatura2 = Asignatura(nombasig="Pruebas  de software")
        session.add(asignatura1)
        session.add(asignatura2)
        session.commit()
        session.close()

        self.session.close()

    def tearDown(self):
        self.session = Session()
        asignaturas = self.session.query(Asignatura).all()
        for asignatura in asignaturas:
            self.session.delete(asignatura)
        self.session.commit()
        self.session.close()

    def test_editar_asignatura(self):
        resultado = agregar_asignatura(1)
        self.assertEqual(resultado, print("editado"))

    def test_editar_asignatura_noencontrada(self):
        resultado = agregar_asignatura(3)
        self.assertEqual(resultado, None)



