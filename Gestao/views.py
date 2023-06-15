from django.shortcuts import render
from Gestao.forms import *
from Gestao.models import *

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

def cadastrar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_animais')
    else:
        form = AnimalForm()
    
    return render(request, 'cadastrar_animal.html', {'form': form})

def buscar_animais(request, search_query=None):
    if request.method == 'GET':
        if search_query:
            animais = Animal.objects.filter(numero_identificacao__icontains=search_query)
            return render(request, 'lista_animais.html', {'animais': animais})
        else:
            return render(request, 'mensagem_erro.html', {'mensagem': 'Digite um valor de busca válido'})

def editar_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('lista_animais')
    else:
        form = AnimalForm(instance=animal)
    
    return render(request, 'editar_animal.html', {'form': form, 'animal': animal})