from rest_framework import viewsets
from core.api import serializers
from core import models

class DoadorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoadorSerializer
    queryset = models.Doador.objects.all()


class DoacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoacaoSerializer
    queryset = models.Doacao.objects.all()

class DoacaoItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoacaoItemSerializer
    queryset = models.DoacaoItem.objects.all()