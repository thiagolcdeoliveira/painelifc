# -*- coding: utf-8 -*-
from django.db import models


class ConfiguracaoTrabalhoModel(models.Model):
    name = models.CharField(max_length=100)
    #quantidade_trabalhos_por_cordenador = models.IntegerField(verbose_name="Quantidade máxima de Trabalhos que um cooredenador pode orientar")
    min_colaborador = models.IntegerField(verbose_name="Quantidade minima de colaboradores por trabalho")
    max_colaborador = models.IntegerField(verbose_name="Quantidade máxima de colaboradores por trabalho")
    min_autor = models.IntegerField(verbose_name="Quantidade minima de  autores  por trabalho ")
    max_autor = models.IntegerField(verbose_name="Quantidade máxima de autores por trabalho")
    min_disciplina = models.IntegerField(verbose_name="Quantidade minima de  disciplinas  por trabalho ")
    max_disciplina = models.IntegerField(verbose_name="Quantidade máxima de disciplinas por trabalho")
    trabalhos_por_colaborador = models.IntegerField(verbose_name="Quantidade máximo de Trabalhos por colaboradores ")
    trabalhos_por_orientador=models.IntegerField(verbose_name="Quantidade máximo de Trabalhos por orientador ")
    trabalhos_por_autor = models.IntegerField(verbose_name="Quantidade máxima de Trabalhos por autores")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Configuração dos Trabalhos"
        verbose_name_plural = "Configurações dos Trabalhos"