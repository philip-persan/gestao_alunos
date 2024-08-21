import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from professor.models import Professor
from turma.models import Aluno, Turma
from users.models import User


class AlunoTests(APITestCase):

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
            nome='Turma A',
            ano=2024,
            professor=self.professor
        )
        self.aluno = Aluno.objects.create(
            nome_completo='João Silva',
            data_nascimento=datetime.date(2005, 1, 1),
            turma=self.turma
        )

    def test_create_aluno(self):
        self.client.login(username='professor1', password='prof123')
        data = {
            'nome_completo': 'Maria Souza',
            'data_nascimento': '2006-02-01',
            'turma_id': self.turma.id
        }
        response = self.client.post(reverse('aluno-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_aluno_detail(self):
        self.client.login(username='professor1', password='prof123')
        response = self.client.get(
            reverse('aluno-detail', args=[self.aluno.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome_completo'], 'João Silva')
