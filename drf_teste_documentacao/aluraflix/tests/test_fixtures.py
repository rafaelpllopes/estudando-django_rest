from aluraflix.models import Programa
from django.test import TestCase


class FixtureDataTestCase(TestCase):
    fixtures = ["programas_iniciais"]

    def test_verifica_carregamento_da_fixtures(self):
        programa_bizarro = Programa.objects.get(pk=1)
        todos_os_programas = Programa.objects.all()

        self.assertEqual(programa_bizarro.titulo, "Coisas bizarras")
        self.assertEqual(len(todos_os_programas), 9)
