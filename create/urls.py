from django.urls import path

from . import views

app_name = 'create'

urlpatterns = [
    path('', views.CreateTurmaDBView.as_view(), name='index'),
    path('alunos/', views.CreateAlunoDBView.as_view(), name='alunos'),
    path('notas/', views.CreateNotaDBView.as_view(), name='notas'),
]
