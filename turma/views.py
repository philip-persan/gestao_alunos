from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Aluno, Nota, Turma
from .serializers import AlunoSerializer, NotaSerializer, TurmaSerializer


class TurmaViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = TurmaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Turma.objects.filter(
            professor__user=user
        ).select_related('professor')
        return queryset


class AlunoViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Aluno.objects.filter(
            turma__professor__user=user
        ).select_related('turma')
        return queryset


class NotaViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = NotaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Nota.objects.filter(
            turma__professor__user=user
        ).select_related('aluno', 'turma')
        return queryset
