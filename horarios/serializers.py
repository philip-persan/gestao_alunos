from rest_framework import serializers

from disciplina.models import Disciplina
from disciplina.serializers import DisciplinaSerializer
from turma.models import Turma
from turma.serializers import TurmaSerializer

from .models import Horario


class HorarioSerializer(serializers.ModelSerializer):
    turma = TurmaSerializer(read_only=True)
    turma_id = serializers.PrimaryKeyRelatedField(
        queryset=Turma.objects.all(),
        source='turma',
        write_only=True
    )
    disciplina = DisciplinaSerializer(read_only=True)
    disciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=Disciplina.objects.all(),
        source='disciplina',
        write_only=True
    )

    class Meta:
        model = Horario
        fields = [
            'id', 'turma', 'turma_id',
            'disciplina', 'disciplina_id',
            'dia_semana', 'hora_inicio', 'hora_fim'
        ]
