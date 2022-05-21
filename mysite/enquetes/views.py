from django.http import HttpResponse
from .models import Pergunta
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    questao_lista = Pergunta.objects.order_by("data_pub")[:5]
    return render(request, 'enquetes/index.html', {'questao_lista' : questao_lista,})

def detalhes(request, id_enquete):
    pergunta = get_object_or_404(Pergunta, pk=id_enquete)
    return render(request, 'enquetes/detalhes.html', {'pergunta' : pergunta})

def resultados(request, id_enquete):
    resposta = "Deltahes da enquete #$s."
    return HttpResponse(resposta % id_enquete)

def votacao(request, id_enquete):
    resposta = "Votação para a questão %s."
    return HttpResponse(resposta % id_enquete)

