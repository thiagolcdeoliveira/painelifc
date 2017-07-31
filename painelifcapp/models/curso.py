# coding:utf-8
from django.db import models


class CursoModel(models.Model):
    nome = models.CharField(max_length=125)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"