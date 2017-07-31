# coding:utf-8
from django.db import models


class StatusModels(models.Model):
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"