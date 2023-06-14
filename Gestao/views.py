from django.shortcuts import render
from .models import Animal, Saude, Reproducao, Peso, Alimentacao, Movimentacao, Economia, Abate, Observacao

def dashboard_view(request):
    # Obter dados dos modelos
    animals = Animal.objects.all()
    saude = Saude.objects.all()
    reproducao = Reproducao.objects.all()
    pesos = Peso.objects.all()
    alimentacao = Alimentacao.objects.all()
    movimentacao = Movimentacao.objects.all()
    economia = Economia.objects.all()
    abate = Abate.objects.all()
    observacoes = Observacao.objects.all()
    quantidade_animais = Animal.objects.count()

    # Passar os dados para o template
    context = {
        'animals': animals,
        'saude': saude,
        'reproducao': reproducao,
        'pesos': pesos,
        'alimentacao': alimentacao,
        'movimentacao': movimentacao,
        'economia': economia,
        'abate': abate,
        'observacoes': observacoes,
    }

    return render(request, '../templates/dashboard.html', context)
