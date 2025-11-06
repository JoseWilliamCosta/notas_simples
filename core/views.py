from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import NotaForm
from .models import Nota
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NotaSerializer

'''

============= Views api =============

'''

@api_view(['GET'])
def notas_api(request):
    notas = Nota.objects.all().order_by('-data_publicacao')
    serializer = NotaSerializer(notas, many=True)
    return Response(serializer.data)







'''

============= Views normais =============

'''

def index(request):
    notas = Nota.objects.all().order_by('-data_publicacao')  # Exibe todas as notas, mais recentes primeiro
    return render(request, 'index.html', {'notas': notas})

def nota(request, nota_id):
    notas = get_object_or_404(Nota, id=nota_id)
    return render(request, 'nota.html', {'notas': notas})




'''

============= NOTAS =============

'''

def criar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST, request.FILES)
        if form.is_valid():
            nota = form.save(commit=False)
            #nota.usuario = request.user  # Associa a nota ao usuário logado
            nota.save()
            messages.success(request, 'Nota criada com sucesso!')
            return redirect('index')  # Redireciona após salvar
        else:
            messages.error(request, 'Erro ao criar a nota. Verifique os campos.')
    else:
        form = NotaForm()

    return render(request, 'criar_nota.html', {'form': form})

'''

============= NOTAS EDITAR =============

'''


def editar_nota(request, nota_id=None):
    # Se houver um ID, edita a nota. Caso contrário, cria nova.
    nota = get_object_or_404(Nota, pk=nota_id) if nota_id else None

    if request.method == 'POST':
        form = NotaForm(request.POST, request.FILES if request.FILES else None, instance=nota)
        if form.is_valid():
            nova_nota = form.save(commit=False)
            #if not nota:  # Se for criação, define o usuário
                #nova_nota.usuario = request.user
            nova_nota.save()
            return redirect('index')  # Redirecione para a lista de notas
    else:
        form = NotaForm(instance=nota)

    return render(request, 'criar_nota.html', {'form': form})


'''

============= NOTAS EXCLUIR =============

'''
def excluir_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)

    # Permite exclusão apenas para autor ou admin
    #if request.user == nota.usuario or request.user.is_superuser:
    nota.delete()
    return redirect('index')