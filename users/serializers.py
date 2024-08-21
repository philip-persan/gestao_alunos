from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name',
            'username', 'email', 'telefone', 'is_active'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Para garantir que a senha seja salva corretamente
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        print(f"Updating User SR: {instance.id}")
        print(f"Validated Data SR: {validated_data}")
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        instance.save()
        if password:
            user.set_password(password)
            user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Credenciais inválidas.")
        else:
            raise serializers.ValidationError(
                "Ambos os campos são necessários.")

        data['user'] = user
        return data


class UserGerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name',
            'username', 'email', 'telefone',
            'is_active', 'is_staff'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Para garantir que a senha seja salva corretamente
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        print(f"Updating User SR: {instance.id}")
        print(f"Validated Data SR: {validated_data}")
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        instance.save()
        if password:
            user.set_password(password)
            user.save()
        return user
