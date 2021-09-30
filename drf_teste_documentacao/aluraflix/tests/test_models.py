from aluraflix.models import Programa
from django.test import TestCase


class ProgramaModelTestCase(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo="Procurando niguem",
            data_lancamento="2003-07-04",
        )

    def test_verifica_atributos_do_programa(self):
        """Teste que verifica os atributos de um programa com valores default"""
        self.assertEqual(self.programa.titulo, "Procurando niguem")
        self.assertEqual(self.programa.tipo, "F")
        self.assertEqual(self.programa.data_lancamento, "2003-07-04")
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)