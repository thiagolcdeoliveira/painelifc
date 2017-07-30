# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from settingsapp.models.setting import SettingModel
from settingsapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
from settingsapp.models.curso import CursoModel
from settingsapp.models.disciplina import DisciplinaModel
from settingsapp.models.papel import PapelModel
from settingsapp.models.pessoa import PessoaModel
from settingsapp.models.status import StatusModels
from settingsapp.models.trabalho import TrabalhoModel
from settingsapp.models.turma import TurmaModel
# Register your models here.
admin.site.register(SettingModel)
admin.site.register(ConfiguracaoTrabalhoModel)
admin.site.register(CursoModel)
admin.site.register(DisciplinaModel)
admin.site.register(PapelModel)
admin.site.register(PessoaModel)
admin.site.register(StatusModels)
admin.site.register(TrabalhoModel)
admin.site.register(TurmaModel)