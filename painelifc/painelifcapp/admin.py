# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from painelifcapp.models.setting import SettingModel
from painelifcapp.models.configuracao_trabalho import ConfiguracaoTrabalhoModel
from painelifcapp.models.curso import CursoModel
from painelifcapp.models.disciplina import DisciplinaModel
from painelifcapp.models.papel import PapelModel
from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.models.status import StatusModels
from painelifcapp.models.trabalho import TrabalhoModel
from painelifcapp.models.turma import TurmaModel
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