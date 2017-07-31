# coding: utf-8

from django import forms
import re
from painelifcapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
from painelifcapp.models.trabalho import TrabalhoModel
from painelifcapp.variaveis.variaveis import *
from django.db.models import Q

def ValidarAutor(autor):
    configuracao=ConfiguracaoTrabalhoModel.objects.order_by('id').last()
    if configuracao:
        #if len(autor) >= min_autor and len(Autor) <= max_colabolador:
        if len(autor)+1 >= configuracao.min_autor and len(autor)+1 <= configuracao.max_autor:
            trabalhos=TrabalhoModel.objects.filter(autor__in=autor,status__in=[AGUARDANDO_PROFESSOR,SUBMETIDO,APROVADO])
            if(len(trabalhos)<=configuracao.trabalhos_por_autor):

                return autor
            else:
                raise forms.ValidationError("Existe autores indisponiveis nessa lista.")
        else:
            raise forms.ValidationError("Número de Autores incorreto. min: %d e max: %d" %(configuracao.min_autor,configuracao.max_autor))
    else:
        raise forms.ValidationError("Número de Autores incorreto.")