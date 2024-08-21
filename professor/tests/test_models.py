from django.test import TestCase

from professor.models import Professor
from users.models import User


class ProfessorModelTests(TestCase):

    def test_professor_created_on_user_creation(self):
        """
        Testa se o Professor é criado automaticamente via signal quando um usuário é criado. # noqa
        """
        user = User.objects.create_user(
            username='professor2',
            email='professor2@example.com',
            password='testpass123'
        )

        # Verifica se o Professor foi criado
        professor_exists = Professor.objects.filter(user=user).exists()
        self.assertTrue(professor_exists)
