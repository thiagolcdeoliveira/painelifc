# coding:utf-8
from django.db import models
from painelifc.models.pessoa import PessoaModel
from painelifc.models.disciplina import DisciplinaModel
from painelifc.models.status import StatusModels


class TrabalhoModel(models.Model):
    titulo = models.CharField(max_length=125)
    autor = models.ManyToManyField(PessoaModel)
    orientador = models.ManyToManyField(PessoaModel)
    colaborador = models.ManyToManyField(PessoaModel)
    disciplina = models.ForeignKey(DisciplinaModel, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusModels, on_delete=models.CASCADE)
    resumo = models.CharField(max_length=500)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Trabalho"
        verbose_name_plural = "Trabalhos"