# coding: utf-8

from django import forms
import re
from settingsapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
from settingsapp.models.trabalho import TrabalhoModel
from django.db.models import Q

def ValidarOrientador(orientador):
    configuracao=ConfiguracaoTrabalhoModel.objects.order_by('id').last()
    if configuracao:
        trabalhos=TrabalhoModel.objects.filter(orientador=orientador)
        if(len(trabalhos)<=configuracao.trabalhos_por_orientador):
            return orientador
        else:
            raise forms.ValidationError("Esse Orietandor está indisponivel.")
    else:
        raise forms.ValidationError("Número de orientadores incorreto.")