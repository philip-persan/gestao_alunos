from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Horario
from .serializers import HorarioSerializer


class HorarioViewSet(ModelViewSet):
    queryset = Horario.objects.all(
    ).select_related('turma', 'disciplina')
    serializer_class = HorarioSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
