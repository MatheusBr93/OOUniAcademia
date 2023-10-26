from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self):
        super().__init__()
        self.__aprovacao = ""

    def media(self):
        notas = self.getNota()
        if len(notas) == 0:
            return print("Nenhuma nota registrada")
        media = sum(notas) / len(notas)
        if media >= 7.0:
            self.__aprovacao = "Aprovado"
            return print(self.__aprovacao)
        else:
            self.__aprovacao = "Reprovado"
            return print(self.__aprovacao)

    def __str__(self):
        return f"Nome: {self.getNome()}, Nota: {self.getNota()}, Aprovação: {self.__aprovacao}"