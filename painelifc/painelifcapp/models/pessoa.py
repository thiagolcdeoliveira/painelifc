# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from painelifcapp.models.turma import TurmaModel



class PessoaModel(User):
    matricula = models.CharField(max_length=30)
    turma = models.ForeignKey(TurmaModel, on_delete=models.CASCADE, null=True,blank=True)



    def __str__(self):
        return "%s %s " %(str(self.first_name),str(self.last_name))

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"