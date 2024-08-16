from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Professor
from .serializers import ProfessorSerializer


class ProfessorViewSet(ModelViewSet):
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try:
            queryset = Professor.objects.filter(
                user=user
            ).select_related('user')
            return queryset
        except Professor.DoesNotExist:
            raise NotFound("Professor não encontrado para o usuário logado.")
