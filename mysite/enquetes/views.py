from django.http import HttpResponseRedirect
from .models import Pergunta, Escolha
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    questao_lista = Pergunta.objects.order_by("data_pub")
    return render(request, 'enquetes/index.html', {'questao_lista' : questao_lista,})

def detalhes(request, id_enquete):
    pergunta = get_object_or_404(Pergunta, pk=id_enquete)
    return render(request, 'enquetes/detalhes.html', {'pergunta' : pergunta})

def votacao(request, id_enquete):
    pergunta = get_object_or_404(Pergunta, pk=id_enquete)
    try:
        alternativa_escolhida = pergunta.escolha_set.get(pk=request.POST['escolha'])
    except(KeyError, Escolha.DoesNotExist):
        return render(request, 'enquetes/detalhes.html', {
            'pergunta':pergunta,
            'msg_erro':'Você não selecionou uma opção',
        })
    else:
        alternativa_escolhida.votos += 1
        alternativa_escolhida.save()
        return HttpResponseRedirect(reverse('enquetes:resultados', args=(id_enquete,)))

def resultados(request, id_enquete):
    pergunta = get_object_or_404(Pergunta, pk=id_enquete)
    return render(request, 'enquetes/resultados.html', {'pergunta':pergunta})

