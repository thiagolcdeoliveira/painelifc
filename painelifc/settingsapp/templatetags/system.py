from django import template

from settingsapp.models.setting import Setting

# TODO criar um metodo no manager para 'Sistema.objects.order_by('data')' esta duplicando codigo
register = template.Library()



@register.simple_tag
def logo():
    sis = Setting.objects.order_by('id').last()
    if sis:
        return sis.logo
    return None


@register.simple_tag
def endereco():
    sis = Setting.objects.order_by('id').last()
    if sis:
        return sis.endereco
    return None


@register.simple_tag
def imagem_titulo():
    sis = Setting.objects.order_by('id').last()
    if sis:
        return sis.imagem_titulo
    return None


@register.simple_tag
def name():
    sis = Setting.objects.order_by('id').last()
    if sis:
        return sis.name
    return None

