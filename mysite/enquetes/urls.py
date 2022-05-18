from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enquetes/<int:id_enquete>/', views.detalhes, name="detalhes"),
    path(
        'enquetes/<int:id_enquete>/votacao/',
        views.votacao, name="votacao"
    ),
    path(
        'enquetes/<int:id_enquete>/resultados/',
        views.resultados, name="resultados"
    ),
]