from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from professor.models import Professor
from users.models import User


class ProfessorTests(APITestCase):
    def setUp(self):
        # Criação de um usuário regular
        self.regular_user = User.objects.create_user(
            username='professor1',
            email='professor1@example.com',
            password='testpass123'
        )

    def test_professor_created_on_user_creation(self):
        """
        Testa se o Professor é criado automaticamente ao criar um usuário.
        """
        # Verifica se o Professor foi criado para o usuário regular
        professor_exists = Professor.objects.filter(
            user=self.regular_user).exists()
        self.assertTrue(professor_exists)

    def test_get_professor_detail(self):
        """
        Testa se os detalhes de um professor podem ser acessados.
        """
        # Recupera o professor criado automaticamente
        professor = Professor.objects.get(user=self.regular_user)

        url = reverse('professor-detail', args=[professor.id])
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Acessa o campo 'user' dentro do objeto 'response.data'
        self.assertEqual(
            response.data['user']['id'],
            str(self.regular_user.id)
        )

    def test_update_professor(self):
        """
        Testa se as informações do professor podem ser atualizadas.
        """
        professor = Professor.objects.get(user=self.regular_user)
        url = reverse('professor-detail', args=[professor.id])

        # Atualiza informações do professor
        data = {'formacao': 'Updated formacao'}
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se o campo foi atualizado
        professor.refresh_from_db()
        self.assertEqual(professor.formacao, 'Updated formacao')
