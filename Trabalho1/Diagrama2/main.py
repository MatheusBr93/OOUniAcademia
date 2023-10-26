from Aluno import Aluno
from Curso import Curso
from Diario import Diario
from Disciplina import Disciplina
from Instituicao import Instituicao
from Pessoa import Pessoa
from Professor import Professor
from Situacao import Situacao
from Turma import Turma
from datetime import date

def main():
    pessoa = Pessoa()
    aluno = Aluno()
    professor = Professor()
    situacao1 = Situacao()
    instituicao1 = Instituicao()
    turma1 = Turma()
    diario1 = Diario()
    disciplina1 = Disciplina()
    curso1 = Curso()


    pessoa.set_nome("Vitor")
    pessoa.set_id(1)
    pessoa.set_cpf("123.456.789-00")
    pessoa.set_dataNascimento(date(1990, 1, 15))
    pessoa.set_email("vitor@example.com")
    pessoa.set_endereco("Rua Exemplo, 123")
    pessoa.set_telefone("(12) 3456-7890")
    pessoa.set_identidade("1234567-8")


    aluno.set_nome("Vitor")
    aluno.set_cpf("123.456.789-00")
    aluno.set_dataNascimento("1990-01-15")
    aluno.set_email("vitor@example.com")
    aluno.set_endereco("Rua Exemplo, 123")
    aluno.set_telefone("(12) 3456-7890")
    aluno.set_identidade("1234567-8")
    aluno.set_matricula("2023001")
    aluno.set_anoInicio(2023)
    aluno.set_semestreInicio(1)


    professor.set_nome("John")
    professor.set_cpf("987.654.321-00")
    professor.set_dataNascimento("1975-05-20")
    professor.set_email("john@example.com")
    professor.set_endereco("Avenida Principal, 456")
    professor.set_telefone("(34) 5678-1234")
    professor.set_identidade("7654321-9")
    professor.set_matricula(12345)
    professor.set_titulacaoMaxima("Doutorado")
    professores = [professor]


    situacao1.set_situacao("Aprovado")
    situacao1.set_anoSemestre(2023)
    situacao1.set_alunos(aluno)


    instituicao1.set_id(1)
    instituicao1.set_descricao("Uniacademia")



    turma1.set_id(1)
    turma1.set_descricao("Turma de Matemática")
    turma1.set_ano(2023)
    turma1.set_semestre(1)
    turma1.set_Instituicao(instituicao1)
    turma1.set_Disciplina(disciplina1)
    turma1.set_Professor(professor)
    listaTurmas = [turma1]
    instituicao1.set_turmas(listaTurmas)


    diario1.set_v1(8.5)
    diario1.set_v2(7.5)
    diario1.set_vS(8.0)
    diario1.set_vT(8.2)
    diario1.set_faltas(2)
    diario1.set_Aluno(aluno)
    diario1.set_turma(turma1)


    disciplina1.set_id(1)
    disciplina1.set_descricao("Orientação a Objetos")
    disciplina1.set_Curso(curso1)
    disciplinas = [disciplina1]


    curso1.set_id(1)
    curso1.set_descricao("Engenharia de Software")
    curso1.set_disciplinas(disciplinas)
    curso1.set_professores(professores)

if __name__ == "__main__":
    main()

