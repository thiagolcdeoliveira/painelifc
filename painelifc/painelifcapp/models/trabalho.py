# coding:utf-8
from django.db import models
from django.contrib.auth.models import User

from pessoa import PessoaModel
from disciplina import DisciplinaModel
from status import StatusModels


class TrabalhoModel(models.Model):
    titulo = models.CharField(max_length=125)
    autor = models.ManyToManyField(PessoaModel, related_name="autor")
    orientador = models.ForeignKey(PessoaModel, related_name="orientador")
    colaborador = models.ManyToManyField(PessoaModel, related_name="colaborador")
    usuario=models.ForeignKey(User, related_name="usuario")
    disciplina = models.ManyToManyField(DisciplinaModel,related_name="disciplina")
    status = models.ForeignKey(StatusModels, on_delete=models.CASCADE)
    resumo = models.CharField(max_length=500)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Trabalho"
        verbose_name_plural = "Trabalhos"