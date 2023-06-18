from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from core.api import viewsets as coreviewsets

router = routers.DefaultRouter()
router.register(r'core', coreviewsets.DoadorViewSet, basename='Doador')
router.register(r'doacoes', coreviewsets.DoacaoViewSet, basename='Doacao')
router.register(r'doacaoitens', coreviewsets.DoacaoItemViewSet, basename='DoacaoItem')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
