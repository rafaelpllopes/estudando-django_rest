from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):
    def setUp(self) -> None:
        self.list_url = reverse("programas-list")
        self.user = User.objects.create_user("c3po", password="123456")

    def test_autencacao_user_com_credenciais_corretas(self) -> None:
        """Teste que verifica a autenticação de um user com as credenciais correta"""
        user = authenticate(username="c3po", password="123456")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self) -> None:
        """Teste que verifica uma requisição GET não autorizada"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticacao_de_user_com_username_incorreto(self) -> None:
        """Teste que verifica autenticação de um user com username incorreto"""
        user = authenticate(username="c3pp", password="123456")
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authenticacao_de_user_com_password_incorreto(self) -> None:
        """Teste que verifica autenticação de um user com password incorreto"""
        user = authenticate(username="c3po", password="654321")
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_com_user_autenticado(self) -> None:
        """Teste que verifica uma requisição GET de um user autenticado"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
