from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Funcionário')
    idade = models.PositiveIntegerField(default=0, blank=True, null=False, help_text='Idade do Funcionário')

    def __str__(self):
        return self.nome
