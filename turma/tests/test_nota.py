import datetime

from django.core.exceptions import ValidationError
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from disciplina.models import Disciplina
from professor.models import Professor
from turma.models import Aluno, Nota, Turma
from users.models import User


class NotaTests(APITestCase):

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
        self.disciplina = Disciplina.objects.create(
            nome='Matemática'
        )
        self.nota = Nota.objects.create(
            aluno=self.aluno,
            turma=self.turma,
            disciplina=self.disciplina,
            valor_nota=9.5,
            data_lancamento=datetime.date.today()
        )

    def test_create_nota(self):
        self.client.login(username='professor1', password='prof123')
        data = {
            'aluno_id': self.aluno.id,
            'turma_id': self.turma.id,
            'disciplina_id': self.disciplina.id,
            'valor_nota': 8.0,
            'data_lancamento': '2024-08-15'
        }
        response = self.client.post(reverse('nota-list'), data, format='json')
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Data: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_nota(self):
        self.client.login(username='professor1', password='prof123')
        data = {'valor_nota': 7.5}
        response = self.client.patch(
            reverse('nota-detail', args=[self.nota.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.nota.refresh_from_db()
        self.assertEqual(self.nota.valor_nota, 7.5)

    def test_clean_invalid_nota(self):
        nota = Nota(
            aluno=self.aluno,
            turma=self.turma,
            disciplina=self.disciplina,
            valor_nota=11.0,  # Nota inválida
            data_lancamento=datetime.date.today()
        )
        with self.assertRaises(ValidationError):
            nota.clean()
