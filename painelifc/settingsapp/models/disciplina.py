# coding:utf-8
from django.db import models
from painelifc.models.curso import CursoModel


class DisciplinaModel(models.Model):
    nome = models.CharField(max_length=20)
    curso = models.ForeignKey(CursoModel, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"