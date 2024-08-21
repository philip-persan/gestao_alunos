from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from professor.models import Professor
from turma.models import Turma
from users.models import User


class TurmaTests(APITestCase):

    def setUp(self):
        self.professor_user = User.objects.create_user(
            username='professor1',
            password='prof123',
            is_staff=True
        )
        self.professor = Professor.objects.get(
            user=self.professor_user
        )
        self.turma = Turma.objects.create(
            nome='Turma A', ano=2024, professor=self.professor
        )

    def test_create_turma(self):
        self.client.login(username='professor1', password='prof123')
        data = {
            'nome': 'Turma B', 'ano': 2024,
            'professor_id': self.professor.id
        }
        response = self.client.post(reverse('turma-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_turma_list(self):
        self.client.login(username='professor1', password='prof123')
        response = self.client.get(reverse('turma-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Turma A')
