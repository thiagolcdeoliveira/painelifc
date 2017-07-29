# -*- coding: utf-8 -*-

from django.db import models


class ConfiguracaoTrabalhoModel(models.Model):
    name = models.CharField(max_length=100)
    quantidade_trabalhos_por_cordenador = models.IntegerField(verbose_name="Quantidade máxima de Trabalhos que um cooredenador pode orientar")
    quantidade_trabalhos_por_colaborador = models.IntegerField(verbose_name="Quantidade máxima de Trabalhos que um colaborador pode participar")
    quantidade_trabalhos_por_autor = models.IntegerField(verbose_name="Quantidade máxima de Trabalhos que um autor pode atuar")


    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name = "Configuração dos Trabalhos"
        verbose_name_plural = "Configurações dos Trabalhos"