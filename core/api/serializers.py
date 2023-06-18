from rest_framework import serializers
from core import models

class DoadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doador
        fields = '__all__'

class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doacao
        fields = '__all__'

class DoacaoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DoacaoItem
        fields = '__all__'