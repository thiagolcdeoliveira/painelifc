# -*- coding: utf-8 -*-

from django.db import models


class ConfiguracaoTrabalho(models.Model):
    name = models.CharField(max_length=100)
    quantidade_trabalhos_por_cordenador = models.IntegerField(verbose_name="Quantidade máxima de Trabalhos que um cooredenador pode orientar")
    quantidade_trabalhos_por_colaborador = models.IntegerField(verbose_name="Quantidade máxima de Trabalhos que um colaborador pode participar")
    quantidade_trabalhos_por_autor = models.IntegerField(verbose_name="Quantidade máxima de Trabalhos que um autor pode atuar")

    # image_member = models.ImageField('Imagem default dos Membros', upload_to="image_upload/setting", blank=True)
    # image_project = models.ImageField('Imagem default dos Projetos', upload_to="image_upload/setting", blank=True)
    # image_partner = models.ImageField('Imagem default dos Parceiros', upload_to="image_upload/setting", blank=True)

    def __unicode__(self):
        return self.name
