from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .serializers import UserGerenteSerializer, UserSerializer


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
    serializer_class = UserGerenteSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'is_staff']
    search_fields = [
        'first_name', 'last_name',
        'username', 'email', 'telefone'
    ]
    ordering_fields = [
        'first_name', 'last_name',
    ]
