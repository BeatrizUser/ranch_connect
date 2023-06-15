from django import forms
from .models import Animal, Saude, Reproducao, Peso, Alimentacao, Movimentacao, Economia, Abate, Observacao


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        widgets = {
            'raca': forms.Select(choices=Animal.RACA_CHOICES),
            'sexo': forms.Select(choices=Animal.SEXO_CHOICES),
            'pedigree': forms.Select(choices=Animal.PEDIGREE_CHOICES),
        }


class SaudeForm(forms.ModelForm):
    class Meta:
        model = Saude
        exclude = ('animal',)


class ReproducaoForm(forms.ModelForm):
    class Meta:
        model = Reproducao
        exclude = ('animal',)


class PesoForm(forms.ModelForm):
    class Meta:
        model = Peso
        exclude = ('animal',)


class AlimentacaoForm(forms.ModelForm):
    class Meta:
        model = Alimentacao
        exclude = ('animal',)


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        exclude = ('animal',)


class EconomiaForm(forms.ModelForm):
    class Meta:
        model = Economia
        exclude = ('animal',)


class AbateForm(forms.ModelForm):
    class Meta:
        model = Abate
        exclude = ('animal',)


class ObservacaoForm(forms.ModelForm):
    class Meta:
        model = Observacao
        exclude = ('animal',)
