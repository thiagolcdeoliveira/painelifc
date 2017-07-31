# coding: utf-8

from django import forms
import re
from painelifcapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
from painelifcapp.models.trabalho import TrabalhoModel
from painelifcapp.variaveis.variaveis import *

def ValidarColaborador(colaborador):
    configuracao=ConfiguracaoTrabalhoModel.objects.order_by('id').last()
    if configuracao:
        #if len(colaborador) >= min_colaborador and len(colaborador) <= max_colabolador:
        if len(colaborador) >= configuracao.min_colaborador and len(colaborador) <= configuracao.max_colaborador:
            trabalhos=TrabalhoModel.objects.filter(colaborador__in=colaborador,status__in=[AGUARDANDO_PROFESSOR,SUBMETIDO,APROVADO])

            if(len(trabalhos)< configuracao.trabalhos_por_colaborador):

                return colaborador
            else:
                raise forms.ValidationError("Existe colaboradores indisponiveis nessa lista.")
            #return colaborador
        else:
            raise forms.ValidationError("Número de colaboradores incorreto. min: %d e max: %d" %(configuracao.min_colaborador,configuracao.max_colaborador))
    else:
        raise forms.ValidationError("Número de colaboradores incorreto.")