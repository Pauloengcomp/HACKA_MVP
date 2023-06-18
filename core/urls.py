from django.contrib import admin
from django.urls import path, include
from .views import home, cad_doador, editar, update,delete

urlpatterns = [
    path('', home),
    path('salvar/', cad_doador, name="cad_doador"),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
 