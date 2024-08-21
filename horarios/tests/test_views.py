from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from disciplina.models import Disciplina
from horarios.models import Horario
from professor.models import Professor
from turma.models import Turma
from users.models import User


class HorarioTests(APITestCase):

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
            professor=self.professor,
            nome='Turma Teste',
            ano=2024
        )
        self.disciplina = Disciplina.objects.create(
            nome='Disciplina Teste'
        )
        self.horario = Horario.objects.create(
            turma=self.turma,
            disciplina=self.disciplina,
            dia_semana='Segunda',
            hora_inicio='08:00:00',
            hora_fim='10:00:00'
        )

    def test_create_horario(self):
        self.client.login(username='professor1', password='prof123')
        url = reverse('horarios-list')
        data = {
            'turma_id': self.turma.id,
            'disciplina_id': self.disciplina.id,
            'dia_semana': 'Quarta',
            'hora_inicio': '10:00:00',
            'hora_fim': '12:00:00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Horario.objects.count(), 2)
        self.assertEqual(Horario.objects.latest('id').dia_semana, 'Quarta')

    def test_get_horario_detail(self):
        self.client.login(username='professor1', password='prof123')
        url = reverse('horarios-detail', args=[self.horario.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['dia_semana'], 'Segunda')
        self.assertEqual(response.data['hora_inicio'], '08:00:00')

    def test_update_horario(self):
        self.client.login(username='professor1', password='prof123')
        url = reverse('horarios-detail', args=[self.horario.id])
        data = {
            'dia_semana': 'Sexta',
            'hora_inicio': '14:00:00',
            'hora_fim': '16:00:00'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.horario.refresh_from_db()
        self.assertEqual(self.horario.dia_semana, 'Sexta')
        self.assertEqual(self.horario.hora_inicio, '14:00:00')

    def test_delete_horario(self):
        self.client.login(username='professor1', password='prof123')
        url = reverse('horarios-detail', args=[self.horario.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Horario.objects.count(), 0)
