from datetime import date
from random import randint

from faker import Faker

from turma.models import Aluno, Nota, Turma

fake = Faker('pt_BR')


class TurmaFactoryDB:

    def __init__(self, professor, nome, ano) -> None:
        self.professor = professor
        self.nome = int(nome)
        self.ano = int(ano)

    def make_n_turmas(self, n: int) -> None:
        n1_turma = self.nome
        for i in range(n):
            print(f'Turma: {n1_turma}/{self.ano} criada.')
            Turma.objects.create(
                professor=self.professor,
                nome=n1_turma,
                ano=self.ano
            )
            n1_turma += 1


class AlunoFactoryDB:

    def __init__(self, turma: Turma) -> None:
        self.turma = turma

    def make_n_alunos(self, n: int) -> None:
        for i in range(n):
            aluno = Aluno.objects.create(
                nome_completo=fake.first_name() + ' ' + fake.last_name(),
                data_nascimento=fake.date_between(
                    start_date=date(2000, 1, 1),
                    end_date=date(2010, 1, 1)
                ),
                endereco=fake.address(),
                email=fake.email(),
                turma=self.turma
            )
            print(f'Aluno: {aluno.nome_completo} - {aluno.turma} criado')


class NotaFactoryDB:

    def __init__(self, alunos: Aluno) -> None:
        self.alunos = alunos

    def make_notas_por_disciplina(
        self,
        disciplina,
        start_date: date,
        end_date: date
    ) -> None:
        for aluno in self.alunos:
            Nota.objects.create(
                aluno=aluno,
                turma=aluno.turma,
                disciplina=disciplina,
                valor_nota=randint(0, 10),
                data_lancamento=fake.date_between(
                    start_date=start_date,
                    end_date=end_date
                )
            )
