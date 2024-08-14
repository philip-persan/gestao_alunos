from rest_framework import serializers

from professor.models import Professor
from users.serializers import UserSerializer


class ProfessorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Professor
        fields = ['id', 'user', 'data_nascimento',
                  'formacao', 'nivel', 'estado']

    def update(self, instance, validated_data):
        # Atualiza os dados do professor
        instance.data_nascimento = validated_data.get(
            'data_nascimento', instance.data_nascimento)
        instance.formacao = validated_data.get('formacao', instance.formacao)
        instance.nivel = validated_data.get('nivel', instance.nivel)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.save()

        return instance
