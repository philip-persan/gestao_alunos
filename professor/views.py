from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Professor
from .serializers import ProfessorSerializer


class ProfessorViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nivel', 'estado']
    search_fields = [
        'data_nascimento', 'formacao',
        'nivel', 'estado'
    ]
    ordering_fields = [
        'estado', 'nivel',
    ]

    def get_queryset(self):
        user = self.request.user
        if not user.is_staff:
            try:
                queryset = Professor.objects.filter(
                    user=user
                ).select_related('user')
                return queryset
            except Professor.DoesNotExist:
                raise NotFound(
                    "Professor não encontrado para o usuário logado.")
        else:
            try:
                queryset = Professor.objects.all(
                ).select_related('user')
                return queryset
            except Professor.DoesNotExist:
                raise NotFound(
                    "Professor não encontrado para o usuário logado.")
