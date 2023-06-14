from django.contrib import admin
from .models import *

# Registro do modelo Animal e seus relacionamentos
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal_nome', 'raca', 'data_nascimento', 'pai', 'mae')
    list_filter = ('raca',)
    search_fields = ('nome', 'raca')

    def animal_nome(self, obj):
        return obj.numero_identificacao
    animal_nome.short_description = 'Número de Identificação'

class SaudeAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'historico_vacinacao', 'tratamentos')
    list_filter = ('animal__raca',)
    search_fields = ('animal__numero_identificacao', 'historico_vacinacao')

class ReproducaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'mae', 'pai', 'data_cobertura', 'data_inseminacao', 'data_parto')
    list_filter = ('animal__raca',)
    search_fields = ('animal__numero_identificacao', 'mae__numero_identificacao', 'pai__numero_identificacao')

class PesoAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'data_pesagem', 'peso')
    list_filter = ('animal__raca',)
    search_fields = ('animal__numero_identificacao',)

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Saude, SaudeAdmin)
admin.site.register(Reproducao, ReproducaoAdmin)
admin.site.register(Peso, PesoAdmin)

# Registro dos demais modelos
admin.site.register(Alimentacao)
admin.site.register(Movimentacao)
admin.site.register(Economia)
admin.site.register(Abate)
admin.site.register(Observacao)
admin.site.register(Projeto)
