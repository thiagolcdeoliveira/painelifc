# coding: utf-8
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from painelifcapp.forms.trabalho import FormTrabalho, ConfiguracaoTrabalhoModel
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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Pra gerar PDF e Zip#
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


class ConsultaTrabalhoView(View):
    template = 'index.html'
    template_consulta = 'trabalho/consulta.html'

    @method_decorator(login_required)
    def get(self, request, id=None):
        is_orientador = PessoaModel.objects.filter(pk=request.user.id, groups__in=[ORIENTADOR]).exists()
        is_aluno = PessoaModel.objects.filter(pk=request.user.id, groups__in=[ALUNO]).exists()
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
                    return render(request, self.template_consulta,
                                  {'trabalho': trabalho, 'orientador': is_orientador, 'aluno': is_aluno})
                else:
                    return redirect('/')
            except:
                return redirect('/')
        else:
            trabalhos = TrabalhoModel.objects.filter(
                Q(autor1__pk=request.user.id) | Q(autor2__pk=request.user.id) | Q(
                    autor3__pk=request.user.id) | Q(autor4__pk=request.user.id) | Q(autor5__pk=request.user.id) | Q(
                    autor6__pk=request.user.id) | Q(autor7__pk=request.user.id) | Q(orientador__pk=request.user.id) | Q(
                    colaborador__pk=request.user.id) | Q(usuario=request.user.id)).distinct()
            return render(request, self.template,
                          {'trabalhos': trabalhos, 'orientador': is_orientador, 'aluno': is_aluno})


class CadastroTrabalhoView(View):
    template = 'trabalho/salvar.html'

    @method_decorator(login_required)
    def get(self, request, id=None):
        grupo_orientador = request.user.groups.filter(pk=ORIENTADOR)
        grupo = request.user.groups.filter(pk=ALUNO)

        # ajax
        if 'turma_id' in request.GET:
            import json
            als = PessoaModel.objects.filter(turma=request.GET['turma_id']).only('id', 'first_name')
            alunos = []
            for al in als:
                dict = {'id': al.id, 'nome': al.first_name + " " + al.last_name}
                alunos.append(dict)
            json = json.dumps(alunos)
            return HttpResponse(json)

        if id:
            trabalho = TrabalhoModel.objects.get(pk=id)
            form = FormTrabalho(instance=trabalho)
            turmas = []
        else:
            form = FormTrabalho()
            turmas = TurmaModel.objects.all()

            turma_usuario_logado = None
            turma_usuario_logado_id = None
            if PessoaModel.objects.get(pk=request.user.id).turma:
                turma_usuario_logado_id = PessoaModel.objects.get(pk=request.user.id).turma.id
                turma_usuario_logado = PessoaModel.objects.get(pk=request.user.id).turma.nome

        return render(request, self.template,
                      {'form': form, 'turmas': turmas, 'turma_usuario_logado': turma_usuario_logado,
                       'turma_usuario_logado_id': turma_usuario_logado_id, 'grupo_orientador': grupo_orientador,
                       'grupo': grupo})

    @method_decorator(login_required)
    def post(self, request, id=None):
        grupo = request.user.groups.filter(pk=ORIENTADOR)
        # erro = "Quantidade de autores insuficientes!"
        if id:
            trabalho = TrabalhoModel.objects.get(pk=id)
            form = FormTrabalho(instance=trabalho, data=request.POST)
        else:
            form = FormTrabalho(request.POST)

        try:
            lista_autores = [request.POST['autor1'], request.POST['autor2'], request.POST['autor3'],
                             request.POST['autor4'],
                             request.POST['autor5'], request.POST['autor6']]
        except:
            lista_autores = []
            erro = "Quantidade de autores insuficientes!"
        try:
            lista_autores.append(request.POST['autor7'])
        except:
            pass
        configuracao = ConfiguracaoTrabalhoModel.objects.order_by('id').last()
        erro = ""
        if len(lista_autores) >= 6 and len(lista_autores) <= 7:
            for i, autor in enumerate(lista_autores):
                if autor:
                    trabalhos = TrabalhoModel.objects.filter(
                        Q(colaborador__pk=autor) | Q(orientador__pk=autor) | Q(
                            autor1__pk=autor) | Q(autor2__pk=autor) | Q(autor3__pk=autor) | Q(
                            autor4__pk=autor) | Q(autor5__pk=autor) | Q(autor6__pk=autor) | Q(
                            autor7__pk=autor) | Q(usuario=autor)).distinct()
                    for autor in lista_autores:
                        if autor != None:
                            if lista_autores.count(autor) > 1:
                                erro = "Autor selecionado mais de uma vez!"
                    if (len(trabalhos) >= configuracao.trabalhos_por_autor):
                        erro = "Autor já ta inscrito!"
        else:
            erro = "Quantidade de autores insuficientes!"

        if erro != "":
            turmas = TurmaModel.objects.all()
            return render(request, self.template, {'form': form, 'turmas': turmas, "erro": erro})

        if form.is_valid():
            form_edit = form.save(commit=True)
            form_edit.usuario_id = request.user.id
            form_edit.status_id = AGUARDANDO_PROFESSOR
            form_edit.autor1.id = request.user.id
            form_edit.save()
            return redirect('/')
        turmas = TurmaModel.objects.all()
        return render(request, self.template, {'form': form, 'turmas': turmas, 'grupo': grupo})


class ImprimeTrabalhoView(View):
    template_consulta = 'trabalho/consulta.html'

    @method_decorator(login_required)
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

        autor1 = trabalho.autor1
        autor2 = trabalho.autor2
        autor3 = trabalho.autor3
        autor4 = trabalho.autor4
        autor5 = trabalho.autor5
        autor6 = trabalho.autor6
        autor7 = trabalho.autor7

        autores += (autor1.nome).title().encode('utf-8') + " (" + str(autor1.turma) + "); "
        autores += (autor2.nome).title().encode('utf-8') + " (" + str(autor2.turma) + "); "
        autores += (autor3.nome).title().encode('utf-8') + " (" + str(autor3.turma) + "); "
        autores += (autor4.nome).title().encode('utf-8') + " (" + str(autor4.turma) + "); "
        autores += (autor5.nome).title().encode('utf-8') + " (" + str(autor5.turma) + "); "
        autores += (autor6.nome).title().encode('utf-8') + " (" + str(autor6.turma) + "); "
        if autor7:
            autores += (autor7.nome).title().encode('utf-8') + " (" + str(autor7.turma) + "); "

        orientadores = (trabalho.orientador.nome).title().encode('utf-8') + "; "

        for colaborador in trabalho.colaborador.all():
            colaboradoes += (str(colaborador.nome).title().encode('utf-8')) + "; "

        for disciplina in trabalho.disciplina.all():
            print((disciplina.nome).encode('utf-8'))
            disciplinas += (disciplina.nome).encode('utf-8') + "; "

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


class AceitaTrabalhoView(View):
    def group_test(user):
        return user.groups.filter(pk__in=[ORIENTADOR])

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id, status):
        template = 'trabalho/consulta.html'
        grupo = request.user.groups.filter(pk=ORIENTADOR)
        trabalho = TrabalhoModel.objects.get(pk=id)
        if trabalho.orientador.pk == request.user.pk:
            trabalho.status = StatusModels.objects.get(pk=SUBMETIDO)
            trabalho.save()
        return render(request, template, {'status': trabalho.status, 'grupo': grupo})


class NegaTrabalhoView(View):
    def group_test(user):
        return user.groups.filter(pk__in=[ORIENTADOR, ALUNO])

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id, status):
        template = 'trabalho/consulta.html'
        grupo = request.user.groups.filter(pk=ORIENTADOR)
        trabalho = TrabalhoModel.objects.get(pk=id)
        if trabalho.orientador.pk == request.user.pk:
            trabalho.status = StatusModels.objects.get(pk=NEGADO_PROFESSOR)
            trabalho.save()
        elif trabalho.usuario.pk == request.user.pk:
            trabalho.status = StatusModels.objects.get(pk=CANCELADO_ALUNO)
            trabalho.save()
        return render(request, template, {'status': trabalho.status, 'grupo': grupo})


class AlteraTrabalhoView(View):
    def group_test(user):
        return user.groups.filter(pk__in=[ORIENTADOR])

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id, status):
        template = 'index.html'

        trabalho = TrabalhoModel.objects.get(pk=id)
        if trabalho.orientador.pk == request.user.pk:
            trabalho.status = StatusModels.objects.get(pk=NEGADO_PROFESSOR)
            trabalho.save()
        return render(request, template, {'status': trabalho.status})
