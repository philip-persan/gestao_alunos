from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Disciplina
from .serializers import DisciplinaSerializer


class DisciplinaViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
