from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_enquete>/', views.detalhes, name="detalhes"),
    path(
        '<int:id_enquete>/votacao/',
        views.votacao, name="votacao"
    ),
    path(
        '<int:id_enquete>/resultados/',
        views.resultados, name="resultados"
    ),
]