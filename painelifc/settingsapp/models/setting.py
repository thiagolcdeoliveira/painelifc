# -*- coding: utf-8 -*-

from django.db import models


class Setting(models.Model):
    name = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200, blank=True)
    logo = models.ImageField('Logo ', upload_to="image_upload/setting", blank=True)
    # logo = models.ImageField('Logo ', upload_to="image_upload/setting", blank=True)
    # logo_banner = models.ImageField('Logo do Banner', upload_to="image_upload/setting", blank=True)
    imagem_titulo = models.ImageField('Icone', upload_to="image_upload/setting", blank=True)
    # quantidade_trabalhos_por_cordenador = models.IntegerField()
    # quantidade_trabalhos_por_colaborador = models.IntegerField()
    # quantidade_trabalhos_por_autor = models.IntegerField()

    # image_member = models.ImageField('Imagem default dos Membros', upload_to="image_upload/setting", blank=True)
    # image_project = models.ImageField('Imagem default dos Projetos', upload_to="image_upload/setting", blank=True)
    # image_partner = models.ImageField('Imagem default dos Parceiros', upload_to="image_upload/setting", blank=True)

    def __unicode__(self):
        return self.name
