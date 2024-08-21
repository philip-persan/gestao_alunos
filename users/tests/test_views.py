from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class UserTests(APITestCase):

    def setUp(self):
        # Criando um usuário admin e um usuário normal para os testes
        self.admin_user = User.objects.create_superuser(
            username="admin2",
            email="admin@example.com",
            password="adminpassword"
        )
        self.regular_user = User.objects.create_user(
            username="regularuser",
            first_name="User",
            last_name="Teste",
            email="user@example.com",
            password="userpassword"
        )
        self.client.force_authenticate(user=self.admin_user)

    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'first_name': 'User',
            'last_name': 'Teste',
            'username': 'normaluser',
            'email': 'normaluser@email.com',
            'telefone': '11223344556',
            'password': 'newpassword',
            'is_active': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)

    def test_retrieve_users_admin(self):
        # Testando se o admin consegue listar todos os usuários
        url = reverse('user-admin-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Deve retornar 2 usuários

    def test_regular_user_cannot_see_all_users(self):
        # Testando se o usuário comum não consegue ver todos os usuários
        self.client.force_authenticate(user=self.regular_user)
        url = reverse('user-admin-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user(self):
        url = reverse('user-detail', args=[self.regular_user.id])
        data = {'email': 'updateduser@example.com'}
        response = self.client.patch(url, data, format='json')

        # Adicione debug prints
        print(f"Status Code: {response.status_code}")
        print(f"Response Data: {response.data}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        # Print do email atualizado
        print(f"Updated Email: {self.regular_user.email}")
        self.assertEqual(self.regular_user.email, 'updateduser@example.com')

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.regular_user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 1)
