# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from settingsapp.models.setting import Setting
from settingsapp.models.configuracao_trabalho import ConfiguracaoTrabalho

# Register your models here.
admin.site.register(Setting)
admin.site.register(ConfiguracaoTrabalho)
