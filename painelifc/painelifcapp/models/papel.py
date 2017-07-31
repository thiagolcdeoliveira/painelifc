# coding:utf-8
from django.db import models

class PapelModel(models.Model):
    nome = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Papel"
        verbose_name_plural = "Papéis"