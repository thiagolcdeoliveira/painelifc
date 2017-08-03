# coding: utf-8

from django import forms
import re
from painelifcapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
from painelifcapp.models.trabalho import TrabalhoModel
from painelifcapp.variaveis.variaveis import *
from django.db.models import Q

def ValidarAutor(autores):
    configuracao = ConfiguracaoTrabalhoModel.objects.order_by('id').last()
    if configuracao:
        print(autores.cleaned_data.get('autor1'))
        lista_autores=[autores.cleaned_data.get('autor1'), autores.cleaned_data.get('autor2') ,
                       autores.cleaned_data.get('autor3'), autores.cleaned_data.get('autor4'),
                       autores.cleaned_data.get('autor5'), autores.cleaned_data.get('autor6')]
        #
        for autor in lista_autores:
            if autor:
                print(autor.id)
                # trabalhos = TrabalhoModel.objects.filter(autor=autor.id, status__in=[SUBMETIDO, APROVADO])
                # if(len(trabalhos) >= configuracao.trabalhos_por_autor):
                #     raise forms.ValidationError("O  autor %s %s já está escrito em outro trabalho "  %(autor.first_name,autor.last_name))
                # elif autor in autores.remove(autor):
                #     raise forms.ValidationError("O  autor %  %s foi selecionado mais de uma vez"  %(autor.first_name,autor.last_name))
                # else:
                #     return autores
            else:
                raise forms.ValidationError(" Prencha pelo menos 6 autores" )


        #for autor in autores:
            #print(autor)
    #     raise forms.ValidationError("Número de Autores incorreto.")
    # else:
    #     raise forms.ValidationError("Número de Autores incorreto.")

    # configuracao=ConfiguracaoTrabalhoModel.objects.order_by('id').last()
    # if configuracao:
    #     #if len(autor) >= min_autor and len(Autor) <= max_colabolador:
    #     if len(autor) >= configuracao.min_autor and len(autor) <= configuracao.max_autor:
    #         trabalhos=TrabalhoModel.objects.filter(autor__in=autor, status__in=[SUBMETIDO,APROVADO])
    #         if(len(trabalhos) < configuracao.trabalhos_por_autor):
    #
    #             return autor
    #         else:
    #             raise forms.ValidationError("Existe autores indisponiveis nessa lista.")
    #     else:
    #         raise forms.ValidationError("Número de Autores incorreto. min: %d e max: %d" %(configuracao.min_autor,configuracao.max_autor))
    # else:
    #     raise forms.ValidationError("Número de Autores incorreto.")
