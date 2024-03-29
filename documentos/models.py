from django.db import models
from funcionarios.models import Funcionario



class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertencente = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.descricao
