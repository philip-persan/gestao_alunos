from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    View para que um usuário normal possa acessar e editar seus próprios dados.
    """
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

    def get_object(self):
        user = self.request.user
        return User.objects.get(id=user.id)


class UserAdminViewSet(ModelViewSet):
    """
    View para administradores, permitindo acesso a todos os usuários.
    Apenas admins podem criar, editar e deletar usuários.
    """
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
