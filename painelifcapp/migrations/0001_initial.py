# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 15:40
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracaoTrabalhoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('min_colaborador', models.IntegerField(verbose_name=b'Quantidade minima de colaboradores por trabalho')),
                ('max_colaborador', models.IntegerField(verbose_name=b'Quantidade m\xc3\xa1xima de colaboradores por trabalho')),
                ('min_autor', models.IntegerField(verbose_name=b'Quantidade minima de  autores  por trabalho ')),
                ('max_autor', models.IntegerField(verbose_name=b'Quantidade m\xc3\xa1xima de autores por trabalho')),
                ('trabalhos_por_colaborador', models.IntegerField(verbose_name=b'Quantidade m\xc3\xa1ximo de Trabalhos por colaboradores ')),
                ('trabalhos_por_orientador', models.IntegerField(verbose_name=b'Quantidade m\xc3\xa1ximo de Trabalhos por orientador ')),
                ('trabalhos_por_autor', models.IntegerField(verbose_name=b'Quantidade m\xc3\xa1xima de Trabalhos por autores')),
            ],
            options={
                'verbose_name': 'Configura\xe7\xe3o dos Trabalhos',
                'verbose_name_plural': 'Configura\xe7\xf5es dos Trabalhos',
            },
        ),
        migrations.CreateModel(
            name='CursoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='DisciplinaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painelifcapp.CursoModel')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='PapelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Papel',
                'verbose_name_plural': 'Pap\xe9is',
            },
        ),
        migrations.CreateModel(
            name='PessoaModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('matricula', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SettingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('endereco', models.CharField(blank=True, max_length=200)),
                ('logo', models.ImageField(blank=True, upload_to=b'image_upload/setting', verbose_name=b'Logo ')),
                ('imagem_titulo', models.ImageField(blank=True, upload_to=b'image_upload/setting', verbose_name=b'Icone')),
            ],
            options={
                'verbose_name': 'Configura\xe7\xe3o',
                'verbose_name_plural': 'Configura\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='StatusModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='TrabalhoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=125)),
                ('resumo', models.CharField(max_length=500)),
                ('autor', models.ManyToManyField(related_name='autor', to='painelifcapp.PessoaModel')),
                ('colaborador', models.ManyToManyField(related_name='colaborador', to='painelifcapp.PessoaModel')),
                ('disciplina', models.ManyToManyField(related_name='disciplina', to='painelifcapp.DisciplinaModel')),
                ('orientador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orientador', to='painelifcapp.PessoaModel')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painelifcapp.StatusModels')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Trabalho',
                'verbose_name_plural': 'Trabalhos',
            },
        ),
        migrations.CreateModel(
            name='TurmaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('ano', models.CharField(max_length=30)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painelifcapp.CursoModel')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
        migrations.AddField(
            model_name='pessoamodel',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='painelifcapp.TurmaModel'),
        ),
    ]