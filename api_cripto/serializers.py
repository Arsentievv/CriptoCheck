from rest_framework import serializers

from app_cripto.models import CriptoModel


class CriptoSerializer(serializers.ModelSerializer):

    """Сериалайзер для модели крипто-валюты."""

    class Meta:
        model = CriptoModel
        fields = '__all__'

