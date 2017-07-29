# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from settingsapp.models.setting import SettingModel
from settingsapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel

# Register your models here.
admin.site.register(SettingModel)
admin.site.register(ConfiguracaoTrabalhoModel)
