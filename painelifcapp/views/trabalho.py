# coding: utf-8
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from painelifcapp.forms.trabalho import FormTrabalho
from painelifcapp.models.status import StatusModels
from painelifcapp.models.trabalho import TrabalhoModel
# from painelifcapp.models.pessoa import PessoaModel
from painelifcapp.models.pessoa import PessoaModel
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.db.models import Q

from painelifcapp.models.turma import TurmaModel
from painelifcapp.variaveis.variaveis import *

# Pra gerar PDF e Zip#
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


class ConsultaTrabalhoView(View):
    template = 'index.html'
    template_consulta = 'trabalho/consulta.html'

    def get(self, request, id=None):
        if id:
            try:
                autorizacao = TrabalhoModel.objects.filter(
                    Q(colaborador__pk=request.user.id) | Q(orientador__pk=request.user.id) | Q(
                        autor1__pk=request.user.id) | Q(autor2__pk=request.user.id) | Q(autor3__pk=request.user.id) | Q(
                        autor4__pk=request.user.id) | Q(autor5__pk=request.user.id) | Q(autor6__pk=request.user.id) | Q(
                        autor7__pk=request.user.id) | Q(usuario=request.user.id)).distinct()
                admin = request.user.is_superuser or PessoaModel.objects.get(pk=request.user.id).groups.filter(pk=ADMIN)
                if autorizacao or admin:
                    trabalho = TrabalhoModel.objects.get(pk=id)
                    return render(request, self.template_consulta, {'trabalho': trabalho})
                else:
                    return redirect('/')
            except:
                return redirect('/')
        else:
            # trabalhos = TrabalhoModel.objects.all()
            trabalhos = TrabalhoModel.objects.filter(
                Q(autor1__pk=request.user.id) | Q(autor2__pk=request.user.id) | Q(
                    autor3__pk=request.user.id) | Q(autor4__pk=request.user.id) | Q(autor5__pk=request.user.id) | Q(
                    autor6__pk=request.user.id) | Q(autor7__pk=request.user.id) | Q(orientador__pk=request.user.id) | Q(
                    colaborador__pk=request.user.id) | Q(usuario=request.user.id)).distinct()
            is_orientador = PessoaModel.objects.filter(pk=request.user.id, groups__in=[ORIENTADOR]).exists()
            return render(request, self.template, {'trabalhos': trabalhos, 'orientador': is_orientador})

            # def post(self, request):
            #     return render(request, self.template, {'form': ""})


class CadastroTrabalhoView(View):
    template = 'trabalho/salvar.html'

    def get(self, request, id=None):

        # ajax
        if 'turma_id' in request.GET:
            import json
            als = PessoaModel.objects.filter(turma=request.GET['turma_id']).only('id', 'first_name')
            print(als)
            alunos = []
            for al in als:
                dict = {'id': al.id, 'nome': al.first_name + " " + al.last_name}
                alunos.append(dict)
            json = json.dumps(alunos)
            # json = serializers.serialize("json", als)
            return HttpResponse(json)

        if id:
            trabalho = TrabalhoModel.objects.get(pk=id)
            form = FormTrabalho(instance=trabalho)
            turmas = []
        else:
            form = FormTrabalho()
            turmas = TurmaModel.objects.all()
        return render(request, self.template, {'form': form, 'turmas': turmas})

    def post(self, request, id=None):

        if id:
            trabalho = TrabalhoModel.objects.get(pk=id)
            form = FormTrabalho(instance=trabalho, data=request.POST)
        else:
            form = FormTrabalho(request.POST)
        if form.is_valid():
            form_edit = form.save(commit=True)
            form_edit.usuario_id = request.user.id
            form_edit.status_id = AGUARDANDO_PROFESSOR
            form_edit.save()
            return redirect('/')
        print(form.errors)
        turmas = TurmaModel.objects.all()
        return render(request, self.template, {'form': form, 'turmas': turmas})


class ImprimeTrabalhoView(View):
    template_consulta = 'trabalho/consulta.html'

    def get(self, request, id=None):
        trabalho = TrabalhoModel.objects.get(pk=id)
        nome = "static/media/trabalhos/" + trabalho.titulo + ".pdf"
        doc = SimpleDocTemplate("static/media/trabalhos/" + trabalho.titulo + ".pdf", pagesize=letter, rightMargin=72,
                                leftMargin=72, topMargin=00, bottomMargin=18)
        Story = []
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, spaceBefore=20))
        styles.add(ParagraphStyle(name='inicial', alignment=TA_JUSTIFY, spaceBefore=50))
        styles.add(ParagraphStyle(name='linhas', alignment=TA_JUSTIFY, spaceBefore=20))

        autores = ""
        orientadores = ""
        colaboradoes = ""
        disciplinas = ""
        # for autor in trabalho.autor.all():
        #     autores += (str(autor.first_name) + " " + str(autor.last_name)).title() + " (" +str(autor.turma) + "); "

        autor1 = trabalho.autor1
        autor2 = trabalho.autor2
        autor3 = trabalho.autor3
        autor4 = trabalho.autor4
        autor5 = trabalho.autor5
        autor6 = trabalho.autor6
        autor7 = trabalho.autor7

        autores += (str(autor1.first_name) + " " + str(autor1.last_name)).title() + " (" + str(autor1.turma) + "); "
        autores += (str(autor2.first_name) + " " + str(autor2.last_name)).title() + " (" + str(autor2.turma) + "); "
        autores += (str(autor3.first_name) + " " + str(autor3.last_name)).title() + " (" + str(autor3.turma) + "); "
        autores += (str(autor4.first_name) + " " + str(autor4.last_name)).title() + " (" + str(autor4.turma) + "); "
        autores += (str(autor5.first_name) + " " + str(autor5.last_name)).title() + " (" + str(autor5.turma) + "); "
        autores += (str(autor6.first_name) + " " + str(autor6.last_name)).title() + " (" + str(autor6.turma) + "); "
        if autor7:
            autores += (str(autor7.first_name) + " " + str(autor7.last_name)).title() + " (" + str(autor7.turma) + "); "

        for orientador in trabalho.orientador.orientador.all():
            orientadores += (str(orientador.orientador.first_name) + " " + str(
                orientador.orientador.last_name)).title() + "; "

        for colaborador in trabalho.colaborador.all():
            colaboradoes += (str(colaborador.first_name) + " " + str(colaborador.last_name)).title() + "; "

        for disciplina in trabalho.disciplina.all():
            disciplinas += str(disciplina.nome) + "; "

        logo = "static/media/image_upload/setting/sepe.png"
        imagem = Image(logo, 8.2 * inch, 1 * inch)
        Story.append(imagem)
        Story.append(Paragraph("<b>Título: </b>" + str(trabalho.titulo), styles["inicial"]))
        Story.append(Paragraph("<b>Integrantes do grupo: </b>" + str(autores), styles["linhas"]))
        Story.append(Paragraph("<b>Orientador: </b>" + str(orientadores), styles["linhas"]))
        Story.append(Paragraph("<b>Colaborador(es): </b>" + str(colaboradoes), styles["linhas"]))
        resumo = str(trabalho.resumo)
        Story.append(Paragraph("<b>Resumo: </b>" + resumo, styles["Justify"]))
        Story.append(Spacer(1, 12))
        doc.build(Story)

        return redirect("/" + nome)
        # render(request, self.template_consulta, {'':''})


class AceitaTrabalhoView(View):
    def group_test(user):
        return user.groups.filter(pk__in=[ORIENTADOR])

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id, status):
        template = 'index.html'

        trabalho = TrabalhoModel.objects.get(pk=id)
        print(trabalho.orientador.pk == request.user.pk)
        if trabalho.orientador.pk == request.user.pk:
            trabalho.status = StatusModels.objects.get(pk=SUBMETIDO)
            print(trabalho.status)
            trabalho.save()
        return render(request, template, {'status': trabalho.status})


class NegaTrabalhoView(View):
    def group_test(user):
        return user.groups.filter(pk__in=[ORIENTADOR])

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id, status):
        template = 'index.html'

        trabalho = TrabalhoModel.objects.get(pk=id)
        print(trabalho.orientador.pk == request.user.pk)
        if trabalho.orientador.pk == request.user.pk:
            trabalho.status = StatusModels.objects.get(pk=NEGADO_PROFESSOR)
            print(trabalho.status)
            trabalho.save()
        return render(request, template, {'status': trabalho.status})
