from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from professor.models import Professor
from users.models import User

from ..models import Disciplina


class ProfessorTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            username='professor1',
            email='professor1@example.com',
            password='testpass123',
            is_staff=True
        )
        self.professor = Professor.objects.get(
            user=self.admin_user
        )
        self.disciplina = Disciplina.objects.create(
            nome='Física',
        )

    def test_create_disciplina(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('disciplina-list')
        data = {'nome': 'História'}
        response = self.client.post(url, data, format='json')
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Data: {response.data}")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Disciplina.objects.latest('id').nome, 'História')

    def test_get_disciplina_detail(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('disciplina-detail', args=[self.disciplina.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Física')

    def test_update_disciplina(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('disciplina-detail', args=[self.disciplina.id])
        data = {'nome': 'Sociologia'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.disciplina.refresh_from_db()
        self.assertEqual(self.disciplina.nome, 'Sociologia')

    def test_delete_disciplina(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('disciplina-detail', args=[self.disciplina.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
