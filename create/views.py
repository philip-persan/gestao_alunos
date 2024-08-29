from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from disciplina.models import Disciplina
from professor.models import Professor
from turma.models import Aluno, Nota, Turma
from utils.make_db.create_db import AlunoFactoryDB, NotaFactoryDB


class CreateTurmaDBView(View):
    def get(self, request):
        professores = Professor.objects.all().select_related('user')
        turmas = Turma.objects.all().select_related('professor')
        notas = Nota.objects.all().select_related(
            'aluno', 'turma', 'disciplina'
        ).count()
        alunos = Aluno.objects.all().select_related(
            'turma'
        ).count()
        disciplinas = Disciplina.objects.all()
        ctx = {
            'professores': professores,
            'turmas': turmas,
            'disciplinas': disciplinas,
            'alunos': alunos,
            'notas': notas
        }
        return render(request, 'create/index.html', ctx)

    def post(self, request):
        response = request.POST
        professor_id = response['professor']
        professor = Professor.objects.get(id=professor_id)
        nome = response['nome']
        ano = int(response['ano'])
        qtd = int(response['quantidade'])
        n_turmas = 0

        try:
            nome_turma = int(nome)
        except ValueError:
            messages.error(
                request, "Nome da Turma deve ser um número Ex.: 101, 201, etc."
            )
            return redirect('create:index')

        for i in range(qtd):
            n_turmas += 1
            Turma.objects.create(
                professor=professor,
                nome=nome_turma,
                ano=ano
            )
            nome_turma += 1
        messages.success(request, f"{n_turmas} turmas criadas com sucesso!")

        return redirect('create:index')


class CreateAlunoDBView(View):
    def post(self, request):
        response = request.POST
        turma = Turma.objects.get(id=response['turma_id'])
        qtd = response['quantidade']
        alunos_factory = AlunoFactoryDB(turma=turma)

        alunos_factory.make_n_alunos(qtd)
        messages.success(request, f"{qtd} alunos criados com sucesso!")

        return redirect('create:index')


class CreateNotaDBView(View):
    def post(self, request):
        response = request.POST
        alunos = Aluno.objects.all().select_related('turma')
        start_date = response['start_date']
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = response['end_date']
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        disciplina_id = response['disciplina']
        disciplina = Disciplina.objects.get(id=disciplina_id)
        notas_factory = NotaFactoryDB(alunos)

        notas_factory.make_notas_por_disciplina(
            disciplina=disciplina,
            start_date=start_date,
            end_date=end_date
        )

        messages.success(
            request,
            f"Notas para a disciplina {disciplina} criadas com sucesso!"
        )

        return redirect('create:index')
