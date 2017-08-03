# coding:utf-8
from django.db import models
from django.contrib.auth.models import User

from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.models.disciplina import DisciplinaModel
from painelifcapp.models.status import StatusModels


class TrabalhoModel(models.Model):
    titulo = models.CharField(max_length=125)
    autor1 = models.ForeignKey(PessoaModel, related_name="autor1", verbose_name='Primeiro Autor (1)')
    autor2 = models.ForeignKey(PessoaModel, related_name="autor2", verbose_name='Segundo Autor (2)')
    autor3 = models.ForeignKey(PessoaModel, related_name="autor3", verbose_name='Terceiro Autor (3)')
    autor4 = models.ForeignKey(PessoaModel, related_name="autor4", verbose_name='Quarto Autor (4)')
    autor5 = models.ForeignKey(PessoaModel, related_name="autor5", verbose_name='Quinto Autor (5)')
    autor6 = models.ForeignKey(PessoaModel, related_name="autor6", verbose_name='Sexto Autor (6)')
    autor7 = models.ForeignKey(PessoaModel, related_name="autor7", verbose_name='Sétimo Autor (7)', blank=True, null=True)
    orientador = models.ForeignKey(PessoaModel, related_name="orientador")
    colaborador = models.ManyToManyField(PessoaModel, related_name="colaborador")
    usuario=models.ForeignKey(User, related_name="usuario")
    disciplina = models.ManyToManyField(DisciplinaModel,related_name="disciplina")
    status = models.ForeignKey(StatusModels, on_delete=models.CASCADE)
    resumo = models.CharField(max_length=2400)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Trabalho"
        verbose_name_plural = "Trabalhos"