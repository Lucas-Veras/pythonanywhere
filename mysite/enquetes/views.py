from django.http import HttpResponse, Http404
from .models import Pergunta
#from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    questao_lista = Pergunta.objects.order_by("data_pub")[:5]
 #   template = loader.get_template('enquetes/index.html')
    contexto = {
            'questao_lista' : questao_lista,
        }
    return render(request, 'enquetes/index.html', contexto)
  #  return HttpResponse(template.render(contexto, request))

def detalhes(request, id_pergunta):
    try:
        pergunta = Pergunta.objects.get(pk = id_pergunta)
    except Pergunta.DoesNotExist:
        raise Http404("Enquete desejada não existe")
        contexto = { 'pergunta' : pergunta }
    return render(request, 'enquetes/detalhes', contexto)

def resultados(request, id_enquete):
    resposta = "Deltahes da enquete #$s."
    return HttpResponse(resposta % id_enquete)

def votacao(request, id_enquete):
    resposta = "Votação para a questão %s."
    return HttpResponse(resposta % id_enquete)

