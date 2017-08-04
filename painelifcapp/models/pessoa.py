# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from painelifcapp.models.turma import TurmaModel


class PessoaModel(User):
    matricula = models.CharField(max_length=30,blank=True)
    telefone = models.CharField(max_length=30,blank=True)
    renda = models.CharField(max_length=30,blank=True)
    datadenascimento =  models.CharField(max_length=30,blank=True)
    rg =  models.CharField(max_length=30,blank=True)
    cpf =  models.CharField(max_length=30,blank=True)
    cidade =  models.CharField(max_length=30,blank=True)
    nome =  models.CharField(max_length=50,blank=True)
    turma = models.ForeignKey(TurmaModel, on_delete=models.CASCADE, null=True, blank=True)

    # feturn "%s %s " %(str(self.first_name),str(self.last_name))

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def get_full_name(self):
        return ('%s %s' % (self.first_name, self.last_name)).title()