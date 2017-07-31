# coding: utf-8

from django import forms
import re
from painelifcapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
from painelifcapp.models.trabalho import TrabalhoModel
from django.db.models import Q

def ValidarOrientador(orientador):
    configuracao=ConfiguracaoTrabalhoModel.objects.order_by('id').last()
    if configuracao:
        trabalhos=TrabalhoModel.objects.filter(orientador=orientador,status__in=[AGUARDANDO_PROFESSOR,SUBMETIDO,APROVADO])
        if(len(trabalhos)<=configuracao.trabalhos_por_orientador):
            return orientador
        else:
            raise forms.ValidationError("Esse Orietandor está indisponivel.")
    else:
        raise forms.ValidationError("Número de orientadores incorreto.")