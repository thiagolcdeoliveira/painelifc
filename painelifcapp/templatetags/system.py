from django import template

from painelifcapp.models.setting import SettingModel
from painelifc.settings import MEDIA_URL
# TODO criar um metodo no manager para 'Sistema.objects.order_by('data')' esta duplicando codigo
register = template.Library()



@register.simple_tag
def logo():
    sis = SettingModel.objects.order_by('id').last()
    if sis:
        return MEDIA_URL + str(sis.logo)
    return None


@register.simple_tag
def endereco():
    sis = SettingModel.objects.order_by('id').last()
    if sis:
        return sis.endereco
    return None


@register.simple_tag
def imagem_titulo():
    sis = SettingModel.objects.order_by('id').last()
    if sis:
        return MEDIA_URL + str(sis.imagem_titulo)
    return None


@register.simple_tag
def nome():
    sis = SettingModel.objects.order_by('id').last()
    if sis:
        return sis.name
    return None

@register.simple_tag
def instagram():
    sis = SettingModel.objects.order_by('id').last()
    if sis:
        return sis.instagram
    return None

@register.simple_tag
def facebook():
    sis = SettingModel.objects.order_by('id').last()
    if sis:
        return sis.facebook
    return None

@register.simple_tag
def site():
    sis = SettingModel.objects.order_by('id').last()
    if sis:
        return sis.site
    return None