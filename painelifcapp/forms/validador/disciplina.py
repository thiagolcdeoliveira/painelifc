# coding: utf-8

from django import forms
import re
from painelifcapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
from painelifcapp.models.trabalho import TrabalhoModel
from painelifcapp.variaveis.variaveis import *
from django.db.models import Q

def ValidarDisciplina(disciplina):

    configuracao=ConfiguracaoTrabalhoModel.objects.order_by('id').last()
    if configuracao:
        if(len(disciplina)> configuracao.min_disciplina and len(disciplina)< configuracao.max_disciplina):
            return disciplina
        else:
            raise forms.ValidationError("Número incorreto de disciplinas. min: %d max: %d" %(configuracao.min_disciplina,configuracao.max_disciplina))
    else:
        raise forms.ValidationError("Número de disciplinas incorreto.")