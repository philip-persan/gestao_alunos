from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlunoViewSet, NotaViewSet, TurmaViewSet

router = DefaultRouter()
router.register(r'turma', TurmaViewSet, basename='turma')
router.register(r'aluno', AlunoViewSet, basename='aluno')
router.register(r'nota', NotaViewSet, basename='nota')

urlpatterns = [
    path('', include(router.urls)),
]
