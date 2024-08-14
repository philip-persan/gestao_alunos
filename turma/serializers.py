from rest_framework import serializers

from disciplina.models import Disciplina
from disciplina.serializers import DisciplinaSerializer
from professor.models import Professor
from professor.serializers import ProfessorSerializer
from turma.models import Aluno, Nota, Turma


class TurmaSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer(read_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(
        queryset=Professor.objects.all(),
        source='professor',
        write_only=True
    )

    class Meta:
        model = Turma
        fields = [
            'id', 'nome', 'ano',
            'professor', 'professor_id'
        ]


class AlunoSerializer(serializers.ModelSerializer):
    turma = TurmaSerializer(read_only=True)
    turma_id = serializers.PrimaryKeyRelatedField(
        queryset=Turma.objects.all(),
        source='turma',
        write_only=True
    )

    class Meta:
        model = Aluno
        fields = [
            'id', 'nome_completo', 'data_nascimento',
            'endereco', 'email', 'telefone',
            'turma', 'turma_id'
        ]


class NotaSerializer(serializers.ModelSerializer):
    aluno = AlunoSerializer(read_only=True)
    aluno_id = serializers.PrimaryKeyRelatedField(
        queryset=Aluno.objects.all(),
        source='aluno',
        write_only=True
    )
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
        model = Nota
        fields = [
            'id', 'aluno', 'aluno_id',
            'turma', 'turma_id', 'disciplina',
            'disciplina_id', 'valor_nota',
            'data_lancamento'
        ]
