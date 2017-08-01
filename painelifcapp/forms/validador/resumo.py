# coding: utf-8

from django import forms

def ValidarResumo(resumo):
    if(len(resumo)<= 2400) and (len(resumo)>=1700):
        return resumo
    else:
        raise forms.ValidationError("O resumo deve ter no mínimo 1700 caracteres e no máximo 2400 caracteres")
