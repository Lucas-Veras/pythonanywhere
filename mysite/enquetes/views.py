from django.http import HttpResponse
from .models import Pergunta
from django.template import loader
#from django.shortcuts import render
# Create your views here.

def index(request):
<<<<<<< HEAD
    ultima_questao_lista = Pergunta.objects.order_by("data_pub")[:5]
    template = loader.get_template('enquetes/index.html')
    contexto = {
            'ultima_questao_lista' : ultima_questao_lista,
        }
    return HttpResponse(template.render(contexto, request))

def detalhes(resquest, id_enquete):
=======
    questao_lista = Pergunta.objects.order_by("data_pub")[:5]
    template = loader.get_template('enquetes/index.html')
    contexto = {
            'questao_lista' : questao_lista,
        }
    return HttpResponse(template.render(contexto, request))

def detalhes(request, id_enquete):
>>>>>>> 5732195cef9e8f6bf0def99b257a146573c8a63e
    resposta = "você está visualizando a questão %s."
    return HttpResponse(resposta % id_enquete)

def resultados(request, id_enquete):
    resposta = "Deltahes da enquete #$s."
    return HttpResponse(resposta % id_enquete)

<<<<<<< HEAD
def votacao(resquest, id_enquete):
=======
def votacao(request, id_enquete):
>>>>>>> 5732195cef9e8f6bf0def99b257a146573c8a63e
    resposta = "Votação para a questão %s."
    return HttpResponse(resposta % id_enquete)

