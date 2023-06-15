# urls.py
from django.contrib import admin
from django.urls import path
from Gestao.views import *

app_name = 'Gestao'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='dashboard_view'),
    path('cadastrar/', cadastrar_animal, name='cadastrar_animal'),
    path('buscar/<str:search_query>/', buscar_animais, name='buscar_animais'),
    path('editar/<int:animal_id>/', editar_animal, name='editar_animal'),
]
