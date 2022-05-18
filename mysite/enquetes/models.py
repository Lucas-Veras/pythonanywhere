import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length=150)
    data_pub = models.DateTimeField(
        'Data de publicação', auto_now_add=True)

    def was_published(self):
        return self.data_pub >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.pergunta_texto

class Escolha(models.Model):
    pergunta = models.ForeignKey(
        Pergunta, on_delete=models.CASCADE
    )
    escolha_texto = models.CharField(max_length=50)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.pergunta.pergunta_texto, self.escolha_texto)