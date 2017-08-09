# coding: utf-8

from django import forms

def ValidarTitulo(titulo):
    if(len(titulo)>= 1):
        return titulo
    else:
        raise forms.ValidationError("O título é obrigatório!")
