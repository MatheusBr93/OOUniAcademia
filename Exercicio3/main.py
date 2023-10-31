from Aluno import Aluno
from Cidade import Cidade
from Curso import Curso
from Escola import Escola
from Escolaridade import Escolaridade
from Estado import Estado
from TipoEnsino import TipoEnsino
from Professor import Professor

def main():
    professor1 = Professor()
    professor2 = Professor()
    professor3 = Professor()
    mestrado = Escolaridade()
    doutorado = Escolaridade()
    superior = Escolaridade()
    cidade1 = Cidade()
    cidade2 = Cidade()
    curso1 = Curso()
    aluno1 = Aluno()
    aluno2 = Aluno()
    escola1 = Escola()
    estado1 = Estado()
    estado2 = Estado()
    ensinofundamental = TipoEnsino()
    ensinomedio = TipoEnsino()
    ensinosuperior = TipoEnsino()

    ensinofundamental.setNome("Ensino Fundamental")
    ensinomedio.setNome("Ensino Medio")
    ensinosuperior.setNome("Ensino Superior")

    mestrado.setNivel("Mestrado Completo")
    doutorado.setNivel('Doutorado Completo')
    superior.setNivel('Superior completo')

    cidade1.setNome('Juiz de fora')
    cidade1.setEstado(estado1)
    cidade1.adicionarEscolas(escola1)

    cidade2.setNome('Três Rios')
    cidade2.setEstado(estado2)

    estado2.setNome('Rio de Janeiro')
    estado2.adicionarCidade(cidade2)

    estado1.setNome('Minas Gerais')
    estado1.adicionarCidade(cidade1)

    professor1.setNome('Marcos Miguel')
    professor1.setEscolaridade(mestrado.getNivel())
    professor1.setCurso(curso1)

    professor2.setNome("Marco Antonio")
    professor2.setEscolaridade(doutorado.getNivel())
    professor2.setCidade(cidade2)


    professor3.setNome("Lovisi")
    professor3.setEscolaridade(superior.getNivel())
    professor3.setCurso(curso1)

    curso1.setNome("Engenharia de Software")
    curso1.setCoordenador(professor2)
    curso1.setEscola(escola1)
    curso1.setTipodeEnsino(ensinosuperior)

    escola1.setNome("Uniacademia")
    escola1.setDiretor(professor3)
    escola1.setCidade(cidade1)
    escola1.setDiretor(professor2)

    aluno1.setNome("Felipe")
    aluno1.setCidade(cidade1)
    aluno1.setCurso(curso1)

    aluno2.setNome("Pedro")
    aluno2.setCidade(cidade1)
    aluno2.setCurso(curso1)










    print(f"a)A escolaridade do professor |{professor1.getNome()}| é: |{professor1.getEscolaridade()}|")
    print(f"b)A escolaridade do coordenador |{curso1.getCoordenador()}| do curso de |{curso1.getNome()}| é: |{curso1.getCoordenador().getEscolaridade()}|")
    print(f"c)A escolaridade do diretor |{escola1.getDiretor()}| da escola |{escola1.getNome()}| é: |{escola1.getDiretor().getEscolaridade()}|")
    print(f"d)O estado de nacionalidade do aluno |{aluno1.getNome()}| é: |{aluno1.getCidade().getEstado()}|")
    print(f"e)A cidade de nascimento do professor |{professor2.getNome()}| é: |{professor2.getCidade()}|")
    print(f"f)O estado onde o aluno |{aluno2.getNome()}| estuda é: |{aluno2.getCidade().getEstado()}|")
    print(f"g)O tipo de ensino que o professor |{professor3.getNome()}| foi contratado para lesionar é: |{professor3.getCurso().getTipodeEnsino()}|")
    print(f"h)O coordenador do curso do aluno |{aluno1.getNome()}| é: |{aluno1.getCurso().getCoordenador()}|")
    print(f"i)O diretor do professor |{professor1.getNome()}| é: |{professor1.getCurso().getEscola().getDiretor()}|")
    print(f"j)O coordenador do professor |{professor3.getNome()}| é |{professor3.getCurso().getCoordenador()}|")










if __name__ == "__main__":
    main()