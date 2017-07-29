# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from painelifc.models.turma import TurmaModel



class PessoaModel(User):
    matricula = models.CharField(max_length=30)
    turma = models.ForeignKey(TurmaModel, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"