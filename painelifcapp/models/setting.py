# -*- coding: utf-8 -*-

from django.db import models


class SettingModel(models.Model):
    name = models.CharField(max_length=100)
    endereco = models.CharField(max_length=500, blank=True)
    logo = models.ImageField('Logo ', upload_to="image_upload/setting", blank=True)
    imagem_titulo = models.ImageField('Icone', upload_to="image_upload/setting", blank=True)
    imagem_impressao_trabalho = models.ImageField('Impressao', upload_to="image_upload/setting", blank=True)
    git = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    site = models.URLField()

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Configuração"
        verbose_name_plural = "Configurações"